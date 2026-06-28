from xml.etree.ElementTree import Element
from ..models import State , Service
from ..exceptions import XmlParseError
from .common_functions import _to_int

def parse_state(state: Element | None) ->State:
    if state is None:
        raise XmlParseError("<state> element not found")
    
    try:
        return State(state=state.get('state'),
                     reason=state.get('reason'),
                     reason_ttl=_to_int(state.get('reason_ttl')),
                    )
    except Exception as exc:
        raise XmlParseError(state) from exc