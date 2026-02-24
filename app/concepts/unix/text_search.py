"""Text Search - Finding files and content with grep and find."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="text-search",
    title="Text Search",
    category="unix",
    difficulty="intermediate",
    order=7,
    short_description="Find files and search content with grep and find",
    commands=["grep", "find", "locate", "which", "whereis"],
    try_it_examples=[
        TryItExample(
            title="Search file content",
            command="grep 'root' /etc/passwd",
            description="Find lines containing 'root' in passwd file"
        ),
        TryItExample(
            title="Case-insensitive search",
            command="grep -i 'ROOT' /etc/passwd",
            description="Search ignoring case with -i"
        ),
        TryItExample(
            title="Recursive search",
            command="grep -r 'hosts' /etc/*.conf 2>/dev/null | head -5",
            description="Search recursively in all .conf files"
        ),
        TryItExample(
            title="Find files by name",
            command="find /etc -name '*.conf' 2>/dev/null | head -10",
            description="Find all .conf files under /etc"
        ),
        TryItExample(
            title="Find files by size",
            command="find /var/log -size +100k 2>/dev/null | head -5",
            description="Find files larger than 100KB"
        ),
        TryItExample(
            title="Find and execute",
            command="find /etc -name '*.conf' -exec wc -l {} \\; 2>/dev/null | head -5",
            description="Find files and count lines in each"
        ),
    ],
    gotchas=[
        "grep -r can be slow on large directories; use -l to just list files",
        "find uses -name for exact match, -iname for case-insensitive",
        "Quote your search patterns to prevent shell expansion",
        "grep returns exit code 1 if no match (useful in scripts)",
        "Use grep -v to invert match (show lines NOT matching)",
    ],
    related=["pipes-redirection", "text-processing", "viewing-files"],
)

register_concept(concept)
