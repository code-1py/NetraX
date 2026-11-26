from dataclasses import dataclass


@dataclass
class ExtraReasons:
    """Reason summary for ports grouped into an ``extraports`` result.

    Attributes:
        reason: Nmap state reason, such as ``no-response``.
        count: Number of ports with this reason.
        proto: Protocol associated with these ports, when provided.
        ports: Port identifiers or ranges as reported by Nmap.
    """

    reason: str | None = None
    count: int | None = None
    proto: str | None = None
    ports: str | None = None


@dataclass
class ExtraPorts:
    """Summary of ports whose individual results were omitted by Nmap.

    Attributes:
        state: Shared port state, such as ``closed`` or ``filtered``.
        count: Number of summarized ports.
        extrareasons: Optional breakdown of the reasons for that state.
    """

    state: str | None = None
    count: int | None = None
    extrareasons: ExtraReasons | None = None
