"""Base concept class for all learning concepts."""

from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class TryItExample:
    """A 'Try It' example that can be run in the playground."""
    title: str
    command: str
    description: str = ""


@dataclass
class BaseConcept:
    """Base class for all learning concepts."""

    # Required fields
    slug: str
    title: str
    category: str  # "unix" or "networking"
    difficulty: str  # "beginner", "intermediate", "advanced"
    order: int  # Display order within category

    # Content
    short_description: str = ""
    content_template: str = ""  # Path to content template

    # Interactive examples
    try_it_examples: List[TryItExample] = field(default_factory=list)

    # Common mistakes/gotchas
    gotchas: List[str] = field(default_factory=list)

    # Related concepts (slugs)
    related: List[str] = field(default_factory=list)

    # Key commands covered
    commands: List[str] = field(default_factory=list)

    @property
    def difficulty_badge_color(self) -> str:
        """Return Tailwind color class for difficulty badge."""
        colors = {
            "beginner": "bg-green-100 text-green-800",
            "intermediate": "bg-yellow-100 text-yellow-800",
            "advanced": "bg-red-100 text-red-800",
        }
        return colors.get(self.difficulty, "bg-gray-100 text-gray-800")

    @property
    def category_icon(self) -> str:
        """Return emoji icon for category."""
        icons = {
            "unix": "🐧",
            "networking": "🌐",
        }
        return icons.get(self.category, "📚")

    def to_dict(self) -> Dict[str, Any]:
        """Convert concept to dictionary for JSON serialization."""
        return {
            "slug": self.slug,
            "title": self.title,
            "category": self.category,
            "difficulty": self.difficulty,
            "order": self.order,
            "short_description": self.short_description,
            "commands": self.commands,
            "try_it_examples": [
                {"title": e.title, "command": e.command, "description": e.description}
                for e in self.try_it_examples
            ],
        }
