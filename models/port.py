from dataclasses import dataclass , field
from .status import Status
from .service import Service

@dataclass
class Port:
    protocol:str|None = None
    portid:int|None = None
    state:Status|None = None
    services:Service|None = None