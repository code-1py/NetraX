from xml.etree.ElementTree import Element
import xml.etree.ElementTree as ET
from ..models import State , Service
from ..exceptions import XmlParseError
from .common_functions import _to_int

def parse_status(state: Element | None,service:Service|None = None) ->State:
    if state is None:
        raise XmlParseError("<state> element not found")
    
    try:
        return State(state=state.get('state'),
                     reason=state.get('reason'),
                     reason_ttl=_to_int(state.get('reason_ttl')),
                     service=service)
    except Exception as exc:
        raise XmlParseError(state) from exc