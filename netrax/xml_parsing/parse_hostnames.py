from .common_functions import _to_int
from ..exceptions import XmlParseError
from ..models import HostName
from xml.etree.ElementTree import Element

def parse_hostnames(hostnames: Element | None) -> list[HostName]:
    if hostnames is None:
        raise XmlParseError("<hostnames> element not found")

    try:
        return [HostName(name=hostname.get('name'),
                         type=hostname.get('type'))
                         for hostname in hostnames.findall('hostname')
                        ]
    
    except Exception as exc:
        raise XmlParseError(hostnames) from exc