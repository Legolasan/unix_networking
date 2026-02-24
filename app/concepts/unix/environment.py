"""Environment - Shell environment variables and configuration."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="environment",
    title="Environment",
    category="unix",
    difficulty="intermediate",
    order=10,
    short_description="Work with environment variables, PATH, and shell config",
    commands=["env", "export", "echo", "source", "printenv"],
    try_it_examples=[
        TryItExample(
            title="View all environment variables",
            command="env | head -15",
            description="List all current environment variables"
        ),
        TryItExample(
            title="Print specific variable",
            command="echo $PATH",
            description="Display the PATH variable"
        ),
        TryItExample(
            title="Set and export variable",
            command="export MY_VAR='hello' && echo $MY_VAR",
            description="Create environment variable available to child processes"
        ),
        TryItExample(
            title="View PATH directories",
            command="echo $PATH | tr ':' '\\n'",
            description="Show PATH as separate lines"
        ),
        TryItExample(
            title="Check shell config files",
            command="ls -la ~ | grep -E '\\.(bash|profile|zsh)'",
            description="List shell configuration files"
        ),
        TryItExample(
            title="View common variables",
            command="echo \"USER=$USER HOME=$HOME SHELL=$SHELL\"",
            description="Display common environment variables"
        ),
    ],
    gotchas=[
        "export makes vars available to child processes; without it, they're local",
        "Changes to .bashrc require 'source ~/.bashrc' or new shell to take effect",
        "PATH is searched left-to-right; first match wins",
        "$VAR and ${VAR} are equivalent; braces help with concatenation",
        "Single quotes prevent variable expansion; double quotes allow it",
    ],
    related=["unix-basics", "shell-scripting", "processes"],
)

register_concept(concept)
