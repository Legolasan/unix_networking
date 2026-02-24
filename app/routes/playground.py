"""Playground routes - interactive terminal with session-based containers."""

import uuid
from flask import Blueprint, render_template, request, jsonify, current_app, session
from app.terminal.session_sandbox import session_sandbox

playground_bp = Blueprint("playground", __name__)


@playground_bp.before_request
def ensure_session():
    """Ensure user has a session ID for their sandbox container."""
    if "sandbox_id" not in session:
        session["sandbox_id"] = str(uuid.uuid4())[:8]
        session.permanent = True


@playground_bp.route("/")
def playground():
    """Interactive terminal playground."""
    # Get initial command from query param (for "Try It" links)
    initial_command = request.args.get("cmd", "")
    concept_slug = request.args.get("from", "")

    return render_template(
        "playground.html",
        initial_command=initial_command,
        concept_slug=concept_slug,
    )


@playground_bp.route("/execute", methods=["POST"])
def execute():
    """Execute a command in the user's session container."""
    data = request.get_json()
    command = data.get("command", "").strip()

    if not command:
        return jsonify({"error": "No command provided", "output": ""})

    # Security: Basic command filtering
    blocked_commands = ["rm -rf /", ":(){ :|:& };:", "dd if=/dev/zero"]
    for blocked in blocked_commands:
        if blocked in command:
            return jsonify({
                "error": "This command is not allowed in the sandbox",
                "output": "",
            })

    try:
        session_id = session.get("sandbox_id")
        result = session_sandbox.execute_command(
            session_id=session_id,
            command=command,
            image=current_app.config.get("DOCKER_IMAGE", "linux-sandbox:latest"),
        )
        return jsonify(result)
    except Exception as e:
        return jsonify({
            "error": str(e),
            "output": "",
        })


@playground_bp.route("/status")
def sandbox_status():
    """Check sandbox container status for current session."""
    session_id = session.get("sandbox_id")
    if not session_id:
        return jsonify({
            "running": False,
            "status": "no_session",
            "id": None,
        })

    status = session_sandbox.get_session_status(session_id)
    return jsonify(status)


@playground_bp.route("/reset", methods=["POST"])
def reset_sandbox():
    """Reset the sandbox to a clean state for current session."""
    try:
        session_id = session.get("sandbox_id")
        image = current_app.config.get("DOCKER_IMAGE", "linux-sandbox:latest")
        result = session_sandbox.reset_session(session_id, image)
        return jsonify(result)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@playground_bp.route("/cleanup", methods=["POST"])
def cleanup_expired():
    """
    Clean up expired session containers.

    This endpoint can be called by a cron job or scheduler to remove
    containers that have been idle for more than 30 minutes.

    For security, this should be protected in production (e.g., API key).
    """
    try:
        result = session_sandbox.cleanup_expired()
        return jsonify({
            "success": True,
            **result,
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@playground_bp.route("/sessions")
def list_sessions():
    """
    List active session containers (admin endpoint).

    For debugging and monitoring. Should be protected in production.
    """
    try:
        result = session_sandbox.list_active_sessions()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e), "sessions": []})
