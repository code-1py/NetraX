``netrax.xml_parsing``
======================

This module exposes the helper that converts an Nmap XML document into a
``ScanReport``. Most users can use the scanner methods, which perform this
parsing automatically.

For an XML string that was obtained separately, parse the root element and
pass both the element and the original string:

.. code-block:: python

   from xml.etree import ElementTree
   from netrax.xml_parsing import parse_scan_report

   xml_text = "<nmaprun scanner='nmap'><host /></nmaprun>"
   root = ElementTree.fromstring(xml_text)
   report = parse_scan_report(root, raw_xml=xml_text)

.. automodule:: netrax.xml_parsing
   :members:
   :undoc-members:
   :imported-members:
