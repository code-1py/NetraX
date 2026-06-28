from ..exceptions import XmlParseError
from ..models import Service
from xml.etree.ElementTree import Element

def parse_service(service: Element | None) -> Service:
    if service is None:
        raise XmlParseError("<service> element not found")

    try:
        return Service(
            name=service.get("name"),
            product=service.get("product"),
            servicefp=service.get("servicefp"),
            version=service.get("version"),
            method=service.get("method"),
            tunnel=service.get("tunnel"),
            conf=service.get("conf"),
        )
    except Exception as exc:
        raise XmlParseError(service) from exc