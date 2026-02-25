Installation

Linux / macOS
- chmod +x scripts/install_dependencies.sh scripts/setup_virtualenv.sh
- ./scripts/install_dependencies.sh
- ./scripts/setup_virtualenv.sh

Windows (PowerShell)
- python -m venv venv
- venv\Scripts\Activate.ps1
- pip install -r requirements.txt

Alternative (any platform)
- python scripts/install_requirements.py

After installation
- Activate the environment:
  - Linux/macOS: source venv/bin/activate
  - Windows: venv\Scripts\activate
- Run tools from the repo root, e.g.:
  - python tools/network/port_scanner.py
