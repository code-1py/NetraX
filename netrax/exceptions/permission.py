from .base import NetraxError


class AdminRequiredError(PermissionError, NetraxError):
    """The current process lacks administrator or root privileges."""
