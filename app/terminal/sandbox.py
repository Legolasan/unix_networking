"""Sandbox container management."""

import docker
from docker.errors import DockerException, NotFound
from typing import Dict, Any, Optional


class SandboxManager:
    """Manages the sandbox container lifecycle."""

    CONTAINER_NAME = "linux-learn-sandbox"
    DEFAULT_IMAGE = "linux-sandbox:latest"

    def __init__(self):
        self._client: Optional[docker.DockerClient] = None

    @property
    def client(self) -> docker.DockerClient:
        """Lazy initialization of Docker client."""
        if self._client is None:
            try:
                self._client = docker.from_env()
            except DockerException as e:
                raise RuntimeError(f"Docker is not available: {e}")
        return self._client

    def get_status(self) -> Dict[str, Any]:
        """Get the current status of the sandbox."""
        try:
            container = self.client.containers.get(self.CONTAINER_NAME)
            return {
                "running": container.status == "running",
                "status": container.status,
                "id": container.short_id,
                "image": container.image.tags[0] if container.image.tags else "unknown",
            }
        except NotFound:
            return {
                "running": False,
                "status": "not_created",
                "id": None,
                "image": None,
            }
        except DockerException as e:
            return {
                "running": False,
                "status": "error",
                "error": str(e),
            }

    def start(self, image: str = None) -> Dict[str, Any]:
        """Start a persistent sandbox container."""
        image = image or self.DEFAULT_IMAGE

        # Check if already running
        status = self.get_status()
        if status.get("running"):
            return {"success": True, "message": "Sandbox already running", **status}

        # Remove any stopped container with same name
        try:
            old = self.client.containers.get(self.CONTAINER_NAME)
            old.remove(force=True)
        except NotFound:
            pass

        try:
            container = self.client.containers.run(
                image,
                name=self.CONTAINER_NAME,
                detach=True,
                tty=True,
                stdin_open=True,
                mem_limit="512m",
                cpu_period=100000,
                cpu_quota=50000,
                # Keep container running
                command="/bin/bash",
            )
            return {
                "success": True,
                "message": "Sandbox started",
                "id": container.short_id,
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
            }

    def stop(self) -> Dict[str, Any]:
        """Stop the sandbox container."""
        try:
            container = self.client.containers.get(self.CONTAINER_NAME)
            container.stop(timeout=5)
            container.remove()
            return {"success": True, "message": "Sandbox stopped"}
        except NotFound:
            return {"success": True, "message": "Sandbox was not running"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def reset(self) -> Dict[str, Any]:
        """Reset the sandbox to a clean state."""
        self.stop()
        return self.start()

    def exec_command(self, command: str, workdir: str = "/home/learner") -> Dict[str, Any]:
        """Execute a command in the running sandbox."""
        status = self.get_status()
        if not status.get("running"):
            # Start if not running
            start_result = self.start()
            if not start_result.get("success"):
                return {"output": "", "exit_code": -1, "error": start_result.get("error")}

        try:
            container = self.client.containers.get(self.CONTAINER_NAME)
            exit_code, output = container.exec_run(
                f"/bin/bash -c {repr(command)}",
                workdir=workdir,
                demux=False,
            )
            return {
                "output": output.decode("utf-8") if output else "",
                "exit_code": exit_code,
                "error": None,
            }
        except Exception as e:
            return {
                "output": "",
                "exit_code": -1,
                "error": str(e),
            }
