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
        async with asyncio.timeout(timeouts.NMAP_LOCATE_TIMEOUT): # timeout
            stdout, stderr = await proc.communicate()

    except TimeoutError as exc:
        proc.kill() # kill on timeout
        await proc.wait()

        raise ProcessTimeoutError(
            "Failed to locate Nmap. "
            "Increase netrax.config.timeouts.NMAP_LOCATE_TIMEOUT if needed."
        ) from exc
    except ProcessLookupError: # ignore if process already killed
        pass

    if proc.returncode != 0:
        raise NmapNotFoundError(stderr.decode())

    return True