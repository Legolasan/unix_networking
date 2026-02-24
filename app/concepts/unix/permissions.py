"""File Permissions - Understanding and modifying file permissions."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="permissions",
    title="File Permissions",
    category="unix",
    difficulty="beginner",
    order=4,
    short_description="Understand and modify file permissions with chmod and chown",
    commands=["chmod", "chown", "chgrp", "ls -l", "umask"],
    try_it_examples=[
        TryItExample(
            title="View permissions",
            command="ls -la",
            description="List files with permission details (rwx format)"
        ),
        TryItExample(
            title="Make file executable",
            command="touch script.sh && chmod +x script.sh && ls -l script.sh",
            description="Add execute permission to a file"
        ),
        TryItExample(
            title="Set specific permissions (octal)",
            command="chmod 755 script.sh && ls -l script.sh",
            description="rwxr-xr-x: owner can do all, others can read/execute"
        ),
        TryItExample(
            title="Remove write permission",
            command="chmod -w script.sh && ls -l script.sh",
            description="Make a file read-only"
        ),
        TryItExample(
            title="View current umask",
            command="umask",
            description="Show default permission mask for new files"
        ),
        TryItExample(
            title="View file owner",
            command="ls -la /etc/passwd",
            description="See owner and group of a file"
        ),
    ],
    gotchas=[
        "Permission format: rwxrwxrwx (owner/group/others)",
        "r=4, w=2, x=1 for octal notation (755 = rwxr-xr-x)",
        "Directories need execute permission to enter them",
        "Only root or the owner can change permissions",
        "Scripts need execute permission AND readable content to run",
    ],
    related=["file-operations", "viewing-files"],
)

register_concept(concept)
