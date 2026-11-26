from dataclasses import dataclass, field

from .address import Address
from .extra import ExtraPorts
from .hostname import HostName
from .port import Port
from .times import Times


@dataclass
class Host:
    """One host entry in an Nmap report.

    Attributes:
        starttime: Host scan start time as reported in Nmap XML.
        endtime: Host scan end time as reported in Nmap XML.
        address: Addresses associated with the host.
        extraports: Summary of ports without individual port entries.
        hostnames: Host names reported for the host.
        ports: Individual port results.
        times: Nmap round-trip timing statistics, when present.
    """

    starttime: str | None = None
    endtime: str | None = None
    address: list[Address] = field(default_factory=list)
    extraports: ExtraPorts | None = None
    hostnames: list[HostName] = field(default_factory=list)
    ports: list[Port] = field(default_factory=list)
    times: Times | None = None
