"""Error Layers - Map network errors to OSI/TCP layers for faster debugging."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="error-layers",
    title="Error Layers",
    category="networking",
    difficulty="advanced",
    order=16,
    short_description="Map error messages to network layers for faster debugging",
    commands=["ip", "nc", "ss", "curl", "ping"],
    try_it_examples=[
        TryItExample(
            title="L1-2: Check physical/link layer",
            command="ip link show | grep -E '(^[0-9]|state)'",
            description="Interface DOWN or 'NO-CARRIER' = physical/link layer issue"
        ),
        TryItExample(
            title="L3: Check routing (network layer)",
            command="ip route get 8.8.8.8",
            description="'No route to host' = routing/L3 problem"
        ),
        TryItExample(
            title="L4: Check transport layer",
            command="nc -zv 127.0.0.1 22 2>&1 | head -3",
            description="'Connection refused' or 'timed out' = L4 issue"
        ),
        TryItExample(
            title="L5-7: Check application layer",
            command="curl -sI https://example.com | head -5",
            description="HTTP errors, TLS failures = application layer"
        ),
        TryItExample(
            title="Error-to-Layer cheat sheet",
            command="echo 'ERROR → LAYER QUICK REFERENCE\n═══════════════════════════════════════════\nLAYER 1-2 (Physical/Link)\n  • No carrier         → Cable unplugged/bad NIC\n  • Interface DOWN     → Interface disabled\n  • Link not ready     → Driver/hardware issue\n\nLAYER 3 (Network/IP)\n  • No route to host   → Routing table problem\n  • Network unreachable→ No path to network\n  • Host unreachable   → ARP failure or host down\n\nLAYER 4 (Transport)\n  • Connection refused → Port not listening (RST)\n  • Connection timeout → Firewall DROP or loss\n  • Connection reset   → Peer closed unexpectedly\n\nLAYER 5-7 (Application)\n  • TLS/SSL errors     → Certificate problem\n  • HTTP 4xx           → Client error\n  • HTTP 5xx           → Server error\n  • Permission denied  → Auth/access issue'",
            description="Quick reference: match error to network layer"
        ),
        TryItExample(
            title="Layer-by-layer debug workflow",
            command="echo 'DEBUGGING WORKFLOW - Work from bottom up:\n\n1. PHYSICAL (L1-2):\n   ip link show        # Is interface UP?\n   ethtool eth0        # Link detected?\n\n2. NETWORK (L3):\n   ip addr show        # Have IP address?\n   ip route            # Have default route?\n   ping gateway        # Can reach gateway?\n\n3. TRANSPORT (L4):\n   nc -zv host port    # Port open?\n   ss -tlnp            # What is listening?\n\n4. APPLICATION (L5-7):\n   curl -v URL         # HTTP/TLS working?\n   openssl s_client    # Certificate valid?'",
            description="Systematic debugging from physical to application"
        ),
    ],
    gotchas=[
        "Always debug bottom-up: physical -> network -> transport -> application",
        "If ping works but curl doesn't, the problem is L4+ (port/firewall/app)",
        "If IP works but hostname doesn't, it's DNS (technically L7, but check early)",
        "'Connection refused' means you REACHED the host - the port just isn't listening",
        "'Timed out' is ambiguous - could be firewall DROP, packet loss, or host down",
    ],
    related=["troubleshooting", "connection-errors", "networking-fundamentals"],
)

register_concept(concept)
