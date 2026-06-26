from .base import NetraxError

class ScanTimeoutError(NetraxError):
    def __init__(self, stdout=None, stderr=None):
        self.stdout = stdout
        self.stderr = stderr
        super().__init__(f"Scan timed out\nstdout: {stdout if stdout else 'No output'}\nstderr: {stderr if stderr else 'No error output'}")