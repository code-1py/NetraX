from xml.etree.ElementTree import Element

from ..exceptions import XmlParseError
from ..models import NmapRun, ScanInfo, ScanReport
from .common_functions import _to_int
from .parse_host import parse_host


def parse_nmaprun(nmaprun: Element | None) -> NmapRun:
    if nmaprun is None:
        raise XmlParseError("<nmaprun> element not found")

    try:
        return NmapRun(
            scanner=nmaprun.get("scanner"),
            args=nmaprun.get("args"),
            start=nmaprun.get("start"),
            startstr=nmaprun.get("startstr"),
            version=nmaprun.get("version"),
            xmlversion=nmaprun.get("xmloutputversion"),
        )
    except Exception as exc:
        raise XmlParseError(nmaprun) from exc


def parse_scaninfo(scaninfo: Element | None) -> ScanInfo:
    if scaninfo is None:
        raise XmlParseError("<scaninfo> element not found")

    try:
        return ScanInfo(
            type=scaninfo.get("type"),
            protocol=scaninfo.get("protocol"),
            numservices=_to_int(scaninfo.get("numservices")),
            services=scaninfo.get("services"),
        )
    except Exception as exc:
        raise XmlParseError(scaninfo) from exc


def parse_scan_report(
    nmaprun: Element | None, raw_xml: str | None = None
) -> ScanReport:
    """Parse an Nmap ``<nmaprun>`` element into a :class:`ScanReport`.

    Args:
        nmaprun: Root ``<nmaprun>`` element from an Nmap XML document.
        raw_xml: Optional original XML string to retain on the report.

    Returns:
        A report containing parsed metadata and host results.

    Raises:
        XmlParseError: The root element is missing or the document cannot be
            converted into NetraX result models.
    """
    if nmaprun is None:
        raise XmlParseError("<nmaprun> element not found")

    try:
        verbose = nmaprun.find("verbose")
        debugging = nmaprun.find("debugging")

        return ScanReport(
            nmaprun=parse_nmaprun(nmaprun),
            scaninfo=(
                parse_scaninfo(nmaprun.find("scaninfo"))
                if nmaprun.find("scaninfo") is not None
                else None
            ),
            verbose_level=(
                _to_int(verbose.get("level")) if verbose is not None else None
            ),
            debugging_level=(
                _to_int(debugging.get("level")) if debugging is not None else None
            ),
            hosts=[parse_host(host) for host in nmaprun.findall("host")],
            raw_xml=raw_xml,
        )
    except Exception as exc:
        raise XmlParseError(nmaprun) from exc
