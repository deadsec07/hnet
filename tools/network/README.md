# Network Tools

Prerequisites
- Install dependencies from the repo root with `pip install -r requirements.txt`
- Some tools require `sudo` (packet capture).

port_scanner.py
- Usage: `python tools/network/port_scanner.py`
- Prompts for target and port range (e.g., 1-1024 or 80,443)

subnet_enum.py
- Usage: `python tools/network/subnet_enum.py <target> -p 1-1000 -s subdomains.txt`

vuln_scanner.py
- Usage: `python tools/network/vuln_scanner.py`
- Prompts for target (e.g., example.com or https://example.com)

packet_sniffer.py
- Usage: `sudo python tools/network/packet_sniffer.py`
