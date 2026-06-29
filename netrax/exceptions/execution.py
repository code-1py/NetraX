from .base import NetraxError

class NmapExecutionError(NetraxError):
    """Nmap returned a non-zero exit code."""
    def __init__(self,stderr:str,stdout:str,returncode:int):
        self.stderr = stderr
        self.stdout = stdout
        self.returncode = returncode

        super().__init__(f"Nmap returned a non-zero exit code: {returncode}\n"
                         f"stderr: {stderr if stderr else 'No error output'}\n"
                         f"stdout: {stdout if stdout else 'No output'}\n")