from dataclasses import dataclass , field

@dataclass
class Times:
    srtt:int|None = None
    rttvar:int|None = None
    to:int|None = None