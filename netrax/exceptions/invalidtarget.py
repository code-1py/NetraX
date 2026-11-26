from .base import NetraxError


class InvalidTargetError(ValueError, NetraxError):
    """A scan target is invalid or could not be accepted.

    Attributes:
        target: Target value that was rejected.
        stderr: Optional diagnostic text associated with the invalid target.
    """

    def __init__(self, target: str, stderr: str | None = None):
        self.target = target
        self.stderr = stderr
        super().__init__(
            f"Invalid target: {target}\nstderr: {stderr if stderr else 'No error output'}"
        )
