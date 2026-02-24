"""Data Transfer - Transfer files with curl, wget, scp, and rsync."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="data-transfer",
    title="Data Transfer",
    category="networking",
    difficulty="intermediate",
    order=9,
    short_description="Transfer files with curl, wget, scp, and rsync",
    commands=["curl", "wget", "scp", "rsync"],
    try_it_examples=[
        TryItExample(
            title="Download with curl",
            command="curl -sO https://example.com/index.html && ls -la index.html && rm index.html",
            description="Download file keeping original name"
        ),
        TryItExample(
            title="Download with wget",
            command="wget -q https://example.com/index.html -O /tmp/wget_test.html && head -5 /tmp/wget_test.html",
            description="Download and save with custom name"
        ),
        TryItExample(
            title="Show download progress",
            command="curl -# -o /tmp/curl_test.html https://example.com/index.html && echo 'Downloaded!'",
            description="Progress bar download with curl"
        ),
        TryItExample(
            title="Resume interrupted download",
            command="echo 'curl -C - -O http://example.com/largefile.zip'",
            description="Continue partial download with -C -"
        ),
        TryItExample(
            title="rsync dry run",
            command="rsync -avnc /etc/passwd /tmp/ 2>/dev/null && echo 'Dry run complete'",
            description="Test rsync without making changes (-n = dry run)"
        ),
        TryItExample(
            title="rsync with progress",
            command="rsync -av --progress /etc/hostname /tmp/hostname_backup",
            description="Copy with archive mode and progress"
        ),
    ],
    gotchas=[
        "curl -O uses remote filename; -o lets you specify local name",
        "wget is better for recursive downloads; curl for API calls",
        "scp syntax: scp source user@host:destination",
        "rsync -a preserves permissions, timestamps, symlinks (archive mode)",
        "rsync only transfers differences - great for backups",
    ],
    related=["http-web", "connectivity-testing", "ports-protocols"],
)

register_concept(concept)
