from .base import NetraxError

class InvalidScanProfileError(ValueError, NetraxError):
    """Unknown scan profile."""
    def __init__(self, profile: str, stderr: str=None):
        self.profile = profile
        self.stderr = stderr
        super().__init__(f"Invalid scan profile: {profile}\nstderr: {stderr if stderr else 'No error output'}")