from __future__ import annotations
import asyncio
import warnings
from xml.etree import ElementTree
from ..config import timeouts
from ..exceptions import (
    NmapExecutionError,
    ScanTimeoutError,
)
from ..permissions import require_admin
from ..xml_parsing import parse_scan_report
from .nmap_locator import nmap_locator
from ..models import ScanReport

class Scanner:
    """
    Async Nmap scanner.

    Examples
    --------
    scanner = Scanner()

    report = await scanner.service_scan("192.168.1.1")

    report = await scanner.scan(
        "192.168.1.1",
        "-sV",
        "-T4"
    )
    """

    def __init__(self):
        require_admin()
        self._nmap_verified = False

    async def _verify_nmap(self) -> None:
        """
        Verify Nmap once per Scanner instance.
        """

        if not self._nmap_verified:
            await nmap_locator()
            self._nmap_verified = True

    @staticmethod
    def _warn_timeout(arguments: list[str], timeout: int) -> None:
        """
        Warn when slow timing templates may require a larger timeout.

        If you frequently use slow timing templates, consider increasing
        netrax.config.timeouts.DEFAULT_SCAN_TIMEOUT.
        """

        timing_templates = {
            "-T0": "Paranoid",
            "-T1": "Sneaky",
            "-T2": "Polite",
        }

        for arg in arguments:
            if arg in timing_templates:
                warnings.warn(
                    f"{arg} ({timing_templates[arg]}) detected. "
                    f"This timing template can significantly increase scan duration. "
                    f"If the scan times out, increase the timeout parameter or "
                    f"modify netrax.config.timeouts.DEFAULT_SCAN_TIMEOUT "
                    f"(currently {timeout} seconds).",
                    stacklevel=2,
                )

    async def _run_scan(
        self,
        cmd: list[str],
        timeout: int,
    ) -> ScanReport:
        """
        Internal scan executor.
        """

        await self._verify_nmap()

        self._warn_timeout(cmd, timeout)

        proc = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        stdout = b""
        stderr = b""

        try:
            async with asyncio.timeout(timeout):
                stdout, stderr = await proc.communicate()

        except TimeoutError as exc:
            try:
                proc.kill()
            except ProcessLookupError:
                pass
            
            stdout, stderr = await proc.communicate()

            raise ScanTimeoutError(
                stdout=stdout.decode(errors="replace"),
                stderr=stderr.decode(errors="replace"),
                timeout=timeout,
            ) from exc

        except Exception:
            try:
                proc.kill()
            except ProcessLookupError:
                pass
            
            await proc.wait()
            raise

        if proc.returncode != 0:
            raise NmapExecutionError(
                stderr.decode(errors="ignore"),
                stdout.decode(errors="ignore"),
                proc.returncode,
            )

        raw_xml = stdout.decode(errors="ignore")

        root = ElementTree.fromstring(raw_xml)

        return parse_scan_report(
            nmaprun=root,
            raw_xml=raw_xml,
        )

    async def scan(
        self,
        target: str,
        *arguments: str,
        timeout: int | None = None,
    ) -> ScanReport:
        """
        Execute a custom Nmap scan.

        Args:
            target:
                Target host, IP address, CIDR range, or hostname.

            arguments:
                Additional Nmap arguments.
                Example:
                    ["-sV", "-O", "-Pn"]

            timeout:
                Maximum scan runtime in seconds before the process is terminated.

                To change the package-wide default timeout:

                    from netrax.config import timeouts

                    timeouts.DEFAULT_SCAN_TIMEOUT = 300

        Returns:
            ScanReport:
                Parsed Nmap XML output including raw XML.

        Raises:
            AdminRequiredError:
                Administrator/root privileges are required.

            NmapExecutionError:
                Nmap exited with a non-zero return code.

            ScanTimeoutError:
                The scan exceeded the timeout limit.

            XmlParseError:
                Failed to parse Nmap XML output.
            
            ProcessTimeoutError:
                Internal Nmap verification timed out.
        """
        if timeout is None:
            timeout = timeouts.DEFAULT_SCAN_TIMEOUT

        cmd = [
            "nmap",
            *arguments,
            "-oX",
            "-",
            target,
        ]

        return await self._run_scan(
            cmd=cmd,
            timeout=timeout,
        )

    async def service_scan(
        self,
        target: str,
        timeout: int | None = None,
    ) -> ScanReport:
        """
        Perform Nmap service and version detection (-sV).
        
        This scan attempts to identify services running on open ports and,
        when possible, determine the software product and version.
        
        Args:
            target:
                Target IP address, hostname, or network range.
        
            timeout:
                Maximum scan runtime in seconds before the scan is terminated.
        
                To change the global default timeout:
        
                    from netrax.config import timeouts
        
                    timeouts.DEFAULT_SCAN_TIMEOUT = 300
        
        Returns:
            ScanReport:
                Parsed Nmap scan report.
        
        Raises:
            AdminRequiredError:
                Administrator/root privileges are required.
        
            NmapExecutionError:
                Nmap returned a non-zero exit code.
        
            ScanTimeoutError:
                The scan exceeded the configured timeout.
        
            XmlParseError:
                Failed to parse Nmap XML output.
        
            ProcessTimeoutError:
                Internal Nmap verification timed out.
        """
        if timeout is None:
            timeout = timeouts.DEFAULT_SCAN_TIMEOUT


        return await self.scan(
            target,
            "-sV",
            timeout=timeout,
        )

    async def syn_scan(
        self,
        target: str,
        timeout: int | None = None,
    ) -> ScanReport:
        """
        Perform a TCP SYN scan (-sS).

        A SYN scan is one of Nmap's fastest and most commonly used scan types.
        It identifies open TCP ports without completing the full TCP handshake.

        Args:
            target:
                Target IP address, hostname, or network range.

            timeout:
                Maximum scan runtime in seconds.

        Returns:
            ScanReport:
                Parsed Nmap scan report.
        """
        if timeout is None:
            timeout = timeouts.DEFAULT_SCAN_TIMEOUT

        return await self.scan(
            target,
            "-sS",
            timeout=timeout,
        )

    async def udp_scan(
        self,
        target: str,
        timeout: int | None = None,
    ) -> ScanReport:
        """
        Perform a UDP scan (-sU).

        UDP scans attempt to discover services listening on UDP ports.
        These scans are often slower than TCP scans and may require a larger
        timeout value.

        Args:
            target:
                Target IP address, hostname, or network range.

            timeout:
                Maximum scan runtime in seconds.

        Returns:
            ScanReport:
                Parsed Nmap scan report.
        """
        if timeout is None:
            timeout = timeouts.DEFAULT_SCAN_TIMEOUT

        return await self.scan(
            target,
            "-sU",
            timeout=timeout,
        )

    async def os_scan(
        self,
        target: str,
        timeout: int | None = None,
    ) -> ScanReport:
        """
        Perform operating system detection (-O).
        
        Nmap analyzes network responses and attempts to determine the
        target operating system.
        
        Args:
            target:
                Target IP address, hostname, or network range.
        
            timeout:
                Maximum scan runtime in seconds.
        
        Returns:
            ScanReport:
                Parsed Nmap scan report.
        """
        if timeout is None:
            timeout = timeouts.DEFAULT_SCAN_TIMEOUT

        return await self.scan(
            target,
            "-O",
            timeout=timeout,
        )

    async def aggressive_scan(
        self,
        target: str,
        timeout: int | None = None,
    ) -> ScanReport:
        """
        Perform an aggressive scan (-A).

        This enables OS detection, version detection, script scanning,
        and traceroute.

        Aggressive scans are significantly slower than basic scans and may
        require increasing the timeout value.

        Args:
            target:
                Target IP address, hostname, or network range.

            timeout:
                Maximum scan runtime in seconds.

        Returns:
            ScanReport:
                Parsed Nmap scan report.
        """
        if timeout is None:
            timeout = timeouts.DEFAULT_SCAN_TIMEOUT

        return await self.scan(
            target,
            "-A",
            timeout=timeout,
        )

    async def ping_scan(
        self,
        target: str,
        timeout: int | None = None,
    ) -> ScanReport:
        """
        Perform host discovery (-sn).       

        This scan determines whether hosts are online without performing
        a port scan.        

        Args:
            target:
                Target IP address, hostname, or network range.      

            timeout:
                Maximum scan runtime in seconds.        

        Returns:
            ScanReport:
                Parsed Nmap scan report.
        """
        if timeout is None:
            timeout = timeouts.DEFAULT_SCAN_TIMEOUT

        return await self.scan(
            target,
            "-sn",
            timeout=timeout,
        )