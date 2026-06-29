from .common_functions import _to_int
from ..exceptions import XmlParseError
from ..models import Address
from xml.etree.ElementTree import Element

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