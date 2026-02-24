"""Sockets - Network socket types and netcat usage."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="sockets",
    title="Sockets",
    category="networking",
    difficulty="advanced",
    order=14,
    short_description="Understand socket types and use netcat for network testing",
    commands=["nc", "netcat", "socat"],
    try_it_examples=[
        TryItExample(
            title="Check netcat availability",
            command="which nc || which netcat || echo 'netcat not found'",
            description="Verify netcat is installed"
        ),
        TryItExample(
            title="Port scan with nc",
            command="nc -zv 8.8.8.8 53 2>&1 | head -3 || echo 'Connection test'",
            description="Test if port 53 (DNS) is open on Google"
        ),
        TryItExample(
            title="Socket types explained",
            command="echo 'Socket types:\n  STREAM (TCP) - Connection-oriented, reliable, ordered\n  DGRAM (UDP)  - Connectionless, best-effort, fast\n  RAW          - Direct access to IP layer\n\nTCP: web, SSH, email | UDP: DNS, video, gaming'",
            description="Understanding socket types"
        ),
        TryItExample(
            title="Listen on a port",
            command="echo 'nc -l -p 8080           # Listen on port 8080\nnc hostname 8080         # Connect to that port\n\nAnything typed on one side appears on the other!'",
            description="Creating a simple server with netcat"
        ),
        TryItExample(
            title="HTTP request with nc",
            command="echo -e 'GET / HTTP/1.1\\r\\nHost: example.com\\r\\n\\r\\n' | nc -q1 example.com 80 2>/dev/null | head -10",
            description="Manual HTTP request via netcat"
        ),
        TryItExample(
            title="Socket file example",
            command="ls -la /var/run/*.sock 2>/dev/null | head -5 || echo 'No socket files found (or different location)'",
            description="Unix domain sockets (local IPC)"
        ),
    ],
    gotchas=[
        "nc (netcat) is the 'Swiss Army knife' of networking",
        "TCP sockets guarantee delivery; UDP doesn't (but is faster)",
        "Unix sockets are for local IPC - no network overhead",
        "Use -u flag with nc for UDP instead of TCP",
        "socat is like netcat on steroids - more features, complex syntax",
    ],
    related=["ports-protocols", "network-inspection", "firewalls"],
)

register_concept(concept)
