``netrax.exceptions``
=====================

NetraX exceptions provide specific error types for permission checks, Nmap
execution, timeouts, invalid targets, and XML parsing.

.. automodule:: netrax.exceptions
   :members:
   :undoc-members:
   :imported-members:

Typical handling
----------------

.. code-block:: python

   from netrax import Scanner
   from netrax.exceptions import (
       AdminRequiredError,
       NmapExecutionError,
       NmapNotFoundError,
       ScanTimeoutError,
       XmlParseError,
   )

   try:
       report = await Scanner().service_scan("192.168.1.1", timeout=120)
   except AdminRequiredError:
       print("Run with administrator/root privileges.")
   except NmapNotFoundError:
       print("Install Nmap and make sure it is on PATH.")
   except ScanTimeoutError as exc:
       print(f"The scan exceeded {exc.timeout} seconds.")
   except NmapExecutionError as exc:
       print(f"Nmap exited with {exc.returncode}: {exc.stderr}")
   except XmlParseError:
       print("Nmap returned XML that NetraX could not parse.")

``AdminRequiredError`` can be raised when ``Scanner`` is constructed.
The other errors occur while checking Nmap or executing and parsing a scan.
