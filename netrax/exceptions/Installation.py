from .base import NetraxError

class NmapNotFoundError(FileNotFoundError, NetraxError):
    """Raised when the nmap executable is not found in the system PATH."""
    pass