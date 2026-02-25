import socket
import requests
import ssl
import nmap
from urllib.parse import urlparse

# Function to scan for open ports
def port_scanner(target, ports):
    scanner = nmap.PortScanner()
    try:
        print(f"Scanning {target} for open ports...")
        scanner.scan(target, ports)
        open_ports = []
        if target not in scanner.all_hosts():
            return open_ports
        proto_map = scanner[target]
        for proto in proto_map.all_protocols():
            for port, pdata in proto_map[proto].items():
                if pdata.get('state') == 'open':
                    open_ports.append(port)
        return sorted(open_ports)
    except Exception as e:
        print(f"Error scanning ports: {e}")
        return []

# Function to check common HTTP security headers
def check_http_headers(url):
    try:
        print(f"Checking HTTP headers for {url}...")
        response = requests.head(url, timeout=8, allow_redirects=True)
        headers = response.headers
        missing_headers = []

        required_headers = [
            "Strict-Transport-Security",
            "X-Content-Type-Options",
            "X-Frame-Options",
            "Content-Security-Policy",
            "X-XSS-Protection",
        ]

        for header in required_headers:
            if header not in headers:
                missing_headers.append(header)

        if missing_headers:
            print(f"Missing headers: {', '.join(missing_headers)}")
        else:
            print("All important HTTP security headers are present.")
    except requests.exceptions.RequestException as e:
        print(f"Error checking HTTP headers: {e}")

# Function to check SSL/TLS configuration (if applicable)
def ssl_check(host):
    try:
        print(f"Checking SSL/TLS configuration for {host}...")
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname=host) as s:
            s.settimeout(8)
            s.connect((host, 443))  # Attempt connection on port 443 (HTTPS)
            cert = s.getpeercert()
            print(f"SSL Certificate for {host} - Subject: {cert['subject']}")
            # Checking if SSL/TLS version is weak (e.g., SSLv2 or SSLv3)
            cipher = s.cipher()
            print(f"Using cipher: {cipher[0]}")
    except ssl.SSLError as e:
        print(f"SSL/TLS Error: {e}")
    except Exception as e:
        print(f"Error checking SSL/TLS configuration: {e}")

# Main vulnerability scanning function
def vuln_scanner(target):
    # Port Scanning
    open_ports = port_scanner(target, '1-1024')  # Scan ports 1 to 1024
    if open_ports:
        print(f"Open ports on {target}: {open_ports}")
    else:
        print(f"No open ports found on {target}.")
    
    # HTTP Header Check (for web applications)
    if target.startswith('http'):
        check_http_headers(target)
    
    # SSL/TLS Check (for HTTPS)
    if target.startswith('https'):
        ssl_check(urlparse(target).hostname)
    else:
        print(f"{target} is not an HTTPS URL, skipping SSL/TLS check.")

if __name__ == "__main__":
    target = input("Enter the target (e.g., example.com or https://example.com): ").strip()
    vuln_scanner(target)
