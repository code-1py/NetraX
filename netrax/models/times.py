from dataclasses import dataclass


@dataclass
class Times:
    """Host round-trip timing values from Nmap XML.

    Attributes:
        srtt: Smoothed round-trip time value reported by Nmap.
        rttvar: Round-trip time variation reported by Nmap.
        to: Timeout estimate reported by Nmap.
    """

    srtt: int | None = None
    rttvar: int | None = None
    to: int | None = None
