Installation
============

Requirements
------------

* Python 3.11 or newer.
* Nmap installed separately and available on ``PATH``.
* Administrator or root privileges for most Nmap scan types.

Install NetraX from PyPI:

.. code-block:: console

   python -m pip install netrax

Install Nmap from the `official download page <https://nmap.org/download.html>`_.
On Debian or Ubuntu, for example, use ``sudo apt install nmap``. On macOS,
Homebrew users can run ``brew install nmap``.

Verify that Nmap is available by running ``nmap --version`` in a terminal.

.. note::

   NetraX does not bundle or redistribute Nmap. Nmap is an external program
   and has its own license.
