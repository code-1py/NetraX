from dataclasses import dataclass , field
from .state import State

@dataclass
class Port:
    protocol:str|None = None
    portid:int|None = None
    state:State|None = None