from ..exceptions import XmlParseError
from xml.etree.ElementTree import Element
from ..models import Host
from .parse_address import parse_address
from .parse_extra import parse_extra_ports
from .parse_hostnames import parse_hostnames
from .parse_time import parse_times
from .parse_port import parse_port

def parse_host(host: Element | None) -> Host:
    if host is None:
        raise XmlParseError("<host> element not found")

    try:
        ports = host.find("ports")
        extraports = ports.find("extraports") if ports is not None else None
        hostnames = host.find("hostnames")

        return Host(
            starttime=host.get("starttime"),
            endtime=host.get("endtime"),
            address=[
                parse_address(address)
                for address in host.findall("address")
            ],
            extraports=(
                parse_extra_ports(extraports)
                if extraports is not None
                else None
            ),
            hostnames=(
                parse_hostnames(hostnames)
                if hostnames is not None
                else None
            ),
            ports=[
                parse_port(port)
                for port in ports.findall("port")
            ] if ports is not None else [],
            times=(
                parse_times(host.find("times"))
                if host.find("times") is not None
                else None
            ),
        )
    except Exception as exc:
        raise XmlParseError(host) from exc