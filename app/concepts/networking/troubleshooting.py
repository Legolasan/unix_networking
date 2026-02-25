"""Troubleshooting Workflow - Systematic network debugging methodology."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="troubleshooting",
    title="Troubleshooting Workflow",
    category="networking",
    difficulty="advanced",
    order=15,
    short_description="Systematic approach to debugging network issues",
    commands=["ping", "dig", "ss", "ip", "curl", "traceroute"],
    try_it_examples=[
        TryItExample(
            title="Step 1: Check local interface",
            command="ip addr show | grep -E '(^[0-9]|inet )' | head -10",
            description="Verify interface is up and has IP address"
        ),
        TryItExample(
            title="Step 2: Check default gateway",
            command="ip route | grep default",
            description="Verify default route exists"
        ),
        TryItExample(
            title="Step 3: Ping gateway",
            command="gateway=$(ip route | grep default | awk '{print $3}'); ping -c 2 $gateway 2>/dev/null || echo 'Gateway: '$gateway",
            description="Test connectivity to local gateway"
        ),
        TryItExample(
            title="Step 4: Test external connectivity",
            command="ping -c 2 8.8.8.8",
            description="Ping external IP (bypasses DNS)"
        ),
        TryItExample(
            title="Step 5: Test DNS resolution",
            command="dig google.com +short || nslookup google.com | tail -2",
            description="Verify DNS is working"
        ),
        TryItExample(
            title="Full connectivity check",
            command="echo '=== Interface ===' && ip addr show | grep 'inet ' | head -3 && echo '=== Gateway ===' && ip route | head -2 && echo '=== External ===' && ping -c 1 8.8.8.8 2>&1 | tail -1",
            description="Quick all-in-one connectivity test"
        ),
    ],
    gotchas=[
        "Work from inside out: localhost -> gateway -> internet -> DNS -> application",
        "If ping works but curl doesn't, check port/firewall/application layer",
        "If IP works but hostname doesn't, it's a DNS problem",
        "Use -n flags to avoid DNS lookups when debugging DNS issues",
        "Check /etc/resolv.conf for DNS server configuration",
    ],
    related=["connectivity-testing", "dns-tools", "network-inspection", "packet-analysis", "error-layers", "connection-errors", "tls-errors", "auth-errors"],
)

register_concept(concept)
