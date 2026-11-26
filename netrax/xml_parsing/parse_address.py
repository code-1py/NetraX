from xml.etree.ElementTree import Element

from ..exceptions import XmlParseError
from ..models import Address


def parse_address(address: Element | None) -> Address:
    if address is None:
        raise XmlParseError("<address> element not found")

    try:
        return Address(
            addr=address.get("addr"),
            addrtype=address.get("addrtype"),
            vendor=address.get("vendor"),
        )
    except Exception as exc:
        raise XmlParseError(address) from exc
