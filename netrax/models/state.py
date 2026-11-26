from dataclasses import dataclass


@dataclass
class State:
    state: str | None = None
    reason: str | None = None
    reason_ttl: int | None = None
