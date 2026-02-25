import nmap


def scan_ports(target, ports):
    nm = nmap.PortScanner()
    try:
        print(f"Scanning {target} for open ports...")
        nm.scan(target, ports)

        if target not in nm.all_hosts():
            print("No host data returned.")
            return []

        print(f"Host: {target}")
        print(f"State: {nm[target].state()}")

        open_ports = []
        for protocol in nm[target].all_protocols():
            print(f"Protocol: {protocol}")
            for port, pdata in nm[target][protocol].items():
                if pdata.get('state') == 'open':
                    open_ports.append(port)
                    print(f"Open port: {port}")

        if not open_ports:
            print("No open ports found.")
        return sorted(open_ports)
    except Exception as e:
        print(f"Error scanning {target}: {e}")
        return []

if __name__ == "__main__":
    target = input("Enter the target (IP or domain): ").strip()
    ports = input("Enter the port range (e.g., 1-1024 or 80,443): ").strip()
    open_ports = scan_ports(target, ports)
    print(f"Open ports on {target}: {open_ports}")
