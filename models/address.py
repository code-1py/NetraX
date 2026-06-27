from dataclasses import dataclass , field

@dataclass
class Address:
    addr:str|None = None
    addrtype:str|None = None
    vendor:str|None = None