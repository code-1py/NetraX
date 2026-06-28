from dataclasses import dataclass , field
from .status import State
from .service import Service

@dataclass
class Port:
    protocol:str|None = None
    portid:int|None = None
    state:State|None = None
    services:Service|None = None