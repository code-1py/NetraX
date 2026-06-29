from .base import NetraxError

class InvalidTargetError(ValueError, NetraxError):
    """Invalid IP address, hostname or CIDR."""
    def __init__(self,target: str,stderr: str=None):
        self.target = target
        self.stderr = stderr
        super().__init__(f"Invalid target: {target}\nstderr: {stderr if stderr else 'No error output'}")