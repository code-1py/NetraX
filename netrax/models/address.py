from dataclasses import dataclass


@dataclass
class Address:
    addr: str | None = None
    addrtype: str | None = None
    vendor: str | None = None
