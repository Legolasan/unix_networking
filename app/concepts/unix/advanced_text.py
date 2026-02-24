"""Advanced Text Processing - Powerful text manipulation with awk and sed."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="advanced-text",
    title="Advanced Text Processing",
    category="unix",
    difficulty="advanced",
    order=12,
    short_description="Powerful text manipulation with awk, sed, and regex",
    commands=["awk", "sed", "xargs"],
    try_it_examples=[
        TryItExample(
            title="awk: Print specific columns",
            command="cat /etc/passwd | awk -F: '{print $1, $3}'",
            description="Print username and UID with awk"
        ),
        TryItExample(
            title="awk: Filter rows",
            command="cat /etc/passwd | awk -F: '$3 >= 1000 {print $1}'",
            description="Print usernames with UID >= 1000"
        ),
        TryItExample(
            title="awk: Sum values",
            command="cat /etc/passwd | awk -F: '{sum += $3} END {print \"Total UIDs:\", sum}'",
            description="Sum all UIDs and print total"
        ),
        TryItExample(
            title="sed: Substitute text",
            command="echo 'hello world' | sed 's/world/universe/'",
            description="Replace first occurrence of 'world' with 'universe'"
        ),
        TryItExample(
            title="sed: Global replace",
            command="echo 'foo bar foo' | sed 's/foo/baz/g'",
            description="Replace ALL occurrences with g flag"
        ),
        TryItExample(
            title="xargs: Build commands",
            command="echo 'file1 file2 file3' | xargs -n1 echo 'Processing:'",
            description="Pass input as arguments to another command"
        ),
    ],
    gotchas=[
        "awk field separator: -F':' or -F: both work",
        "sed uses / as delimiter by default; use different char for paths: s|/old|/new|",
        "sed -i edits in place (careful! use -i.bak for backup)",
        "awk has BEGIN (before processing) and END (after processing) blocks",
        "xargs -I{} lets you place args anywhere: xargs -I{} cp {} /backup/",
    ],
    related=["text-processing", "pipes-redirection", "shell-scripting"],
)

register_concept(concept)
