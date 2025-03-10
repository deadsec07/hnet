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

def main():
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("-p", "--ports", type=str, help="Port range (e.g., 1-1000)", default="1-1024")
    args = parser.parse_args()
    
    start_port, end_port = map(int, args.ports.split("-"))
    
    print(f"Scanning {args.target} for open ports {start_port}-{end_port}...")
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, args.target, port)
    
    print("Scan complete.")

if __name__ == "__main__":
    main()

