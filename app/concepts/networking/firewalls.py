"""Firewalls - Control network traffic with iptables and ufw."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="firewalls",
    title="Firewalls",
    category="networking",
    difficulty="advanced",
    order=12,
    short_description="Control network traffic with iptables, nftables, and ufw",
    commands=["iptables", "nft", "ufw", "firewall-cmd"],
    try_it_examples=[
        TryItExample(
            title="View iptables rules",
            command="iptables -L -n 2>/dev/null | head -15 || echo 'iptables requires root'",
            description="List current firewall rules"
        ),
        TryItExample(
            title="Check ufw status",
            command="ufw status 2>/dev/null || echo 'ufw not available or requires root'",
            description="View ufw firewall status"
        ),
        TryItExample(
            title="iptables chains concept",
            command="echo 'iptables chains:\n  INPUT    - Packets destined for this host\n  OUTPUT   - Packets originating from this host\n  FORWARD  - Packets being routed through\n\nTargets: ACCEPT, DROP, REJECT, LOG'",
            description="Understanding iptables chains"
        ),
        TryItExample(
            title="Common iptables rules",
            command="echo 'iptables examples:\n  iptables -A INPUT -p tcp --dport 22 -j ACCEPT   # Allow SSH\n  iptables -A INPUT -p tcp --dport 80 -j ACCEPT   # Allow HTTP\n  iptables -A INPUT -j DROP                        # Drop all else'",
            description="Typical firewall rule patterns"
        ),
        TryItExample(
            title="ufw simple commands",
            command="echo 'ufw commands:\n  ufw enable              # Turn on firewall\n  ufw allow 22/tcp        # Allow SSH\n  ufw allow from 10.0.0.0/8  # Allow network\n  ufw deny 23             # Block telnet\n  ufw status numbered     # Show rules with numbers'",
            description="User-friendly firewall with ufw"
        ),
        TryItExample(
            title="Check for nftables",
            command="which nft && echo 'nftables available (modern replacement for iptables)' || echo 'nft not found'",
            description="nftables is the successor to iptables"
        ),
    ],
    gotchas=[
        "Rule order matters - first match wins in iptables",
        "Don't lock yourself out! Always allow SSH before enabling firewall",
        "iptables rules are NOT persistent by default - use iptables-save",
        "ufw is a frontend for iptables - simpler syntax, same engine",
        "DROP silently discards; REJECT sends error back to sender",
    ],
    related=["network-inspection", "ports-protocols", "sockets"],
)

register_concept(concept)
