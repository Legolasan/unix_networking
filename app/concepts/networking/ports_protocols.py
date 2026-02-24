"""Ports & Protocols - Well-known ports, TCP vs UDP."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="ports-protocols",
    title="Ports & Protocols",
    category="networking",
    difficulty="beginner",
    order=3,
    short_description="Well-known ports, TCP vs UDP differences",
    commands=["ss", "netstat", "lsof"],
    try_it_examples=[
        TryItExample(
            title="View listening ports",
            command="ss -tuln",
            description="Show all TCP and UDP listening ports"
        ),
        TryItExample(
            title="View services file",
            command="head -30 /etc/services",
            description="Standard port to service name mappings"
        ),
        TryItExample(
            title="Check specific port",
            command="ss -tuln | grep ':22'",
            description="Check if SSH port (22) is listening"
        ),
        TryItExample(
            title="TCP connections",
            command="ss -t",
            description="Show established TCP connections"
        ),
        TryItExample(
            title="UDP sockets",
            command="ss -u",
            description="Show UDP sockets"
        ),
    ],
    gotchas=[
        "Ports 0-1023 are privileged (need root to bind)",
        "Port 80=HTTP, 443=HTTPS, 22=SSH, 53=DNS, 25=SMTP",
        "TCP is reliable (web, SSH), UDP is fast (DNS, video)",
        "ss is the modern replacement for netstat",
        "0.0.0.0 means listening on all interfaces",
    ],
    related=["ip-addressing", "dns-explained", "http-web"],
)

register_concept(concept)
