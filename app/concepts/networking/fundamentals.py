"""Networking Fundamentals - OSI model, TCP/IP, and protocols overview."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="networking-fundamentals",
    title="Networking Fundamentals",
    category="networking",
    difficulty="beginner",
    order=1,
    short_description="OSI model, TCP/IP stack, and protocol basics",
    commands=["ip", "ifconfig", "hostname"],
    try_it_examples=[
        TryItExample(
            title="View network interfaces",
            command="ip addr show",
            description="List all network interfaces and their addresses"
        ),
        TryItExample(
            title="View routing table",
            command="ip route show",
            description="Display the kernel routing table"
        ),
        TryItExample(
            title="Network interface stats",
            command="ip -s link show",
            description="Show network statistics (packets, errors, drops)"
        ),
        TryItExample(
            title="View hostname",
            command="hostname -f",
            description="Display the fully qualified domain name"
        ),
        TryItExample(
            title="View hosts file",
            command="cat /etc/hosts",
            description="Local hostname to IP mappings"
        ),
    ],
    gotchas=[
        "ifconfig is deprecated - use 'ip' command instead",
        "lo (loopback) is the local-only interface (127.0.0.1)",
        "eth0/ens0 are typically wired interfaces",
        "wlan0/wlp0 are wireless interfaces",
        "Docker creates its own bridge network (docker0)",
    ],
    related=["ip-addressing", "ports-protocols"],
)

register_concept(concept)
