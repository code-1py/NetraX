from .common_functions import _to_int
from ..exceptions import XmlParseError
from ..models import ExtraPorts , ExtraReasons
from xml.etree.ElementTree import Element

def parse_extra_reasons(extrareasons: Element | None) -> ExtraReasons:
    if extrareasons is None:
        raise XmlParseError("<extrareasons> element not found")

    try:
        return ExtraReasons(
            reason=extrareasons.get("reason"),
            count=_to_int(extrareasons.get("count")),
            proto=extrareasons.get("proto"),
            ports=extrareasons.get("ports"),
        )
    except Exception as exc:
        raise XmlParseError(extrareasons) from exc


def parse_extra_ports(extraports: Element | None) -> ExtraPorts:
    if extraports is None:
        raise XmlParseError("<extraports> element not found")

    try:
        extrareasons = extraports.find("extrareasons")
        return ExtraPorts(
            state=extraports.get("state"),
            count=_to_int(extraports.get("count")),
            extrareasons=(
                parse_extra_reasons(extrareasons)
                if extrareasons is not None
                else None
            ),
        )
    except Exception as exc:
        raise XmlParseError(extraports) from exc