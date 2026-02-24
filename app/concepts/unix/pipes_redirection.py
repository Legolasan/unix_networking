"""Pipes & Redirection - Connecting commands and controlling I/O."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="pipes-redirection",
    title="Pipes & Redirection",
    category="unix",
    difficulty="intermediate",
    order=6,
    short_description="Connect commands with pipes and control input/output",
    commands=["|", ">", ">>", "<", "2>&1", "tee"],
    try_it_examples=[
        TryItExample(
            title="Basic pipe",
            command="ls -la /etc | head -10",
            description="Send output of ls to head (show first 10 lines)"
        ),
        TryItExample(
            title="Multiple pipes",
            command="cat /etc/passwd | cut -d: -f1 | sort | head -5",
            description="Chain commands: extract usernames, sort, show first 5"
        ),
        TryItExample(
            title="Redirect output to file",
            command="ls /etc > /tmp/filelist.txt && cat /tmp/filelist.txt | head -5",
            description="Write output to a file with >"
        ),
        TryItExample(
            title="Append to file",
            command="echo 'first line' > /tmp/test.txt && echo 'second line' >> /tmp/test.txt && cat /tmp/test.txt",
            description="Append output to file with >>"
        ),
        TryItExample(
            title="Redirect stderr and stdout",
            command="ls /nonexistent /etc 2>&1 | head -5",
            description="Combine stderr with stdout using 2>&1"
        ),
        TryItExample(
            title="Tee - write and pass through",
            command="ls /etc | tee /tmp/etc_files.txt | wc -l && echo '---' && head -3 /tmp/etc_files.txt",
            description="tee writes to file while also passing data through"
        ),
    ],
    gotchas=[
        "> overwrites the file; >> appends to it",
        "2>&1 must come AFTER the redirect (cmd > file 2>&1)",
        "Pipes connect stdout of one command to stdin of the next",
        "/dev/null is a black hole - redirects discard output",
        "Use | less to paginate long output",
    ],
    related=["unix-basics", "text-processing", "text-search"],
)

register_concept(concept)
