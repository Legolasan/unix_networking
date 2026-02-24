"""Cron & Scheduling - Automate tasks with cron and at."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="cron-scheduling",
    title="Cron & Scheduling",
    category="unix",
    difficulty="advanced",
    order=15,
    short_description="Schedule recurring tasks with cron and one-time jobs with at",
    commands=["crontab", "at", "atq", "atrm"],
    try_it_examples=[
        TryItExample(
            title="View current crontab",
            command="crontab -l 2>/dev/null || echo 'No crontab for this user'",
            description="List your scheduled cron jobs"
        ),
        TryItExample(
            title="Cron syntax example",
            command="echo '# min hour day month weekday command\n# 30 2 * * * /path/to/script.sh\n# Runs at 2:30 AM every day'",
            description="Understand cron timing format"
        ),
        TryItExample(
            title="System cron directories",
            command="ls -la /etc/cron.* 2>/dev/null | head -10",
            description="View system cron directories"
        ),
        TryItExample(
            title="Check cron service",
            command="systemctl status cron 2>/dev/null || service cron status 2>/dev/null || echo 'cron status unavailable'",
            description="Verify cron daemon is running"
        ),
        TryItExample(
            title="At job syntax",
            command="echo 'at schedules one-time jobs: at 2:30pm tomorrow'",
            description="Schedule one-time execution with at"
        ),
        TryItExample(
            title="Common cron schedules",
            command="echo '@daily    = 0 0 * * *   (midnight)\n@hourly   = 0 * * * *\n@weekly   = 0 0 * * 0   (Sunday midnight)\n@monthly  = 0 0 1 * *   (1st of month)'",
            description="Special cron time shortcuts"
        ),
    ],
    gotchas=[
        "Cron format: minute hour day month weekday (5 fields)",
        "Cron jobs run with minimal PATH - use full paths to commands",
        "Cron output is emailed by default; redirect to avoid mail buildup",
        "Edit crontab with 'crontab -e', not by editing files directly",
        "Use @reboot to run a command once at system startup",
    ],
    related=["shell-scripting", "system-admin", "environment"],
)

register_concept(concept)
