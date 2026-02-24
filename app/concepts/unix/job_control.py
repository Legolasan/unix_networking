"""Job Control - Managing background processes and terminal sessions."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="job-control",
    title="Job Control",
    category="unix",
    difficulty="advanced",
    order=13,
    short_description="Background processes, job management, and persistent sessions",
    commands=["&", "jobs", "fg", "bg", "nohup", "screen", "tmux"],
    try_it_examples=[
        TryItExample(
            title="Run in background",
            command="sleep 10 & echo 'Process started in background' && jobs",
            description="Start a process in background with &"
        ),
        TryItExample(
            title="List background jobs",
            command="sleep 100 & sleep 200 & jobs",
            description="Show all background jobs for this shell"
        ),
        TryItExample(
            title="nohup for persistence",
            command="nohup echo 'This persists' > /tmp/nohup_test.txt 2>&1 & cat /tmp/nohup_test.txt",
            description="Run command that survives terminal close"
        ),
        TryItExample(
            title="Check screen availability",
            command="which screen || echo 'screen not installed'",
            description="Check if screen is available"
        ),
        TryItExample(
            title="Check tmux availability",
            command="which tmux || echo 'tmux not installed'",
            description="Check if tmux is available"
        ),
        TryItExample(
            title="Disown a process",
            command="sleep 60 & disown && echo 'Process disowned (no longer a job)'",
            description="Remove job from shell's job table"
        ),
    ],
    gotchas=[
        "Ctrl+Z suspends (pauses) a process; use bg to continue in background",
        "nohup prevents SIGHUP when terminal closes; output goes to nohup.out",
        "Jobs are per-shell; background processes survive, job table doesn't",
        "screen/tmux sessions persist across disconnections - great for SSH",
        "& puts process in background; && chains commands (run if previous succeeds)",
    ],
    related=["processes", "shell-scripting", "system-admin"],
)

register_concept(concept)
