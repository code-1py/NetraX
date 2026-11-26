from dataclasses import dataclass


@dataclass
class HostName:
    """A hostname associated with a scanned host.

    Attributes:
        name: Hostname text.
        type: Name source reported by Nmap, commonly ``PTR``.
    """

    name: str | None = None
    type: str | None = None
