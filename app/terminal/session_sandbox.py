"""Session-based sandbox container management for multi-user support."""

import docker
import threading
import time
from docker.errors import DockerException, NotFound, ImageNotFound
from typing import Dict, Any, Optional
from datetime import datetime, timedelta


class SessionSandbox:
    """
    Manages per-session sandbox containers.

    Each user session gets their own persistent Docker container,
    allowing state to persist across command executions.
    Containers are automatically cleaned up after 30 minutes of inactivity.
    """

    CONTAINER_PREFIX = "learn-"
    DEFAULT_IMAGE = "linux-sandbox:latest"
    IDLE_TIMEOUT_MINUTES = 30

    def __init__(self):
        self._client: Optional[docker.DockerClient] = None
        self._lock = threading.RLock()
        # Track last activity time for each session
        self._last_activity: Dict[str, datetime] = {}

    @property
    def client(self) -> docker.DockerClient:
        """Lazy initialization of Docker client."""
        if self._client is None:
            try:
                self._client = docker.from_env()
            except DockerException as e:
                raise RuntimeError(f"Docker is not available: {e}")
        return self._client

    def _container_name(self, session_id: str) -> str:
        """Get container name for a session."""
        return f"{self.CONTAINER_PREFIX}{session_id}"

    def _update_activity(self, session_id: str) -> None:
        """Update last activity timestamp for a session."""
        self._last_activity[session_id] = datetime.now()

    def get_or_create_container(
        self, session_id: str, image: str = None
    ) -> Dict[str, Any]:
        """
        Get existing container for session or create a new one.

        Args:
            session_id: Unique session identifier
            image: Docker image to use (defaults to DEFAULT_IMAGE)

        Returns:
            Dictionary with container info or error
        """
        image = image or self.DEFAULT_IMAGE
        container_name = self._container_name(session_id)

        with self._lock:
            try:
                # Check if container already exists
                container = self.client.containers.get(container_name)

                # If it exists but isn't running, start it
                if container.status != "running":
                    container.start()

                self._update_activity(session_id)
                return {
                    "success": True,
                    "container_id": container.short_id,
                    "status": "running",
                    "created": False,
                }

            except NotFound:
                # Container doesn't exist, create it
                pass

            # Check if image exists
            try:
                self.client.images.get(image)
            except ImageNotFound:
                return {
                    "success": False,
                    "error": f"Docker image '{image}' not found. Run 'docker build -t {image} docker/' to build it.",
                }

            try:
                container = self.client.containers.run(
                    image,
                    name=container_name,
                    detach=True,
                    tty=True,
                    stdin_open=True,
                    mem_limit="256m",
                    cpu_period=100000,
                    cpu_quota=50000,  # 50% CPU
                    command="/bin/bash",
                    labels={"learn-session": session_id},
                )
                self._update_activity(session_id)
                return {
                    "success": True,
                    "container_id": container.short_id,
                    "status": "running",
                    "created": True,
                }

            except Exception as e:
                return {
                    "success": False,
                    "error": str(e),
                }

    def execute_command(
        self,
        session_id: str,
        command: str,
        workdir: str = "/home/learner",
        image: str = None,
    ) -> Dict[str, Any]:
        """
        Execute a command in the session's container.

        Args:
            session_id: Unique session identifier
            command: Shell command to execute
            workdir: Working directory inside the container
            image: Docker image to use if container needs to be created

        Returns:
            Dictionary with output, exit_code, and optionally error
        """
        # Ensure container exists
        container_result = self.get_or_create_container(session_id, image)
        if not container_result.get("success"):
            return {
                "output": "",
                "exit_code": -1,
                "error": container_result.get("error"),
            }

        container_name = self._container_name(session_id)

        with self._lock:
            try:
                container = self.client.containers.get(container_name)
                exit_code, output = container.exec_run(
                    f"/bin/bash -c {repr(command)}",
                    workdir=workdir,
                    demux=False,
                )
                self._update_activity(session_id)
                return {
                    "output": output.decode("utf-8") if output else "",
                    "exit_code": exit_code,
                    "error": None,
                }

            except NotFound:
                return {
                    "output": "",
                    "exit_code": -1,
                    "error": "Container not found. Please try again.",
                }

            except Exception as e:
                return {
                    "output": "",
                    "exit_code": -1,
                    "error": str(e),
                }

    def reset_session(self, session_id: str, image: str = None) -> Dict[str, Any]:
        """
        Destroy and recreate the session's container.

        Args:
            session_id: Unique session identifier
            image: Docker image to use for new container

        Returns:
            Dictionary with success status and message
        """
        container_name = self._container_name(session_id)

        with self._lock:
            # Remove existing container
            try:
                container = self.client.containers.get(container_name)
                container.remove(force=True)
            except NotFound:
                pass
            except Exception as e:
                return {"success": False, "error": f"Failed to remove container: {e}"}

            # Clear activity tracking
            self._last_activity.pop(session_id, None)

            # Create fresh container
            result = self.get_or_create_container(session_id, image)
            if result.get("success"):
                return {"success": True, "message": "Sandbox reset successfully"}
            return {"success": False, "error": result.get("error")}

    def get_session_status(self, session_id: str) -> Dict[str, Any]:
        """
        Get the status of a session's container.

        Args:
            session_id: Unique session identifier

        Returns:
            Dictionary with container status information
        """
        container_name = self._container_name(session_id)

        try:
            container = self.client.containers.get(container_name)
            last_activity = self._last_activity.get(session_id)
            return {
                "running": container.status == "running",
                "status": container.status,
                "id": container.short_id,
                "session_id": session_id,
                "last_activity": last_activity.isoformat() if last_activity else None,
            }
        except NotFound:
            return {
                "running": False,
                "status": "not_created",
                "id": None,
                "session_id": session_id,
            }
        except DockerException as e:
            return {
                "running": False,
                "status": "error",
                "error": str(e),
                "session_id": session_id,
            }

    def cleanup_expired(self) -> Dict[str, Any]:
        """
        Remove containers that have been idle for more than IDLE_TIMEOUT_MINUTES.

        Returns:
            Dictionary with cleanup results
        """
        cutoff = datetime.now() - timedelta(minutes=self.IDLE_TIMEOUT_MINUTES)
        removed = []
        errors = []

        with self._lock:
            # Find expired sessions
            expired_sessions = [
                session_id
                for session_id, last_active in self._last_activity.items()
                if last_active < cutoff
            ]

            # Also find any orphaned containers (in case activity wasn't tracked)
            try:
                containers = self.client.containers.list(
                    all=True,
                    filters={"name": self.CONTAINER_PREFIX},
                )
                for container in containers:
                    # Extract session_id from container name
                    if container.name.startswith(self.CONTAINER_PREFIX):
                        session_id = container.name[len(self.CONTAINER_PREFIX):]
                        if session_id not in self._last_activity:
                            # No activity tracked, consider it expired
                            expired_sessions.append(session_id)
            except Exception:
                pass

            # Remove expired containers
            for session_id in set(expired_sessions):
                container_name = self._container_name(session_id)
                try:
                    container = self.client.containers.get(container_name)
                    container.remove(force=True)
                    removed.append(session_id)
                    self._last_activity.pop(session_id, None)
                except NotFound:
                    # Already removed
                    self._last_activity.pop(session_id, None)
                except Exception as e:
                    errors.append({"session_id": session_id, "error": str(e)})

        return {
            "removed_count": len(removed),
            "removed_sessions": removed,
            "errors": errors,
        }

    def list_active_sessions(self) -> Dict[str, Any]:
        """
        List all active session containers.

        Returns:
            Dictionary with list of active sessions
        """
        sessions = []

        try:
            containers = self.client.containers.list(
                all=True,
                filters={"name": self.CONTAINER_PREFIX},
            )
            for container in containers:
                if container.name.startswith(self.CONTAINER_PREFIX):
                    session_id = container.name[len(self.CONTAINER_PREFIX):]
                    last_activity = self._last_activity.get(session_id)
                    sessions.append({
                        "session_id": session_id,
                        "container_id": container.short_id,
                        "status": container.status,
                        "last_activity": last_activity.isoformat() if last_activity else None,
                    })
        except Exception as e:
            return {"error": str(e), "sessions": []}

        return {"sessions": sessions, "count": len(sessions)}


# Singleton instance for the application
session_sandbox = SessionSandbox()
