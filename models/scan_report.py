from dataclasses import dataclass , field
from .host import Host
from dataclasses import asdict
import json

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
    """
    Parsed Nmap scan report.

    Notes
    -----
    ScanReport instances can be converted to standard Python
    dictionaries and JSON.

    Examples
    --------
    report = await scanner.service_scan("127.0.0.1")

    # NetraX helper methods
    data = report.to_dict()
    json_data = report.to_json(indent=4)

    # Standard dataclasses API
    from dataclasses import asdict

    data = asdict(report)
    """

    def to_dict(self) -> dict:
        """
        Convert the scan report to a dictionary.

        This method is equivalent to:

            from dataclasses import asdict
            asdict(report)

        Returns:
            dict:
                Dictionary representation of the scan report.
        """
        return asdict(self)

    def to_json(self, indent: int | None = None) -> str:
        """
        Convert the scan report to a JSON string.
    
        Args:
            indent:
                Number of spaces used for indentation.
                Use None for compact JSON output.
    
        Returns:
            str:
                JSON representation of the scan report.
        """
        return json.dumps(
            self.to_dict(),
            indent=indent,
        )
    nmaprun:NmapRun|None = None
    scaninfo:ScanInfo|None = None
    verbose_level:int|None = None
    debugging_level:int|None = None
    hosts:list[Host|None] = field(default_factory=list)
    raw_xml:str|None = None