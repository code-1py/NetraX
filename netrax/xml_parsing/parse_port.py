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
        state_elem = port.find("state")
        service_elem = port.find("service")

        return Port(
            protocol=port.get("protocol"),
            portid=_to_int(port.get("portid")),
            state=(
                parse_state(state_elem)
                if state_elem is not None
                else None
            ),
            services=(
                parse_service(service_elem)
                if service_elem is not None
                else None
            ),
        )

    except Exception as exc:
        raise XmlParseError(port) from exc