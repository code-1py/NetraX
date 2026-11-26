Configuration
=============

NetraX exposes two timeout defaults from ``netrax.config.timeouts``:

* ``DEFAULT_SCAN_TIMEOUT`` is the scan process timeout in seconds (default: 60).
* ``NMAP_LOCATE_TIMEOUT`` is the timeout used while checking Nmap availability
  (default: 3).

Change a default for the current process:

.. code-block:: python

   from netrax.config import timeouts

   timeouts.DEFAULT_SCAN_TIMEOUT = 120
   timeouts.NMAP_LOCATE_TIMEOUT = 5

To set a timeout for one scan, pass ``timeout`` to its method:

.. code-block:: python

   report = await scanner.aggressive_scan("192.168.1.1", timeout=300)

Slow Nmap timing templates such as ``-T0``, ``-T1``, and ``-T2`` can exceed
the default scan timeout. NetraX emits a warning when one of these templates
is supplied to a custom scan.
