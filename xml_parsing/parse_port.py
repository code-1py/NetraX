from .common_functions import _to_int
from ..exceptions import XmlParseError
from ..models import Port , State , Service
from xml.etree.ElementTree import Element
from .parse_service import parse_service
from .parse_state import parse_state


def parse_port(port: Element | None) -> Port:
    if port is None:
        raise XmlParseError("<port> element not found")

    try:
        state = port.find("state")
        service = port.find("service")

        parsed_service = parse_service(service) if service else None
        parsed_state = parse_state(state) if state else None
        

        return Port(
            protocol=port.get("protocol"),
            portid=_to_int(port.get("portid")),
            state=parsed_state,
            services=parsed_service
            )
            
    except Exception as exc:
        raise XmlParseError(port) from exc