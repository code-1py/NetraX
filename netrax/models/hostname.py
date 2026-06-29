from dataclasses import dataclass , field

@dataclass
class HostName:
    name:str|None = None
    type:str|None = None