"""Concept routes - individual concept pages."""

from flask import Blueprint, render_template, abort, jsonify
from app.concepts import get_concept, get_all_concepts, get_concepts_by_category

concepts_bp = Blueprint("concepts", __name__)


@concepts_bp.route("/")
def concept_list():
    """List all concepts organized by category."""
    unix_concepts = get_concepts_by_category("unix")
    networking_concepts = get_concepts_by_category("networking")

    return render_template(
        "concepts/list.html",
        unix_concepts=unix_concepts,
        networking_concepts=networking_concepts,
    )


@concepts_bp.route("/<slug>")
def concept_detail(slug: str):
    """Display a specific concept."""
    concept = get_concept(slug)
    if not concept:
        abort(404)

    # Get related concepts
    related_concepts = [get_concept(s) for s in concept.related if get_concept(s)]

    # Try to load concept-specific template, fall back to generic
    template_name = f"concepts/{concept.category}/{concept.slug}.html"

    return render_template(
        "concepts/detail.html",
        concept=concept,
        related_concepts=related_concepts,
        content_template=template_name,
    )


@concepts_bp.route("/<slug>/content")
def concept_content(slug: str):
    """HTMX endpoint for loading concept content."""
    concept = get_concept(slug)
    if not concept:
        abort(404)

    template_name = f"concepts/{concept.category}/{concept.slug}.html"

    try:
        return render_template(template_name, concept=concept)
    except Exception:
        # Fall back to generic content if specific template doesn't exist
        return render_template("concepts/_generic_content.html", concept=concept)


@concepts_bp.route("/api/list")
def api_concept_list():
    """API endpoint for concept list (JSON)."""
    concepts = get_all_concepts()
    return jsonify({
        slug: concept.to_dict() for slug, concept in concepts.items()
    })
