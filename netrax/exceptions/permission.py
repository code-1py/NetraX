from .base import NetraxError

class AdminRequiredError(PermissionError,NetraxError):
    """Raised when administrator/root privileges are required."""
    pass