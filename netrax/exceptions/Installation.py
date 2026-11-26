from .base import NetraxError


class NmapNotFoundError(FileNotFoundError, NetraxError):
    """Nmap could not be found on the system ``PATH``."""
