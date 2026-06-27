from xml.etree.ElementTree import Element
import xml.etree.ElementTree as ET

from ..models import Times
from ..exceptions import XmlParseError


def parse_times(times: Element | None) -> Times:
    if times is None:
        raise XmlParseError("<times> element not found")

    try:
        return Times(
            srtt=times.get("srtt"),
            rttvar=times.get("rttvar"),
            to=times.get("to"),
        )
    except Exception as exc:
        raise XmlParseError(times) from exc