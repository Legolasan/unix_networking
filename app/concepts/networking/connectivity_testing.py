"""Connectivity Testing - Test network reachability with ping, traceroute, and mtr."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="connectivity-testing",
    title="Connectivity Testing",
    category="networking",
    difficulty="intermediate",
    order=6,
    short_description="Test network reachability with ping, traceroute, and mtr",
    commands=["ping", "traceroute", "tracepath", "mtr"],
    try_it_examples=[
        TryItExample(
            title="Ping a host",
            command="ping -c 4 8.8.8.8",
            description="Send 4 ICMP echo requests to Google DNS"
        ),
        TryItExample(
            title="Ping with timeout",
            command="ping -c 2 -W 2 1.1.1.1",
            description="Ping Cloudflare DNS with 2 second timeout"
        ),
        TryItExample(
            title="Traceroute to host",
            command="traceroute -m 10 8.8.8.8 2>/dev/null || tracepath -m 10 8.8.8.8 2>/dev/null",
            description="Show path packets take (max 10 hops)"
        ),
        TryItExample(
            title="Check DNS resolution + ping",
            command="ping -c 2 google.com",
            description="Test both DNS resolution and connectivity"
        ),
        TryItExample(
            title="Ping with packet size",
            command="ping -c 2 -s 1000 8.8.8.8",
            description="Send larger packets (test MTU)"
        ),
        TryItExample(
            title="Check for packet loss",
            command="ping -c 10 -i 0.2 8.8.8.8 | tail -3",
            description="Quick burst to check for packet loss"
        ),
    ],
    gotchas=[
        "Some hosts block ICMP (ping may fail but host is up)",
        "traceroute uses UDP by default; some firewalls block it",
        "* in traceroute means that hop didn't respond (firewall or timeout)",
        "High latency on first hop = local network issue",
        "mtr combines ping and traceroute into one live display",
    ],
    related=["ip-addressing", "dns-tools", "troubleshooting"],
)

register_concept(concept)
