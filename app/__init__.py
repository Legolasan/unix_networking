"""Flask application factory for Unix & Networking learning platform."""

import os
from datetime import timedelta
from flask import Flask


def create_app(config=None):
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # Default configuration
    app.config.update(
        # Security: Use environment variable in production
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev-key-change-in-production"),
        DOCKER_IMAGE="linux-sandbox:latest",
        DOCKER_TIMEOUT=30,
        # Session configuration
        SESSION_COOKIE_SECURE=os.environ.get("FLASK_ENV") == "production",
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
        PERMANENT_SESSION_LIFETIME=timedelta(hours=2),
    )

    # Override with custom config if provided
    if config:
        app.config.update(config)

    # Register blueprints
    from app.routes.main import main_bp
    from app.routes.concepts import concepts_bp
    from app.routes.playground import playground_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(concepts_bp, url_prefix="/concepts")
    app.register_blueprint(playground_bp, url_prefix="/playground")

    # Register concepts
    from app.concepts import register_all_concepts
    register_all_concepts(app)

    return app
