"""IP Addressing - IPv4, IPv6, CIDR, and subnets."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="ip-addressing",
    title="IP Addressing",
    category="networking",
    difficulty="beginner",
    order=2,
    short_description="IPv4, IPv6 basics, CIDR notation, and subnets",
    commands=["ip addr", "hostname -I"],
    try_it_examples=[
        TryItExample(
            title="Show all IP addresses",
            command="hostname -I",
            description="Display all IP addresses for this host"
        ),
        TryItExample(
            title="IPv4 addresses only",
            command="ip -4 addr show",
            description="Show only IPv4 addresses"
        ),
        TryItExample(
            title="IPv6 addresses only",
            command="ip -6 addr show",
            description="Show only IPv6 addresses"
        ),
        TryItExample(
            title="Check your public IP",
            command="curl -s ifconfig.me",
            description="Get your public IP address (requires internet)"
        ),
        TryItExample(
            title="Examine subnet mask",
            command="ip addr show | grep inet",
            description="View IP addresses with CIDR notation (/24, etc.)"
        ),
    ],
    gotchas=[
        "192.168.x.x and 10.x.x.x are private IP ranges (not routable on internet)",
        "127.0.0.1 is always localhost (loopback)",
        "/24 means 256 addresses (common home network)",
        "/32 means exactly one address",
        "IPv6 addresses are much longer (128 bits vs 32 bits)",
    ],
    related=["networking-fundamentals", "ports-protocols", "dns-explained"],
)

register_concept(concept)
