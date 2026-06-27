from dataclasses import dataclass , field

@dataclass
class ExtraReasons:
    reason:str|None = None
    count:int|None = None
    proto:str|None = None
    ports:str|None = None

class ExtraPorts:
    state:str|None = None
    count:int|None = None
    extrareasons:ExtraReasons|None = None