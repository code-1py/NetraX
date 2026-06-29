import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
from .base import NetraxError


class XmlParseError(NetraxError):
    """Failed to parse Nmap XML output."""

    def __init__(self, xml_output: str | Element | None):
        if isinstance(xml_output, Element):
            xml_output = ET.tostring(xml_output, encoding="unicode")

        super().__init__(
            "Failed to parse Nmap XML output. "
            "The output may be malformed or not in XML format.\n\n"
            f"XML Output:\n{xml_output}"
        )