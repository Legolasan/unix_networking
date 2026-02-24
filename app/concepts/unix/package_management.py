"""Package Management - Installing software with apt, yum, and dnf."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="package-management",
    title="Package Management",
    category="unix",
    difficulty="advanced",
    order=16,
    short_description="Install, update, and manage software packages",
    commands=["apt", "apt-get", "dpkg", "yum", "dnf", "rpm"],
    try_it_examples=[
        TryItExample(
            title="Update package list",
            command="apt update 2>&1 | head -10 || echo 'apt not available or requires sudo'",
            description="Refresh available package information (Debian/Ubuntu)"
        ),
        TryItExample(
            title="Search for packages",
            command="apt search htop 2>/dev/null | head -10 || echo 'apt search unavailable'",
            description="Find packages matching a term"
        ),
        TryItExample(
            title="Show package info",
            command="apt show curl 2>/dev/null | head -15 || dpkg -s curl 2>/dev/null | head -15",
            description="Display package details"
        ),
        TryItExample(
            title="List installed packages",
            command="dpkg -l | head -20",
            description="Show all installed packages (Debian/Ubuntu)"
        ),
        TryItExample(
            title="Check package manager",
            command="which apt && echo 'Debian/Ubuntu (apt)' || which dnf && echo 'Fedora/RHEL 8+ (dnf)' || which yum && echo 'RHEL/CentOS (yum)'",
            description="Detect which package manager is available"
        ),
        TryItExample(
            title="View package files",
            command="dpkg -L bash | head -15",
            description="List files installed by a package"
        ),
    ],
    gotchas=[
        "apt is user-friendly; apt-get is for scripts (more stable output)",
        "Always run apt update before apt install to get latest versions",
        "apt autoremove cleans up unused dependencies",
        "dpkg is low-level (no dependencies); apt handles dependencies",
        "RHEL/CentOS use yum/dnf; Debian/Ubuntu use apt - don't mix them!",
    ],
    related=["system-admin", "environment", "unix-basics"],
)

register_concept(concept)
