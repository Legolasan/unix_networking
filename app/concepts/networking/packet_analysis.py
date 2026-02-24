"""Packet Analysis - Capture and analyze network traffic with tcpdump."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="packet-analysis",
    title="Packet Analysis",
    category="networking",
    difficulty="advanced",
    order=10,
    short_description="Capture and analyze network packets with tcpdump",
    commands=["tcpdump", "tshark"],
    try_it_examples=[
        TryItExample(
            title="Check tcpdump availability",
            command="which tcpdump && echo 'tcpdump is installed' || echo 'tcpdump not found (needs install)'",
            description="Verify tcpdump is available"
        ),
        TryItExample(
            title="List network interfaces",
            command="tcpdump -D 2>/dev/null || ip link show | grep -E '^[0-9]'",
            description="Show available interfaces for capture"
        ),
        TryItExample(
            title="tcpdump syntax examples",
            command="echo 'tcpdump -i eth0              # Capture on eth0\ntcpdump -i any port 80       # HTTP traffic\ntcpdump -i any host 8.8.8.8  # Traffic to/from Google DNS\ntcpdump -c 10 -i any         # Capture 10 packets'",
            description="Common tcpdump command patterns"
        ),
        TryItExample(
            title="Filter expressions",
            command="echo 'tcpdump filters:\n  port 443        # HTTPS\n  host 10.0.0.1   # Specific IP\n  net 192.168.0.0/24  # Subnet\n  tcp/udp/icmp    # Protocol\n  src/dst port 22 # Direction'",
            description="BPF filter syntax reference"
        ),
        TryItExample(
            title="Save to pcap file",
            command="echo 'tcpdump -i any -w capture.pcap   # Write to file\ntcpdump -r capture.pcap          # Read from file'",
            description="Capture to file for later analysis"
        ),
        TryItExample(
            title="Verbose output options",
            command="echo 'tcpdump flags:\n  -v    # Verbose\n  -vv   # More verbose\n  -X    # Show packet contents in hex/ASCII\n  -n    # Numeric (no DNS lookup)\n  -c N  # Capture N packets'",
            description="Output verbosity flags"
        ),
    ],
    gotchas=[
        "tcpdump requires root/sudo to capture packets",
        "Use -n to avoid DNS lookups (faster, shows raw IPs)",
        "Ctrl+C stops capture; -c N limits packet count",
        ".pcap files can be opened in Wireshark for GUI analysis",
        "Capturing on busy interfaces generates huge amounts of data - use filters!",
    ],
    related=["wireshark", "network-inspection", "troubleshooting"],
)

register_concept(concept)
