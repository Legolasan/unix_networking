"""DNS Tools - Query DNS with dig, nslookup, and host."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="dns-tools",
    title="DNS Tools",
    category="networking",
    difficulty="intermediate",
    order=7,
    short_description="Query DNS records with dig, nslookup, and host",
    commands=["dig", "nslookup", "host", "getent"],
    try_it_examples=[
        TryItExample(
            title="Basic DNS lookup",
            command="dig google.com +short",
            description="Get IP address for a domain (short output)"
        ),
        TryItExample(
            title="Full dig output",
            command="dig google.com | head -25",
            description="See complete DNS response with timing"
        ),
        TryItExample(
            title="Query specific record type",
            command="dig MX google.com +short",
            description="Look up mail server (MX) records"
        ),
        TryItExample(
            title="Query using specific DNS server",
            command="dig @8.8.8.8 example.com +short",
            description="Query Google's DNS server directly"
        ),
        TryItExample(
            title="Reverse DNS lookup",
            command="dig -x 8.8.8.8 +short",
            description="Get hostname from IP address"
        ),
        TryItExample(
            title="View all record types",
            command="dig google.com ANY +noall +answer 2>/dev/null | head -10 || dig google.com +short",
            description="Query all DNS record types"
        ),
    ],
    gotchas=[
        "dig is more powerful than nslookup (preferred for debugging)",
        "A = IPv4 address, AAAA = IPv6, MX = mail, NS = nameserver, CNAME = alias",
        "TTL (Time To Live) determines how long records are cached",
        "+short gives minimal output; +trace shows full resolution path",
        "/etc/resolv.conf contains your system's DNS server configuration",
    ],
    related=["dns-explained", "connectivity-testing", "troubleshooting"],
)

register_concept(concept)
