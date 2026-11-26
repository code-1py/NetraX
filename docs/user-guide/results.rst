Working with results
====================

Each scan returns a :class:`netrax.models.ScanReport` with Nmap metadata,
host results, and the original XML output.

.. code-block:: python

   report = await scanner.service_scan("192.168.1.1")

   for host in report.hosts:
       for address in host.address:
           print("Address:", address.addr)

       for port in host.ports:
           state = port.state.state if port.state else "unknown"
           print(f"{port.portid}/{port.protocol}: {state}")

           if port.services:
               print("  Service:", port.services.name)
               print("  Product:", port.services.product)
               print("  Version:", port.services.version)

The report can be converted to built-in Python structures or JSON:

.. code-block:: python

   data = report.to_dict()
   json_text = report.to_json(indent=2)
   xml_text = report.raw_xml

The data model is nested: a report contains hosts; hosts contain addresses,
host names, ports, and timing information; ports contain state and service
details. See :doc:`../api/models` for the complete exported model list.
