from .base import NetraxError


class InvalidScanProfileError(ValueError, NetraxError):
    """A scan profile name is not recognized.

    Attributes:
        profile: Profile name that was rejected.
        stderr: Optional diagnostic text associated with the invalid profile.
    """

    def __init__(self, profile: str, stderr: str | None = None):
        self.profile = profile
        self.stderr = stderr
        super().__init__(
            f"Invalid scan profile: {profile}\nstderr: {stderr if stderr else 'No error output'}"
        )
