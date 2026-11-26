import os

from ..exceptions import AdminRequiredError


def is_admin() -> bool:
    """Return whether the current process has administrator/root privileges.

    On Windows this uses the administrator membership check. On POSIX systems
    it checks whether the effective user ID is zero.
    """
    if os.name == "nt":
        import ctypes

        return ctypes.windll.shell32.IsUserAnAdmin() != 0

    return os.geteuid() == 0


def require_admin() -> None:
    """Raise :class:`AdminRequiredError` unless the process is privileged.

    Raises:
        AdminRequiredError: The current process is not running as an
            administrator or root user.
    """
    if not is_admin():
        raise AdminRequiredError(
            "netrax requires administrator/root privileges to perform scans."
        )
