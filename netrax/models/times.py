from dataclasses import dataclass


@dataclass
class Times:
    srtt: int | None = None
    rttvar: int | None = None
    to: int | None = None
