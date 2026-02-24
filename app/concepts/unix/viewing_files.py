"""Viewing Files - Reading and inspecting file contents."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="viewing-files",
    title="Viewing Files",
    category="unix",
    difficulty="beginner",
    order=5,
    short_description="View file contents with cat, less, head, tail, and wc",
    commands=["cat", "less", "head", "tail", "wc", "nl"],
    try_it_examples=[
        TryItExample(
            title="View entire file",
            command="cat /etc/os-release",
            description="Display the entire contents of a file"
        ),
        TryItExample(
            title="First 5 lines",
            command="head -5 /var/log/sample-app.log",
            description="Show only the first N lines of a file"
        ),
        TryItExample(
            title="Last 5 lines",
            command="tail -5 /var/log/sample-app.log",
            description="Show the last N lines (great for logs)"
        ),
        TryItExample(
            title="Count lines, words, characters",
            command="wc /etc/passwd",
            description="Count lines, words, and bytes in a file"
        ),
        TryItExample(
            title="Count lines only",
            command="wc -l /etc/passwd",
            description="Just count the number of lines"
        ),
        TryItExample(
            title="View with line numbers",
            command="nl /var/log/sample-app.log",
            description="Display file contents with line numbers"
        ),
    ],
    gotchas=[
        "cat prints everything at once - bad for large files",
        "Use less for large files (press q to quit, / to search)",
        "tail -f follows a file in real-time (great for logs)",
        "head/tail default to 10 lines if -n not specified",
        "wc output is: lines words bytes filename",
    ],
    related=["permissions", "pipes-redirection"],
)

register_concept(concept)
