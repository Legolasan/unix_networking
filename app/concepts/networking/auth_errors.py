"""Auth Errors - Debug SSH keys, permissions, and authentication problems."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="auth-errors",
    title="Auth Errors",
    category="networking",
    difficulty="advanced",
    order=19,
    short_description="Debug SSH, key permissions, and authentication errors",
    commands=["ssh", "ls", "chmod", "curl"],
    try_it_examples=[
        TryItExample(
            title="Check SSH key files exist",
            command="ls -la ~/.ssh/ 2>/dev/null || echo 'No .ssh directory - run: ssh-keygen'",
            description="List SSH keys and check if they exist"
        ),
        TryItExample(
            title="SSH permission requirements",
            command="echo 'SSH FILE PERMISSION REQUIREMENTS\n═══════════════════════════════════════════════════════\nFile/Directory        | Required   | Command\n═══════════════════════════════════════════════════════\n~/.ssh/               | 700        | chmod 700 ~/.ssh\n~/.ssh/id_rsa         | 600        | chmod 600 ~/.ssh/id_*\n~/.ssh/id_rsa.pub     | 644        | chmod 644 ~/.ssh/*.pub\n~/.ssh/authorized_keys| 600        | chmod 600 ~/.ssh/auth*\n~/.ssh/config         | 600        | chmod 600 ~/.ssh/config\n~/.ssh/known_hosts    | 644        | (auto-managed)\n\nWARNING: SSH will REFUSE to use keys with wrong permissions!\n\"Permissions 0644 for id_rsa are too open\" = chmod 600 id_rsa'",
            description="Required permissions for SSH files"
        ),
        TryItExample(
            title="Auth error quick reference",
            command="echo 'AUTH ERROR QUICK REFERENCE\n═══════════════════════════════════════════════════════\nPermission denied (publickey)\n  → Key not on server or wrong key\n  → ssh-copy-id user@host\n  → Check ~/.ssh/authorized_keys\n\nPermissions too open\n  → Key file permissions too loose\n  → chmod 600 ~/.ssh/id_rsa\n\nPermission denied (password)\n  → Wrong password or disabled\n  → Check PasswordAuthentication in sshd_config\n\nToo many auth failures\n  → Tried too many keys\n  → ssh -o IdentitiesOnly=yes -i key\n\nHost key verification failed\n  → Server key changed (or MITM!)\n  → ssh-keygen -R hostname (if expected)'",
            description="Common SSH auth errors and quick fixes"
        ),
        TryItExample(
            title="Debug SSH with verbose mode",
            command="echo 'SSH DEBUGGING WITH -v:\n\nssh -v user@host     # Basic debug\nssh -vv user@host    # More verbose\nssh -vvv user@host   # Maximum verbosity\n\nLook for these lines:\n  \"Offering public key\"  → Which key is tried\n  \"Server accepts key\"   → Key was accepted\n  \"Permission denied\"    → Method that failed\n\nCommon findings:\n  - No keys offered    → Wrong path/not found\n  - Key denied         → Not in authorized_keys\n  - Password denied    → Wrong or disabled'",
            description="Use -v, -vv, -vvv to debug SSH connections"
        ),
        TryItExample(
            title="HTTP auth errors (401 vs 403)",
            command="echo 'HTTP AUTH ERRORS: 401 vs 403\n═══════════════════════════════════════════════════════\n401 Unauthorized\n  \"Who are you?\" - Authentication required\n  Missing or invalid credentials\n  Fix: Provide valid auth token/credentials\n\n403 Forbidden\n  \"I know who you are, but NO\"\n  Authenticated but not allowed\n  Fix: Request access or check permissions\n\nExamples:\n  curl -I https://api.github.com/user\n  # Returns 401 - need auth token\n\n  curl -H \"Authorization: Bearer TOKEN\" /admin\n  # Returns 403 if user not admin'",
            description="Difference between HTTP 401 and 403"
        ),
        TryItExample(
            title="Fix SSH key permissions",
            command="echo 'QUICK FIX - Set all SSH permissions:\n\n# Fix directory\nchmod 700 ~/.ssh\n\n# Fix private keys\nchmod 600 ~/.ssh/id_*\nchmod 600 ~/.ssh/config 2>/dev/null\nchmod 600 ~/.ssh/authorized_keys 2>/dev/null\n\n# Fix public keys\nchmod 644 ~/.ssh/*.pub\n\n# Verify\nls -la ~/.ssh/'",
            description="Commands to fix all SSH permissions at once"
        ),
        TryItExample(
            title="SSH auth troubleshooting workflow",
            command="echo 'SSH AUTH TROUBLESHOOTING WORKFLOW:\n\n1. Can you reach the server at all?\n   ping host && nc -zv host 22\n\n2. Is SSH accepting connections?\n   ssh -v user@host 2>&1 | head -20\n\n3. Which key is being tried?\n   ssh -v user@host 2>&1 | grep -i offering\n\n4. Check permissions locally:\n   ls -la ~/.ssh/\n\n5. Check on server (if accessible):\n   cat ~/.ssh/authorized_keys\n\n6. Server-side logs (if root):\n   tail -f /var/log/auth.log\n   journalctl -u sshd -f'",
            description="Step-by-step SSH auth debugging"
        ),
    ],
    gotchas=[
        "SSH silently fails if key permissions are wrong - always check with ls -la ~/.ssh/",
        "The server's authorized_keys must contain your PUBLIC key (.pub), not private",
        "ssh-copy-id is the easiest way to add your key to a server",
        "Too many keys? Use ssh -o IdentitiesOnly=yes -i /path/to/key",
        "401 means 'authenticate yourself', 403 means 'authenticated but not authorized'",
        "Password auth may be disabled on servers - check PasswordAuthentication in sshd_config",
    ],
    related=["error-layers", "troubleshooting", "connectivity-testing"],
)

register_concept(concept)
