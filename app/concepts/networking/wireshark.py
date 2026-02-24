"""Wireshark Concepts - Understanding packet analysis with Wireshark."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="wireshark",
    title="Wireshark Concepts",
    category="networking",
    difficulty="advanced",
    order=11,
    short_description="Understand packet analysis concepts and Wireshark filters",
    commands=["tshark", "wireshark"],
    try_it_examples=[
        TryItExample(
            title="Check tshark availability",
            command="which tshark && echo 'tshark (CLI Wireshark) is installed' || echo 'tshark not found'",
            description="Verify Wireshark CLI tools are available"
        ),
        TryItExample(
            title="Display filter syntax",
            command="echo 'Wireshark display filters:\n  ip.addr == 10.0.0.1      # IP address\n  tcp.port == 443          # TCP port\n  http.request             # HTTP requests\n  dns                       # DNS traffic\n  tcp.flags.syn == 1       # SYN packets'",
            description="Common Wireshark display filters"
        ),
        TryItExample(
            title="Capture filter vs display filter",
            command="echo 'Capture filter (BPF): Applied during capture, limits what is saved\nDisplay filter: Applied after capture, filters what you see\n\nCapture: \"port 80\"  vs  Display: \"tcp.port == 80\"'",
            description="Understand the two filter types"
        ),
        TryItExample(
            title="Follow TCP stream concept",
            command="echo 'Follow TCP Stream:\n- Right-click packet -> Follow -> TCP Stream\n- Shows complete conversation between client/server\n- Great for seeing HTTP requests/responses\n- Can export as text or raw data'",
            description="Reconstructing conversations"
        ),
        TryItExample(
            title="Protocol hierarchy",
            command="echo 'Ethernet Frame\n  └─ IP Packet\n       └─ TCP Segment (or UDP Datagram)\n            └─ Application Data (HTTP, DNS, etc.)\n\nEach layer encapsulates the next'",
            description="Network protocol layers"
        ),
        TryItExample(
            title="Common analysis tasks",
            command="echo 'Analysis tips:\n- Statistics -> Conversations (see all connections)\n- Statistics -> Protocol Hierarchy (traffic breakdown)\n- Analyze -> Expert Information (find problems)\n- tcp.analysis.retransmission (find packet loss)'",
            description="Key Wireshark analysis features"
        ),
    ],
    gotchas=[
        "tshark is Wireshark for the command line - same engine",
        "Display filters use different syntax than capture filters (BPF)",
        "Large captures can be slow - filter early when possible",
        "Follow TCP Stream shows the conversation in readable format",
        "Look for retransmissions and out-of-order packets to diagnose issues",
    ],
    related=["packet-analysis", "http-web", "troubleshooting"],
)

register_concept(concept)
