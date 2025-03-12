import logging
from scapy.all import sniff, IP, TCP, UDP, ICMP

# Configure logging
logging.basicConfig(filename="packet_sniffer.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Define the packet handler function
def packet_handler(packet):
    try:
        # If the packet is IP
        if IP in packet:
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            ip_proto = packet[IP].proto
            logging.info(f"IP Packet: {ip_src} -> {ip_dst} | Protocol: {ip_proto}")

            # Handle different types of IP protocols
            if TCP in packet:
                tcp_sport = packet[TCP].sport
                tcp_dport = packet[TCP].dport
                logging.info(f"TCP Packet: {ip_src} -> {ip_dst} | Src Port: {tcp_sport} | Dst Port: {tcp_dport}")

            elif UDP in packet:
                udp_sport = packet[UDP].sport
                udp_dport = packet[UDP].dport
                logging.info(f"UDP Packet: {ip_src} -> {ip_dst} | Src Port: {udp_sport} | Dst Port: {udp_dport}")

            elif ICMP in packet:
                logging.info(f"ICMP Packet: {ip_src} -> {ip_dst} | Type: {packet[ICMP].type} | Code: {packet[ICMP].code}")

    except Exception as e:
        logging.error(f"Error processing packet: {e}")

# Start sniffing packets
def start_sniffing(interface="eth0", filter="ip"):
    print(f"Starting sniffing on interface {interface} with filter: {filter}")
    sniff(iface=interface, filter=filter, prn=packet_handler, store=False)

if __name__ == "__main__":
    # Start sniffing
    start_sniffing()

