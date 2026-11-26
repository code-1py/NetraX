from dataclasses import dataclass

from .service import Service
from .state import State


@dataclass
class Port:
    protocol: str | None = None
    portid: int | None = None
    state: State | None = None
    services: Service | None = None
