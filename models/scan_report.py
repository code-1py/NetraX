from dataclasses import dataclass , field
from .host import Host

@dataclass
class NmapRun:
    scanner:str|None = None
    args:str|None = None
    start:str|None = None
    startstr:str|None = None
    version:str|None = None
    xmlversion:str|None = None

@dataclass
class ScanInfo:
    type:str|None = None
    protocol:str|None = None
    numservices:int|None = None
    services:str|None = None

@dataclass
class ScanReport:
    nmaprun:NmapRun|None = None
    scaninfo:ScanInfo|None = None
    verbose_level:int|None = None
    debugging_level:int|None = None
    hosts:list[Host|None] = field(default_factory=list)
    raw_xml:str|None = None