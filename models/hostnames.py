from dataclasses import dataclass , field

@dataclass
class HostNames:
    name:str|None = None
    type:str|None = None