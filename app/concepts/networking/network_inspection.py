"""Network Inspection - View connections and ports with ss, netstat, and lsof."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="network-inspection",
    title="Network Inspection",
    category="networking",
    difficulty="intermediate",
    order=8,
    short_description="View network connections and ports with ss, netstat, and lsof",
    commands=["ss", "netstat", "lsof"],
    try_it_examples=[
        TryItExample(
            title="Show all listening ports",
            command="ss -tuln",
            description="TCP and UDP listening ports with numeric addresses"
        ),
        TryItExample(
            title="Show established connections",
            command="ss -t state established | head -10",
            description="View active TCP connections"
        ),
        TryItExample(
            title="Show process using port",
            command="ss -tlnp 2>/dev/null | head -10 || ss -tln | head -10",
            description="Show which process owns each socket (-p needs root)"
        ),
        TryItExample(
            title="Connection summary",
            command="ss -s",
            description="Display socket statistics summary"
        ),
        TryItExample(
            title="Find process by port",
            command="lsof -i :22 2>/dev/null || echo 'lsof requires elevated permissions'",
            description="Show what's using port 22 (SSH)"
        ),
        TryItExample(
            title="All network connections",
            command="ss -tunap 2>/dev/null | head -15 || ss -tuna | head -15",
            description="All TCP/UDP sockets with process info"
        ),
    ],
    gotchas=[
        "ss is faster than netstat (preferred on modern systems)",
        "-t = TCP, -u = UDP, -l = listening, -n = numeric, -p = process",
        "lsof -i shows all network files; add :port to filter",
        "State LISTEN means waiting for connections; ESTABLISHED is active",
        "0.0.0.0:port means listening on all interfaces; 127.0.0.1 is localhost only",
    ],
    related=["ports-protocols", "sockets", "troubleshooting"],
)

register_concept(concept)
