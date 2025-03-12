import nmap

def scan_ports(target, ports):
    nm = nmap.PortScanner()
    try:
        print(f"Scanning {target} for open ports...")
        nm.scan(target, ports)
        
        # Print scan results
        print(f"Host: {target}")
        print(f"State: {nm[target].state()}")
        
        # Check open ports
        open_ports = []
        for protocol in nm[target].all_protocols():
            print(f"Protocol: {protocol}")
            lport = nm[target][protocol].keys()
            for port in lport:
                if nm[target][protocol][port]['state'] == 'open':
                    open_ports.append(port)
                    print(f"Open port: {port}")
        
        if not open_ports:
            print("No open ports found.")
        return open_ports
    except Exception as e:
        print(f"Error scanning {target}: {e}")
        return []

if __name__ == "__main__":
    target = input("Enter the target (IP or domain): ").strip()
    ports = input("Enter the port range (e.g., 1-1024, 80,443): ").strip()
    open_ports = scan_ports(target, ports)
    print(f"Open ports on {target}: {open_ports}")

