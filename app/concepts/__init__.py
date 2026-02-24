"""Concept registration and management."""

from typing import Dict, Type
from app.concepts.base import BaseConcept

# Registry of all concepts
_concepts: Dict[str, BaseConcept] = {}


def register_concept(concept: BaseConcept):
    """Register a concept in the global registry."""
    _concepts[concept.slug] = concept


def get_concept(slug: str) -> BaseConcept | None:
    """Get a concept by its slug."""
    return _concepts.get(slug)


def get_all_concepts() -> Dict[str, BaseConcept]:
    """Get all registered concepts."""
    return _concepts.copy()


def get_concepts_by_category(category: str) -> list[BaseConcept]:
    """Get all concepts in a category, sorted by order."""
    return sorted(
        [c for c in _concepts.values() if c.category == category],
        key=lambda c: c.order
    )


def register_all_concepts(app):
    """Register all concepts with the application."""
    # Import and register Unix concepts - Beginner
    from app.concepts.unix import unix_basics
    from app.concepts.unix import file_navigation
    from app.concepts.unix import file_operations
    from app.concepts.unix import permissions
    from app.concepts.unix import viewing_files

    # Import and register Unix concepts - Intermediate
    from app.concepts.unix import pipes_redirection
    from app.concepts.unix import text_search
    from app.concepts.unix import text_processing
    from app.concepts.unix import processes
    from app.concepts.unix import environment

    # Import and register Unix concepts - Advanced
    from app.concepts.unix import shell_scripting
    from app.concepts.unix import advanced_text
    from app.concepts.unix import job_control
    from app.concepts.unix import system_admin
    from app.concepts.unix import cron_scheduling
    from app.concepts.unix import package_management

    # Import and register Networking concepts - Beginner
    from app.concepts.networking import fundamentals
    from app.concepts.networking import ip_addressing
    from app.concepts.networking import ports_protocols
    from app.concepts.networking import dns_explained

    # Import and register Networking concepts - Intermediate
    from app.concepts.networking import http_web
    from app.concepts.networking import connectivity_testing
    from app.concepts.networking import dns_tools
    from app.concepts.networking import network_inspection
    from app.concepts.networking import data_transfer

    # Import and register Networking concepts - Advanced
    from app.concepts.networking import packet_analysis
    from app.concepts.networking import wireshark
    from app.concepts.networking import firewalls
    from app.concepts.networking import network_namespaces
    from app.concepts.networking import sockets
    from app.concepts.networking import troubleshooting

    # Store concepts in app context for templates
    app.config["CONCEPTS"] = _concepts
