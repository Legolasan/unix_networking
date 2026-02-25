"""Connection Errors - Deep dive into refused, timeout, and no route errors."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="connection-errors",
    title="Connection Errors",
    category="networking",
    difficulty="advanced",
    order=17,
    short_description="Understand 'refused' vs 'timeout' vs 'no route' errors",
    commands=["nc", "curl", "telnet", "ss", "ping"],
    try_it_examples=[
        TryItExample(
            title="Simulate: Connection refused",
            command="nc -zv 127.0.0.1 54321 2>&1; echo '\nYou reached the host, but port 54321 is not listening'",
            description="Refused = host received packet, sent RST back"
        ),
        TryItExample(
            title="Simulate: Connection timeout",
            command="timeout 3 nc -zv 10.255.255.1 80 2>&1 || echo '\nTimeout: packets sent but no response (firewall DROP or host unreachable)'",
            description="Timeout = no response (blocked or lost)"
        ),
        TryItExample(
            title="Error comparison table",
            command="echo 'CONNECTION ERROR COMPARISON\n═══════════════════════════════════════════════════════\nError              | Reached? | Layer | What Happened\n═══════════════════════════════════════════════════════\nConnection refused | YES      | L4    | Port not listening\n                   |          |       | (got TCP RST back)\n───────────────────────────────────────────────────────\nConnection timeout | MAYBE    | L3-4  | No response received\n                   |          |       | (firewall DROP, loss)\n───────────────────────────────────────────────────────\nNo route to host   | NO       | L3    | Routing problem\n                   |          |       | (no path to network)\n───────────────────────────────────────────────────────\nNetwork unreachable| NO       | L3    | No route to network\n                   |          |       | (check ip route)\n───────────────────────────────────────────────────────\nHost unreachable   | NO       | L2-3  | ARP failed or ICMP\n                   |          |       | unreachable received'",
            description="Side-by-side comparison of connection errors"
        ),
        TryItExample(
            title="Debug: Connection refused",
            command="echo 'CONNECTION REFUSED - Debug steps:\n\n1. Verify the service is running:\n   ss -tlnp | grep :PORT\n   systemctl status SERVICE\n\n2. Check its listening on the right address:\n   ss -tlnp  # 0.0.0.0=all, 127.0.0.1=local only\n\n3. Check service logs:\n   journalctl -u SERVICE -f\n\nCommon causes:\n  - Service not started or crashed\n  - Listening on localhost only\n  - Wrong port configured'",
            description="How to fix 'Connection refused'"
        ),
        TryItExample(
            title="Debug: Connection timeout",
            command="echo 'CONNECTION TIMEOUT - Debug steps:\n\n1. Is host reachable at all?\n   ping HOST\n\n2. Is a firewall blocking?\n   iptables -L -n | grep PORT\n\n3. Is something in the path blocking?\n   traceroute HOST\n\n4. Is the port actually open?\n   ss -tlnp | grep PORT  # on server\n\nCommon causes:\n  - Firewall DROP rule (not REJECT)\n  - Security group blocking (cloud)\n  - Host actually down\n  - Packet loss / congestion'",
            description="How to fix 'Connection timed out'"
        ),
        TryItExample(
            title="Debug: No route to host",
            command="echo 'NO ROUTE TO HOST - Debug steps:\n\n1. Check your routing table:\n   ip route\n\n2. Can you reach the gateway?\n   ping GATEWAY\n\n3. Is the destination reachable?\n   ip route get DESTINATION_IP\n\n4. Check if interface is up:\n   ip link show\n\nCommon causes:\n  - No default gateway configured\n  - VPN disconnected\n  - Interface down\n  - Incorrect subnet mask'",
            description="How to fix 'No route to host'"
        ),
        TryItExample(
            title="Quick diagnosis commands",
            command="echo 'Quick commands to identify the error:\n\n# Test TCP connection (shows exact error):\nnc -zv HOST PORT\n\n# Verbose curl (shows connection phase):\ncurl -v telnet://HOST:PORT\n\n# Check routing:\nip route get HOST_IP\n\n# Check what is listening locally:\nss -tlnp\n\n# Trace the path:\ntraceroute -n HOST'",
            description="Commands to quickly identify which error you have"
        ),
    ],
    gotchas=[
        "REFUSED is actually good news - it means the network path works!",
        "TIMEOUT is the hardest to debug - could be many things along the path",
        "Firewalls that DROP (not REJECT) cause timeouts, not 'refused' errors",
        "Cloud security groups usually DROP, making blocked connections look like timeouts",
        "Always test from the server itself first: ss -tlnp shows what's listening",
    ],
    related=["error-layers", "troubleshooting", "firewalls", "connectivity-testing"],
)

register_concept(concept)
