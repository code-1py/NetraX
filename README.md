# netrax

**Async Python wrapper for Nmap** — run network scans, parse results, and integrate with your tools using clean async/await syntax.

[![PyPI version](https://img.shields.io/pypi/v/netrax.svg)](https://pypi.org/project/netrax/)
[![Python](https://img.shields.io/pypi/pyversions/netrax.svg)](https://pypi.org/project/netrax/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> **Note:** netrax requires [Nmap](https://nmap.org) to be installed on your system.
> Nmap is a separate open-source tool distributed under the
> [Nmap Public Source License](https://svn.nmap.org/nmap/LICENSE). netrax does not
> bundle or redistribute Nmap — it invokes it as an external process.

---

## Features

- **Fully async** — built on `asyncio`, no blocking calls
- **7 built-in scan types** — service, SYN, UDP, OS, aggressive, ping, and fully custom
- **Typed dataclass models** — structured access to every field in the Nmap XML output
- **Rich exception hierarchy** — granular error handling for timeouts, bad targets, missing Nmap, and more
- **Configurable timeouts** — global defaults or per-scan overrides
- **Admin privilege check** — fails fast with a clear error if root/administrator access is missing
- **JSON and dict export** — `report.to_dict()` and `report.to_json()` built in
- **Zero dependencies** — uses only the Python standard library

---

## Requirements

- Python 3.11+
- [Nmap](https://nmap.org/download.html) installed and available in `PATH`
- Administrator / root privileges (required by Nmap for most scan types)

---

## Installation

```bash
pip install netrax
```

Then make sure Nmap is installed on your system:

| OS | Command |
|---|---|
| Ubuntu / Debian | `sudo apt install nmap` |
| Fedora / RHEL | `sudo dnf install nmap` |
| macOS | `brew install nmap` |
| Windows | Download from [nmap.org](https://nmap.org/download.html) |

---

## Quick Start

```python
import asyncio
import netrax

async def main():
    scanner = netrax.Scanner()

    # Service and version detection
    report = await scanner.service_scan("192.168.1.1")

    for host in report.hosts:
        for addr in host.address:
            print(f"Host: {addr.addr}")
        for port in host.ports:
            print(port.portid, port.state.state, port.services.name)

asyncio.run(main())
```

---

## Scan Types

All scan methods return a `ScanReport` object.

| Method | Nmap Flag | Description |
|---|---|---|
| `service_scan(target)` | `-sV` | Service and version detection |
| `syn_scan(target)` | `-sS` | TCP SYN scan (fast, stealthy) |
| `udp_scan(target)` | `-sU` | UDP port scan |
| `os_scan(target)` | `-O` | Operating system detection |
| `aggressive_scan(target)` | `-A` | OS + version + scripts + traceroute |
| `ping_scan(target)` | `-sn` | Host discovery only (no port scan) |
| `scan(target, *arguments)` | custom | Pass any Nmap flags directly |

### Custom scan example

```python
report = await scanner.scan(
    "10.0.0.0/24",
    "-sV",
    "-O",
    "-T4",
    "--open",
)
```

---

## Timeouts

Every scan method accepts an optional `timeout` parameter (seconds). If omitted, the global default is used.

```python
# Per-scan timeout
report = await scanner.aggressive_scan("192.168.1.1", timeout=300)

# Change the global default
from netrax.config import timeouts
timeouts.DEFAULT_SCAN_TIMEOUT = 120
```

> **Note:** Slow timing templates (`-T0`, `-T1`, `-T2`) will trigger an automatic warning
> suggesting you increase the timeout.

---

## Working with Results

`ScanReport` is a fully typed dataclass. You can access every field directly, or export to dict/JSON.

```python
report = await scanner.service_scan("192.168.1.1")

# Access structured data
for host in report.hosts:
    for addr in host.address:
        print(f"IP: {addr.addr}  Type: {addr.addrtype}")

    for port in host.ports:
        svc = port.services
        print(f"Port {port.portid}/{port.protocol} — {port.state.state}")
        if svc:
            print(f"  Service: {svc.name} {svc.product} {svc.version}")

# Export
data = report.to_dict()
json_str = report.to_json(indent=4)
raw_xml = report.raw_xml
```

### Data model overview

```
ScanReport
├── nmaprun         (NmapRun)       — scanner metadata, args, version
├── scaninfo        (ScanInfo)      — scan type, protocol, service count
├── verbose_level   (int)
├── debugging_level (int)
├── raw_xml         (str)           — raw Nmap XML output
└── hosts           (list[Host])
    ├── starttime / endtime
    ├── address     (list[Address]) — IP and MAC addresses
    ├── hostnames   (list[HostName])
    ├── extraports  (ExtraPorts)
    ├── times       (Times)         — RTT statistics
    └── ports       (list[Port])
        ├── portid / protocol
        ├── state   (State)         — open/closed/filtered + reason
        └── services (Service)     — name, product, version, tunnel
```

---

## Exception Handling

```python
from netrax.exceptions import (
    AdminRequiredError,
    NmapNotFoundError,
    NmapExecutionError,
    ScanTimeoutError,
    InvalidTargetError,
    XmlParseError,
)

try:
    report = await scanner.service_scan("192.168.1.1")
except AdminRequiredError:
    print("Run as root / administrator.")
except NmapNotFoundError:
    print("Nmap is not installed or not in PATH.")
except ScanTimeoutError as e:
    print(f"Scan timed out after {e.timeout}s.")
except NmapExecutionError as e:
    print(f"Nmap error (exit {e.returncode}): {e.stderr}")
except XmlParseError:
    print("Could not parse Nmap XML output.")
```

### Exception hierarchy

```
NetraxError (base)
├── AdminRequiredError
├── NmapNotFoundError
├── NmapExecutionError
├── ScanTimeoutError
├── ProcessTimeoutError
├── InvalidTargetError
├── InvalidScanProfileError
├── XmlParseError
├── AIProviderError
└── ReportGenerationError
```

---

## API Reference

### `Scanner`

```python
scanner = Scanner()
```

Instantiating `Scanner` checks for root/administrator privileges immediately.
All scan methods are coroutines and must be awaited.

#### `scan(target, *arguments, timeout=None) → ScanReport`
Run Nmap with arbitrary arguments.

#### `service_scan(target, timeout=None) → ScanReport`
Service and version detection (`-sV`).

#### `syn_scan(target, timeout=None) → ScanReport`
TCP SYN scan (`-sS`).

#### `udp_scan(target, timeout=None) → ScanReport`
UDP scan (`-sU`).

#### `os_scan(target, timeout=None) → ScanReport`
OS detection (`-O`).

#### `aggressive_scan(target, timeout=None) → ScanReport`
Aggressive scan (`-A`): OS + version + scripts + traceroute.

#### `ping_scan(target, timeout=None) → ScanReport`
Host discovery only (`-sn`).

---

### `ScanReport`

| Method | Returns | Description |
|---|---|---|
| `to_dict()` | `dict` | Full report as a Python dictionary |
| `to_json(indent=None)` | `str` | Full report as a JSON string |

---

## Configuration

```python
from netrax.config import timeouts

timeouts.DEFAULT_SCAN_TIMEOUT = 120   # seconds (default: 60)
timeouts.NMAP_LOCATE_TIMEOUT  = 5     # seconds (default: 3)
```

---

## Legal

netrax is released under the [MIT License](LICENSE).

This project invokes [Nmap](https://nmap.org) as an external subprocess.
Nmap is not bundled with netrax and is distributed under its own
[Nmap Public Source License](https://svn.nmap.org/nmap/LICENSE).
Users are responsible for complying with Nmap's license and all applicable
laws when performing network scans. Only scan networks and systems you own
or have explicit permission to scan.