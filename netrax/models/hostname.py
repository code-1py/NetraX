from dataclasses import dataclass


@dataclass
class HostName:
    name: str | None = None
    type: str | None = None
