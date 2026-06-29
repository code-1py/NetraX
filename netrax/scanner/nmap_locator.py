import asyncio

from ..exceptions import (
    NmapNotFoundError,
    ProcessTimeoutError,
)
from ..config import timeouts


async def nmap_locator() -> bool:
    try:
        proc = await asyncio.create_subprocess_exec(
            "nmap",
            "--version",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
    except FileNotFoundError as exc:
        raise NmapNotFoundError() from exc

    try:
        async with asyncio.timeout(timeouts.NMAP_LOCATE_TIMEOUT):
            stdout, stderr = await proc.communicate()

    except TimeoutError as exc:
        if proc.returncode is None:
            proc.kill()
            await proc.wait()

        raise ProcessTimeoutError(
            "Failed to locate Nmap. "
            "Increase netrax.config.timeouts.NMAP_LOCATE_TIMEOUT if needed."
        ) from exc

    except Exception:
        if proc.returncode is None:
            proc.kill()
            await proc.wait()
        raise

    if proc.returncode != 0:
        raise NmapNotFoundError(stderr.decode())

    return True