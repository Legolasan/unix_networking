"""DNS Explained - How DNS works, resolution process, record types."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="dns-explained",
    title="DNS Explained",
    category="networking",
    difficulty="beginner",
    order=4,
    short_description="How DNS works, resolution process, and record types",
    commands=["dig", "nslookup", "host", "cat /etc/resolv.conf"],
    try_it_examples=[
        TryItExample(
            title="Simple DNS lookup",
            command="host google.com",
            description="Quick DNS lookup for a domain"
        ),
        TryItExample(
            title="Detailed DNS query",
            command="dig google.com",
            description="Full DNS query with timing and server info"
        ),
        TryItExample(
            title="Query specific record type",
            command="dig google.com MX",
            description="Look up mail server (MX) records"
        ),
        TryItExample(
            title="Reverse DNS lookup",
            command="dig -x 8.8.8.8",
            description="Find hostname for an IP address"
        ),
        TryItExample(
            title="View DNS configuration",
            command="cat /etc/resolv.conf",
            description="See which DNS servers your system uses"
        ),
        TryItExample(
            title="Check local hosts file",
            command="cat /etc/hosts",
            description="Local overrides (checked before DNS)"
        ),
    ],
    gotchas=[
        "/etc/hosts is checked BEFORE DNS queries",
        "DNS uses port 53 (both UDP and TCP)",
        "A records = IPv4, AAAA records = IPv6",
        "MX records = mail servers, CNAME = aliases",
        "TTL (Time To Live) controls how long results are cached",
    ],
    related=["ip-addressing", "ports-protocols"],
)

register_concept(concept)
