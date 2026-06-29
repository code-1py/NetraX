from .base import NetraxError

class ScanTimeoutError(NetraxError):
    """An Nmap scan exceeded its allowed execution time."""
    def __init__(self, stdout=None, stderr=None):
        self.stdout = stdout
        self.stderr = stderr
        super().__init__(f"Scan timed out\nstdout: {stdout if stdout else 'No output'}\nstderr: {stderr if stderr else 'No error output'}")

class ProcessTimeoutError(NetraxError):
    def __init__(self, reason: str | None = None):
        message = "Process timed out"

        if reason:
            message += f": {reason}"

        super().__init__(message)