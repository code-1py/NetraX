import json
from dataclasses import asdict, dataclass, field

from .host import Host


@dataclass
class NmapRun:
    """Top-level Nmap scan metadata.

    Attributes:
        scanner: Scanner program name.
        args: Command line recorded in the XML.
        start: Scan start time value recorded by Nmap.
        startstr: Human-readable scan start time.
        version: Nmap version string.
        xmlversion: Nmap XML format version.
    """

    scanner: str | None = None
    args: str | None = None
    start: str | None = None
    startstr: str | None = None
    version: str | None = None
    xmlversion: str | None = None


@dataclass
class ScanInfo:
    """Summary of the scan type and services covered.

    Attributes:
        type: Scan type reported by Nmap.
        protocol: Protocol scanned, when specified.
        numservices: Number of services or ports included in the scan.
        services: Service or port selection recorded by Nmap.
    """

    type: str | None = None
    protocol: str | None = None
    numservices: int | None = None
    services: str | None = None


@dataclass
class ScanReport:
    """
    Parsed Nmap scan report.

    Attributes:
        nmaprun: Top-level scanner metadata.
        scaninfo: Summary of the scan type and service selection.
        verbose_level: Nmap verbosity level, if included.
        debugging_level: Nmap debugging level, if included.
        hosts: Parsed host results.
        raw_xml: Original XML text captured from Nmap.

    Notes
    -----
    ScanReport instances can be converted to standard Python
    dictionaries and JSON.

    Examples
    --------
    .. code-block:: python

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

        .. code-block:: python

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

    nmaprun: NmapRun | None = None
    scaninfo: ScanInfo | None = None
    verbose_level: int | None = None
    debugging_level: int | None = None
    hosts: list[Host | None] = field(default_factory=list)
    raw_xml: str | None = None
