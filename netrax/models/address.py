from dataclasses import dataclass


@dataclass
class Address:
    """An address reported for a host.

    Attributes:
        addr: Address value, such as an IPv4, IPv6, or MAC address.
        addrtype: Address type reported by Nmap (for example, ``ipv4`` or ``mac``).
        vendor: Hardware vendor when Nmap identifies one for a MAC address.
    """

    addr: str | None = None
    addrtype: str | None = None
    vendor: str | None = None
