"""TLS Errors - Debug certificate and SSL/TLS handshake problems."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="tls-errors",
    title="TLS Errors",
    category="networking",
    difficulty="advanced",
    order=18,
    short_description="Debug certificate, handshake, and SSL/TLS errors",
    commands=["curl", "openssl"],
    try_it_examples=[
        TryItExample(
            title="View certificate info with curl",
            command="curl -vI https://example.com 2>&1 | grep -E '(subject:|issuer:|expire|SSL|TLS)'",
            description="See certificate details and TLS version"
        ),
        TryItExample(
            title="See expired certificate error",
            command="curl https://expired.badssl.com/ 2>&1 | head -5",
            description="What an expired certificate error looks like"
        ),
        TryItExample(
            title="See self-signed certificate error",
            command="curl https://self-signed.badssl.com/ 2>&1 | head -5",
            description="What a self-signed/untrusted cert error looks like"
        ),
        TryItExample(
            title="See wrong host certificate error",
            command="curl https://wrong.host.badssl.com/ 2>&1 | head -5",
            description="What a hostname mismatch error looks like"
        ),
        TryItExample(
            title="Bypass certificate check (testing only!)",
            command="curl -k https://self-signed.badssl.com/ 2>&1 | head -3; echo '\nWARNING: -k bypasses ALL cert checks - NEVER use in production!'",
            description="Skip verification with -k (insecure, testing only)"
        ),
        TryItExample(
            title="TLS error quick reference",
            command="echo 'TLS ERROR QUICK REFERENCE\n═══════════════════════════════════════════════════════\nError Message               | Cause\n═══════════════════════════════════════════════════════\ncertificate has expired     | Cert past expiration date\nself signed certificate     | Not signed by trusted CA\nunable to verify cert       | CA not in trust store\ncertificate verify failed   | General verify failure\nhostname mismatch           | Cert CN/SAN != URL hostname\nSSL handshake failed        | Protocol/cipher mismatch\ncertificate revoked         | Cert on revocation list\ncert not yet valid          | Cert start date in future'",
            description="Common TLS errors and their meanings"
        ),
        TryItExample(
            title="Deep certificate inspection",
            command="echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null | openssl x509 -noout -subject -issuer -dates",
            description="Extract cert subject, issuer, and validity dates"
        ),
        TryItExample(
            title="Check certificate chain",
            command="echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null | grep -E '(Certificate chain|s:|i:)' | head -10",
            description="View the full certificate chain"
        ),
        TryItExample(
            title="Debug TLS handshake",
            command="echo 'TLS DEBUGGING WORKFLOW:\n\n1. Check certificate validity:\n   curl -vI https://site.com 2>&1 | grep -i ssl\n\n2. Get detailed cert info:\n   openssl s_client -connect site.com:443 |\n     openssl x509 -noout -text | head -30\n\n3. Check supported TLS versions:\n   openssl s_client -connect site.com:443 -tls1_2\n   openssl s_client -connect site.com:443 -tls1_3\n\nCommon fixes:\n  - Expired: certbot renew\n  - Self-signed: Use real cert or install CA\n  - Hostname mismatch: Fix cert SAN\n  - Handshake failed: Update TLS config'",
            description="Step-by-step TLS troubleshooting"
        ),
    ],
    gotchas=[
        "curl -k bypasses ALL certificate verification - never use in production scripts",
        "SNI (Server Name Indication) requires -servername flag with openssl",
        "Certificate errors can be client-side (outdated CA bundle) or server-side",
        "Let's Encrypt certs expire every 90 days - set up auto-renewal!",
        "'Certificate verify failed' often means the CA bundle is outdated",
        "Hostname must match CN or SAN in the certificate - www. matters!",
    ],
    related=["http-web", "error-layers", "troubleshooting"],
)

register_concept(concept)
