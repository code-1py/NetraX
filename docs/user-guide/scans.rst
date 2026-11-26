Running scans
=============

Every scanner method is asynchronous and returns a
:class:`netrax.models.ScanReport`.

Built-in scan methods
---------------------

.. list-table::
   :header-rows: 1

   * - Method
     - Nmap option
     - Purpose
   * - ``service_scan(target)``
     - ``-sV``
     - Detect services and versions.
   * - ``syn_scan(target)``
     - ``-sS``
     - Perform a TCP SYN scan.
   * - ``udp_scan(target)``
     - ``-sU``
     - Scan UDP ports.
   * - ``os_scan(target)``
     - ``-O``
     - Attempt operating system detection.
   * - ``aggressive_scan(target)``
     - ``-A``
     - Enable OS detection, version detection, scripts, and traceroute.
   * - ``ping_scan(target)``
     - ``-sn``
     - Discover online hosts without a port scan.

Each built-in method accepts an optional timeout in seconds. The default is
``timeouts.DEFAULT_SCAN_TIMEOUT``.

Custom arguments
----------------

Use :meth:`netrax.Scanner.scan` to pass Nmap options directly:

.. code-block:: python

   report = await scanner.scan(
       "10.0.0.0/24",
       "-sV",
       "-O",
       "-T4",
       "--open",
       timeout=300,
   )

Pass each option as its own string argument. Do not include the executable
name (``nmap``) or the target among ``arguments``; NetraX adds the target
after the options. It also adds ``-oX -`` so it can capture and parse Nmap's
XML output.

If options are stored in a list, unpack the list:

.. code-block:: python

   options = ["-sV", "--top-ports", "100"]
   report = await scanner.scan("192.168.1.1", *options, timeout=300)

To use a custom Nmap option that takes a value, pass the option and value as
separate strings, as in ``"--top-ports", "100"``. The ``timeout`` keyword is
NetraX's timeout in seconds; do not pass it as an Nmap command-line option.

Nmap scan options can affect scan duration and privileges required. Consult
the `Nmap reference guide <https://nmap.org/book/man.html>`_ for option
semantics, and scan only authorized targets.
