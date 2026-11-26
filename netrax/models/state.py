from dataclasses import dataclass


@dataclass
class State:
    """State and reason reported for a port.

    Attributes:
        state: Nmap state, such as ``open``, ``closed``, or ``filtered``.
        reason: Reason Nmap assigned to the state.
        reason_ttl: TTL value associated with the reason, when provided.
    """

    state: str | None = None
    reason: str | None = None
    reason_ttl: int | None = None
