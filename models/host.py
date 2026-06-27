from dataclasses import dataclass , field
from .address import Address
from .hostnames import HostNames
from .port import Port
from .extra import ExtraPorts
from .times import Times

@dataclass
class Host:
    starttime:str|None = None
    endtime:str|None = None
    address:list[Address|None] = field(default_factory=list)
    extraports:ExtraPorts|None = None
    hostnames:HostNames|None = None
    ports:list[Port|None] = field(default_factory=list)
    times:Times|None = None