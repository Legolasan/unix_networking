"""File System Navigation - Moving around the file system."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="file-navigation",
    title="File System Navigation",
    category="unix",
    difficulty="beginner",
    order=2,
    short_description="Navigate directories with ls, cd, pwd, and understand paths",
    commands=["ls", "cd", "pwd", "tree"],
    try_it_examples=[
        TryItExample(
            title="Print working directory",
            command="pwd",
            description="Show your current location in the file system"
        ),
        TryItExample(
            title="List files",
            command="ls",
            description="List contents of current directory"
        ),
        TryItExample(
            title="Detailed listing",
            command="ls -la",
            description="List all files with details (permissions, size, date)"
        ),
        TryItExample(
            title="Navigate to home",
            command="cd ~ && pwd",
            description="Go to your home directory"
        ),
        TryItExample(
            title="View directory tree",
            command="tree -L 2",
            description="Show directory structure as a tree (2 levels deep)"
        ),
        TryItExample(
            title="Go up one level",
            command="cd .. && pwd",
            description="Move to the parent directory"
        ),
    ],
    gotchas=[
        "~ (tilde) is a shortcut for your home directory",
        ". (single dot) refers to the current directory",
        ".. (double dot) refers to the parent directory",
        "Absolute paths start with /, relative paths don't",
        "Tab completion saves typing - start typing and press Tab",
    ],
    related=["unix-basics", "file-operations"],
)

register_concept(concept)
