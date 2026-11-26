from dataclasses import dataclass


@dataclass
class Service:
    """Service identification details associated with a port.

    Attributes:
        name: Service name reported by Nmap.
        product: Detected software product.
        servicefp: Service fingerprint, when Nmap includes one.
        version: Detected product version.
        method: Detection method reported by Nmap.
        tunnel: Tunnel protocol, when identified.
        conf: Nmap's confidence value for the service match.
    """

    name: str | None = None
    product: str | None = None
    servicefp: str | None = None
    version: str | None = None
    method: str | None = None
    tunnel: str | None = None
    conf: int | None = None
