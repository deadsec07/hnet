# hnet – Pentest Toolkit

Modern, scriptable penetration testing utilities for network, web, wireless, exploitation, and basic automation.

Warning and ethics
- For authorized security testing only. Obtain explicit, written permission before scanning or attacking any systems you do not own.
- You are responsible for compliance with local laws and policies. The maintainers disclaim any liability for misuse.

Supported targets
- Python 3.9+ on Linux, macOS, and Windows (some wireless features are Linux‑only).

Quick start
- Linux/macOS
  - `./scripts/install_dependencies.sh`
  - `./scripts/setup_virtualenv.sh`
- Windows (PowerShell)
  - `python -m venv venv`
  - `venv\Scripts\Activate.ps1`
  - `pip install -r requirements.txt`

After activation
- `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows)
- Unified CLI: `./hnet <group> <command> [options]`
  - Examples:
    - `./hnet network port-scan example.com 1-1024`
    - `./hnet web recon https://example.com`
    - `./hnet exploit encode "This is a test" base64`
    - `./hnet auto exploit https://example.com --pdf`

Install as a command
- Local editable install: `pip install -e .`
- Or system/user install: `pip install .` (consider `pipx install .`)
- Then run `hnet --help` from anywhere.

Tools overview
- Network: `port_scanner.py`, `subnet_enum.py`, `vuln_scanner.py`, `packet_sniffer.py`
- Web: `sql_injector.py`, `xss_tester.py`, `web_recon.py`
- Wireless: `wifi_deauth.py` (Linux/monitor mode), `bluetooth_scanner.py`
- Exploitation: `shellcode_encoder.py`, `buffer_overflow.py`, `keylogger.py`
- Automation: `autoexploit/AutoExploit.py`, `autoexploit/AutoReport.py`

Installation details
- Requirements are listed in `requirements.txt` (root).
- System dependencies: `nmap`, `tcpdump` (for packet capture), monitor‑mode capable Wi‑Fi adapter for wireless features.

Scripts
- `scripts/install_dependencies.sh`: Install system packages via apt or Homebrew and Python deps.
- `scripts/setup_virtualenv.sh`: Create and populate a local venv.
- `scripts/install_requirements.py`: Python alternative to install dependencies from the root `requirements.txt`.

Documentation
- See `tools/*/README.md` and `autoexploit/README.md` for tool‑specific usage.
- `INSTALL.md` contains platform setup steps.

Contributing
- Open issues and pull requests are welcome. Please keep changes minimal, with clear descriptions and follow the existing code style.

License
- See `LICENSE`.

Releasing
- See `docs/RELEASING.md` for versioning, build, and publish steps.
