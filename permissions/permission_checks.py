import os 
from ..exceptions import AdminRequiredError

def is_admin() -> bool:
    if os.name == "nt":
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    
    return os.geteuid() == 0

def require_admin() -> None:
    if not is_admin():
        raise AdminRequiredError("netrax requires administrator/root privileges to perform scans.")