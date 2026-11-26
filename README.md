# NetraX

**NetraX is an async Python wrapper for Nmap.** It runs Nmap scans, parses Nmap's XML output into typed Python dataclasses, and provides structured scan reports for asyncio applications.

## Current release

- Version: **0.1.5**
- Python: **3.11 or newer**
- Runtime dependencies: **none** (standard library only)
- License: [MIT](LICENSE)

NetraX invokes Nmap as an external program. Install Nmap separately and make sure it is available on your `PATH`. Most scan types require administrator or root privileges.

## Install

```bash
python -m pip install netrax
```

Install Nmap using the instructions for your operating system at [nmap.org](https://nmap.org/download.html).

## Quick start

```python
import asyncio
from netrax import Scanner


async def main():
    scanner = Scanner()
    report = await scanner.service_scan("192.168.1.1")

    for host in report.hosts:
        for port in host.ports:
            service_name = port.services.name if port.services else "unknown"
            state = port.state.state if port.state else "unknown"
            print(f"{port.portid}/{port.protocol}: {state} ({service_name})")


asyncio.run(main())
```

Only scan systems and networks you own or have explicit permission to test. Nmap is not bundled with NetraX and remains subject to its own license.

## Documentation

Read the [NetraX documentation](https://netrax.readthedocs.io/en/latest/) for installation details, usage guides, and API reference organized by module. You can also start with the [quick start guide](https://netrax.readthedocs.io/en/latest/quickstart.html) or browse the [public API reference](https://netrax.readthedocs.io/en/latest/api/index.html).

## Project links

- [Source code](https://github.com/code-1py/NetraX)
- [Changelog](CHANGELOG.md)
- [Issue tracker](https://github.com/code-1py/NetraX/issues)
- [PyPI](https://pypi.org/project/netrax/)
