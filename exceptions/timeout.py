from .base import NetraxError

class ScanTimeoutError(NetraxError):
    """
    An Nmap scan exceeded its allowed execution time.

    Attributes:
        stdout: Partial stdout captured before timeout.
        stderr: Partial stderr captured before timeout.
        timeout: Timeout value (seconds) that was exceeded.
    """

    def __init__(
        self,
        stdout: str | None = None,
        stderr: str | None = None,
        timeout: int | float | None = None,
    ):
        self.stdout = stdout
        self.stderr = stderr
        self.timeout = timeout

        super().__init__(
            f"Scan timed out after {timeout if timeout is not None else 'unknown'} seconds.\n"
            f"Increase the scan timeout argument or modify "
            f"netrax.config.timeouts.DEFAULT_SCAN_TIMEOUT.\n"
            f"stdout: {stdout or 'No output'}\n"
            f"stderr: {stderr or 'No error output'}"
        )

class ProcessTimeoutError(NetraxError):
    def __init__(self, reason: str | None = None):
        message = "Process timed out"

        if reason:
            message += f": {reason}"

        super().__init__(message)