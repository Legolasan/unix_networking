"""Main routes - home page and navigation."""

from flask import Blueprint, render_template, current_app
from app.concepts import get_concepts_by_category

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    """Home page with overview of all concepts."""
    unix_concepts = get_concepts_by_category("unix")
    networking_concepts = get_concepts_by_category("networking")

    return render_template(
        "index.html",
        unix_concepts=unix_concepts,
        networking_concepts=networking_concepts,
    )


@main_bp.route("/about")
def about():
    """About page with project information."""
    return render_template("about.html")
