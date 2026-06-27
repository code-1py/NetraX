from dataclasses import dataclass , field
from .status import Status

@dataclass
class Port:
    protocol:str|None = None
    portid:int|None = None
    state:Status|None = None