"""HTTP & Web - Understanding HTTP methods, headers, status codes, and TLS."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="http-web",
    title="HTTP & Web",
    category="networking",
    difficulty="intermediate",
    order=5,
    short_description="HTTP methods, headers, status codes, and TLS/HTTPS",
    commands=["curl", "http", "wget"],
    try_it_examples=[
        TryItExample(
            title="Simple GET request",
            command="curl -s http://httpbin.org/get | head -20",
            description="Make a basic HTTP GET request"
        ),
        TryItExample(
            title="View response headers",
            command="curl -I http://httpbin.org/get 2>/dev/null | head -15",
            description="Show only HTTP response headers with -I"
        ),
        TryItExample(
            title="POST request with data",
            command="curl -s -X POST http://httpbin.org/post -d 'name=test&value=123' | head -20",
            description="Send form data with POST"
        ),
        TryItExample(
            title="Custom headers",
            command="curl -s -H 'X-Custom: myvalue' http://httpbin.org/headers | head -15",
            description="Add custom request headers"
        ),
        TryItExample(
            title="Follow redirects",
            command="curl -sL -o /dev/null -w '%{http_code} -> %{redirect_url}' http://httpbin.org/redirect/1",
            description="Follow redirects with -L, show codes"
        ),
        TryItExample(
            title="View TLS certificate info",
            command="curl -vI https://example.com 2>&1 | grep -E '(subject:|issuer:|expire)'",
            description="Inspect HTTPS certificate details"
        ),
    ],
    gotchas=[
        "GET retrieves data; POST submits data; PUT replaces; DELETE removes",
        "Status 2xx = success, 3xx = redirect, 4xx = client error, 5xx = server error",
        "HTTPS = HTTP + TLS encryption (port 443 vs 80)",
        "curl -v shows verbose output including headers and TLS handshake",
        "Host header is required for virtual hosting (multiple sites on one IP)",
    ],
    related=["dns-explained", "ports-protocols", "data-transfer"],
)

register_concept(concept)
