# Changelog

Notable changes to NetraX are documented here.

## 0.1.6
- Bumped version to 0.1.6.
- Added Sphinx documentation organized by user guides and public API modules, with Read the Docs configuration.
- Expanded public API docstrings and clarified custom Nmap arguments and timeout behavior.
- Wrapped malformed Nmap XML output in `XmlParseError`.
- Switched package builds to setuptools and excluded documentation and CI assets from source distributions.
- Fixed incorrect relative imports in __init__.py.

## 0.1.5

- Published the async Nmap wrapper with typed scan result models and XML parsing.
- Added scan methods for service, SYN, UDP, OS, aggressive, and ping scans, plus custom arguments.
- Added configurable scan timeouts, privilege and Nmap availability checks, and structured exceptions.
- Added dictionary and JSON export for scan reports.
