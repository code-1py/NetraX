Quick start
===========

Create a scanner and await one of its asynchronous scan methods:

.. code-block:: python

   import asyncio
   from netrax import Scanner


   async def main():
       scanner = Scanner()
       report = await scanner.service_scan("192.168.1.1")

       for host in report.hosts:
           for port in host.ports:
               service = port.services.name if port.services else "unknown"
               state = port.state.state if port.state else "unknown"
               print(f"{port.portid}/{port.protocol}: {state} ({service})")


   asyncio.run(main())

Creating ``Scanner`` checks that the process has administrator or root
privileges. NetraX verifies that Nmap is available when the first scan runs.
Use only targets for which you have authorization.

See :doc:`user-guide/scans` for the built-in scan types and custom arguments,
and :doc:`user-guide/results` for working with returned reports.
