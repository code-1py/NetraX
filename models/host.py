from dataclasses import dataclass , field
from .address import Address
from .hostname import HostName
from .port import Port
from .extra import ExtraPorts
from .times import Times

@dataclass
class Host:
    starttime:str|None = None
    endtime:str|None = None
    address:list[Address] = field(default_factory=list)
    extraports:ExtraPorts|None = None
    hostnames:list[HostName] = field(default_factory=list)
    ports:list[Port] = field(default_factory=list)
    times:Times|None = None