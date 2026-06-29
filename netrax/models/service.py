from dataclasses import dataclass , field

@dataclass
class Service:
    name:str|None = None
    product:str|None = None
    servicefp:str|None = None
    version:str|None = None
    method:str|None = None
    tunnel:str|None = None
    conf:int|None = None
