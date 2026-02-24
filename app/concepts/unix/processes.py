"""Processes - Managing running processes with ps, top, and kill."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="processes",
    title="Processes",
    category="unix",
    difficulty="intermediate",
    order=9,
    short_description="View and manage running processes",
    commands=["ps", "top", "htop", "kill", "killall", "pgrep", "pkill"],
    try_it_examples=[
        TryItExample(
            title="List all processes",
            command="ps aux | head -15",
            description="Show all processes with details (BSD style)"
        ),
        TryItExample(
            title="Find specific process",
            command="ps aux | grep -v grep | grep bash",
            description="Find bash processes"
        ),
        TryItExample(
            title="Process tree",
            command="ps auxf | head -20",
            description="Show process hierarchy as a tree"
        ),
        TryItExample(
            title="Find process by name",
            command="pgrep -l bash",
            description="List PIDs and names of matching processes"
        ),
        TryItExample(
            title="Top processes by memory",
            command="ps aux --sort=-%mem | head -10",
            description="Show top 10 memory-consuming processes"
        ),
        TryItExample(
            title="Top processes by CPU",
            command="ps aux --sort=-%cpu | head -10",
            description="Show top 10 CPU-consuming processes"
        ),
    ],
    gotchas=[
        "kill sends SIGTERM by default (graceful); use kill -9 for SIGKILL (force)",
        "PID 1 is init/systemd - never kill it!",
        "ps aux (BSD style) vs ps -ef (System V style) - both work",
        "Zombie processes (Z state) are already dead, waiting for parent",
        "top refreshes live; press q to quit, k to kill a process",
    ],
    related=["job-control", "system-admin", "environment"],
)

register_concept(concept)
