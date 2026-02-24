"""Text Processing - Transforming text with cut, sort, uniq, and tr."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="text-processing",
    title="Text Processing",
    category="unix",
    difficulty="intermediate",
    order=8,
    short_description="Transform and manipulate text with cut, sort, uniq, and tr",
    commands=["cut", "sort", "uniq", "tr", "wc", "paste"],
    try_it_examples=[
        TryItExample(
            title="Extract columns with cut",
            command="cat /etc/passwd | cut -d: -f1,3",
            description="Extract username and UID (fields 1 and 3, : delimiter)"
        ),
        TryItExample(
            title="Sort lines",
            command="cat /etc/passwd | cut -d: -f3 | sort -n | head -10",
            description="Sort UIDs numerically"
        ),
        TryItExample(
            title="Count unique values",
            command="cat /etc/passwd | cut -d: -f7 | sort | uniq -c | sort -rn",
            description="Count occurrences of each shell"
        ),
        TryItExample(
            title="Translate characters",
            command="echo 'hello world' | tr 'a-z' 'A-Z'",
            description="Convert lowercase to uppercase"
        ),
        TryItExample(
            title="Delete characters",
            command="echo 'hello 123 world' | tr -d '0-9'",
            description="Remove all digits with tr -d"
        ),
        TryItExample(
            title="Word and line count",
            command="wc -lwc /etc/passwd",
            description="Count lines, words, and characters"
        ),
    ],
    gotchas=[
        "uniq only removes ADJACENT duplicates - sort first!",
        "cut -d sets delimiter (default is tab)",
        "sort -n for numeric, -r for reverse, -k for specific field",
        "tr works on characters, not strings",
        "wc -l counts newlines, not lines (differs for files without trailing newline)",
    ],
    related=["pipes-redirection", "text-search", "advanced-text"],
)

register_concept(concept)
