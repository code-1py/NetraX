from .base import NetraxError

class XmlParseError(NetraxError):
    """Failed to parse Nmap XML output."""
    def __init__(self,xml_output:str):
        xml_output = xml_output
        super().__init__("Failed to parse Nmap XML output. The output may be malformed or not in XML format.\n"
                         f"XML Output:\n{xml_output}")
        
