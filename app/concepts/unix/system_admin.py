"""System Administration - Services, systemd, and system management."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="system-admin",
    title="System Administration",
    category="unix",
    difficulty="advanced",
    order=14,
    short_description="Manage services with systemd, view logs with journalctl",
    commands=["systemctl", "journalctl", "service", "hostnamectl", "timedatectl"],
    try_it_examples=[
        TryItExample(
            title="List running services",
            command="systemctl list-units --type=service --state=running | head -15",
            description="Show all currently running services"
        ),
        TryItExample(
            title="Check service status",
            command="systemctl status cron 2>/dev/null || echo 'cron not available'",
            description="View status of cron service"
        ),
        TryItExample(
            title="View recent logs",
            command="journalctl -n 20 --no-pager 2>/dev/null || echo 'journalctl not available'",
            description="Show last 20 log entries"
        ),
        TryItExample(
            title="View boot logs",
            command="journalctl -b --no-pager 2>/dev/null | head -20 || echo 'journalctl not available'",
            description="Show logs from current boot"
        ),
        TryItExample(
            title="System information",
            command="hostnamectl 2>/dev/null || hostname",
            description="Display system hostname and OS info"
        ),
        TryItExample(
            title="Check date/time settings",
            command="timedatectl 2>/dev/null || date",
            description="View timezone and NTP status"
        ),
    ],
    gotchas=[
        "systemctl enable starts service on boot; start runs it now",
        "journalctl -f follows logs in real-time (like tail -f)",
        "Use journalctl -u servicename to filter logs by service",
        "Some containers don't run full systemd; use service command",
        "systemctl daemon-reload needed after editing unit files",
    ],
    related=["processes", "cron-scheduling", "package-management"],
)

register_concept(concept)
