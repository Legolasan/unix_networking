"""Network Namespaces - Isolated network stacks and container networking."""

from app.concepts.base import BaseConcept, TryItExample
from app.concepts import register_concept

concept = BaseConcept(
    slug="network-namespaces",
    title="Network Namespaces",
    category="networking",
    difficulty="advanced",
    order=13,
    short_description="Isolated network stacks, veth pairs, and container networking",
    commands=["ip", "ip netns", "nsenter", "unshare"],
    try_it_examples=[
        TryItExample(
            title="List network namespaces",
            command="ip netns list 2>/dev/null || echo 'No namespaces or requires root'",
            description="Show all named network namespaces"
        ),
        TryItExample(
            title="Current namespace info",
            command="ip link show | head -10",
            description="View network interfaces in current namespace"
        ),
        TryItExample(
            title="Namespace concept",
            command="echo 'Network namespace:\n- Isolated network stack (interfaces, routes, iptables)\n- Each container gets its own namespace\n- veth pairs connect namespaces (like a virtual cable)\n- Docker/Kubernetes use namespaces heavily'",
            description="Understanding network namespaces"
        ),
        TryItExample(
            title="Creating namespaces (concept)",
            command="echo 'ip netns add myns                    # Create namespace\nip netns exec myns ip link show       # Run command in namespace\nip link add veth0 type veth peer name veth1  # Create veth pair'",
            description="Commands for namespace management"
        ),
        TryItExample(
            title="Docker networking",
            command="docker network ls 2>/dev/null || echo 'Docker not available'",
            description="Docker's network implementations use namespaces"
        ),
        TryItExample(
            title="View namespace of a process",
            command="ls -la /proc/self/ns/net",
            description="Each process has namespace references in /proc"
        ),
    ],
    gotchas=[
        "Network namespaces need root to create and manage",
        "Containers are isolated using namespaces (network, PID, mount, etc.)",
        "veth pairs always come in twos - one end in each namespace",
        "Bridge interfaces connect multiple veths (like a virtual switch)",
        "ip netns exec runs commands inside a specific namespace",
    ],
    related=["ip-addressing", "firewalls", "sockets"],
)

register_concept(concept)
