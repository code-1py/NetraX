from dataclasses import dataclass

from .service import Service
from .state import State


@dataclass
class Port:
    """An individual TCP or UDP port result.

    Attributes:
        protocol: Transport protocol, usually ``tcp`` or ``udp``.
        portid: Numeric port number.
        state: Port state and Nmap's reason for it, when present.
        services: Detected service details, when Nmap identifies a service.
    """

    protocol: str | None = None
    portid: int | None = None
    state: State | None = None
    services: Service | None = None
