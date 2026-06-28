from xml.etree.ElementTree import Element
from ..models import Times
from ..exceptions import XmlParseError
from .common_functions import _to_int


def parse_times(times: Element | None) -> Times:
    if times is None:
        raise XmlParseError("<times> element not found")

    try:
        return Times(
            srtt=_to_int(times.get("srtt")),
            rttvar=_to_int(times.get("rttvar")),
            to=_to_int(times.get("to")),
        )
    except Exception as exc:
        raise XmlParseError(times) from exc