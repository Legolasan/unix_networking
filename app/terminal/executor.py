"""Docker-based command execution for the sandbox environment."""

import docker
from docker.errors import DockerException, ImageNotFound, APIError
from typing import Dict, Any


def get_docker_client():
    """Get Docker client, with helpful error message if Docker isn't available."""
    try:
        client = docker.from_env()
        client.ping()
        return client
    except DockerException as e:
        raise RuntimeError(
            "Docker is not available. Please ensure Docker is installed and running. "
            f"Error: {e}"
        )


def execute_command(
    command: str,
    timeout: int = 30,
    image: str = "linux-sandbox:latest",
    working_dir: str = "/home/learner",
) -> Dict[str, Any]:
    """
    Execute a command in a Docker container and return the result.

    Args:
        command: The shell command to execute
        timeout: Maximum execution time in seconds
        image: Docker image to use
        working_dir: Working directory inside the container

    Returns:
        Dictionary with 'output', 'exit_code', and optionally 'error'
    """
    try:
        client = get_docker_client()
    except RuntimeError as e:
        return {
            "output": "",
            "exit_code": -1,
            "error": str(e),
        }

    try:
        # Check if image exists
        try:
            client.images.get(image)
        except ImageNotFound:
            return {
                "output": "",
                "exit_code": -1,
                "error": f"Docker image '{image}' not found. Run 'docker build -t {image} docker/' to build it.",
            }

        # Run command in container
        container = client.containers.run(
            image,
            command=f"/bin/bash -c {repr(command)}",
            working_dir=working_dir,
            remove=True,
            detach=False,
            stdout=True,
            stderr=True,
            # Security constraints
            mem_limit="256m",
            cpu_period=100000,
            cpu_quota=50000,  # 50% CPU
            network_mode="bridge",
            # Timeouts
            # Note: actual timeout is handled by Docker daemon
        )

        # Docker SDK returns bytes
        output = container.decode("utf-8") if isinstance(container, bytes) else str(container)

        return {
            "output": output,
            "exit_code": 0,
            "error": None,
        }

    except docker.errors.ContainerError as e:
        # Command executed but returned non-zero exit code
        output = e.stderr.decode("utf-8") if e.stderr else ""
        return {
            "output": output,
            "exit_code": e.exit_status,
            "error": None,  # Not an error, just non-zero exit
        }

    except APIError as e:
        return {
            "output": "",
            "exit_code": -1,
            "error": f"Docker API error: {e}",
        }

    except Exception as e:
        return {
            "output": "",
            "exit_code": -1,
            "error": f"Unexpected error: {e}",
        }


def check_image_exists(image: str = "linux-sandbox:latest") -> bool:
    """Check if the sandbox Docker image exists."""
    try:
        client = get_docker_client()
        client.images.get(image)
        return True
    except (ImageNotFound, RuntimeError):
        return False
