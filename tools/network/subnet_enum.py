import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def scan_port(target, port):
    """Attempts to connect to a given port on a target host."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((target, port))
            print(f"[+] Port {port} is open on {target}")
    except (socket.timeout, ConnectionRefusedError):
        pass

def subdomain_enum(target, subdomains):
    """Attempts to resolve a list of subdomains for a target domain."""
    for sub in subdomains:
        full_url = f"{sub}.{target}"
        try:
            ip = socket.gethostbyname(full_url)
            print(f"[+] Found: {full_url} -> {ip}")
        except socket.gaierror:
            pass

def main():
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner & Subdomain Enumerator")
    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("-p", "--ports", type=str, help="Port range (e.g., 1-1000)", default="1-1024")
    parser.add_argument("-s", "--subdomains", type=str, help="Subdomains file (one per line)")
    args = parser.parse_args()
    
    start_port, end_port = map(int, args.ports.split("-"))
    
    print(f"Scanning {args.target} for open ports {start_port}-{end_port}...")
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, args.target, port)
    
    if args.subdomains:
        try:
            with open(args.subdomains, "r") as f:
                subdomains = [line.strip() for line in f]
            print(f"Enumerating subdomains for {args.target}...")
            subdomain_enum(args.target, subdomains)
        except FileNotFoundError:
            print("[!] Subdomains file not found.")
    
    print("Scan complete.")

if __name__ == "__main__":
    main()

