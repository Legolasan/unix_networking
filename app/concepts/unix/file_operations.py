"""File Operations - Creating, copying, moving, and deleting files."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="file-operations",
    title="File Operations",
    category="unix",
    difficulty="beginner",
    order=3,
    short_description="Create, copy, move, and delete files and directories",
    commands=["touch", "mkdir", "cp", "mv", "rm", "rmdir", "file"],
    try_it_examples=[
        TryItExample(
            title="Create a file",
            command="touch myfile.txt && ls -l myfile.txt",
            description="Create an empty file (or update timestamp if exists)"
        ),
        TryItExample(
            title="Create a directory",
            command="mkdir mydir && ls -ld mydir",
            description="Create a new directory"
        ),
        TryItExample(
            title="Create nested directories",
            command="mkdir -p parent/child/grandchild && tree parent",
            description="Create parent directories as needed with -p"
        ),
        TryItExample(
            title="Copy a file",
            command="cp myfile.txt myfile_backup.txt && ls -l myfile*",
            description="Copy a file to a new name"
        ),
        TryItExample(
            title="Move/rename a file",
            command="mv myfile_backup.txt renamed.txt && ls -l *.txt",
            description="Move or rename files"
        ),
        TryItExample(
            title="Check file type",
            command="file /etc/passwd",
            description="Determine the type of a file"
        ),
    ],
    gotchas=[
        "rm is permanent - there's no trash bin in the terminal!",
        "Use rm -i for interactive confirmation before deleting",
        "rm -r removes directories recursively - be very careful",
        "cp -r is needed to copy directories",
        "mv works for both moving and renaming",
    ],
    related=["file-navigation", "permissions"],
)

register_concept(concept)
