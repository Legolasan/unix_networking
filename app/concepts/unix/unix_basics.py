"""Unix Basics - Introduction to Unix/Linux and terminal fundamentals."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="unix-basics",
    title="Unix Basics",
    category="unix",
    difficulty="beginner",
    order=1,
    short_description="What is Unix/Linux, terminal basics, and shell concepts",
    commands=["echo", "whoami", "hostname", "date", "clear", "history"],
    try_it_examples=[
        TryItExample(
            title="Who am I?",
            command="whoami",
            description="Display the current username"
        ),
        TryItExample(
            title="Current date and time",
            command="date",
            description="Show the current system date and time"
        ),
        TryItExample(
            title="Echo a message",
            command="echo 'Hello, Unix!'",
            description="Print text to the terminal"
        ),
        TryItExample(
            title="System hostname",
            command="hostname",
            description="Display the name of the current host"
        ),
        TryItExample(
            title="View command history",
            command="history | tail -10",
            description="Show the last 10 commands you've run"
        ),
    ],
    gotchas=[
        "Linux is case-sensitive: 'File.txt' and 'file.txt' are different files",
        "Commands are separated from arguments by spaces",
        "Most commands have a --help flag for quick reference",
        "Use 'man command' for detailed documentation",
    ],
    related=["file-navigation", "file-operations"],
)

register_concept(concept)
