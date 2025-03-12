import requests
import socket
import whois
import ssl
import OpenSSL
from urllib.parse import urlparse
from dns import resolver

# DNS Lookup
def dns_lookup(domain):
    try:
        print("\n[INFO] DNS Lookup for domain:", domain)
        answers = resolver.resolve(domain, 'A')
        for rdata in answers:
            print(f"IP Address: {rdata.to_text()}")
    except Exception as e:
        print(f"[ERROR] DNS Lookup failed: {e}")

# Whois Lookup
def whois_lookup(domain):
    try:
        print("\n[INFO] Whois Lookup for domain:", domain)
        w = whois.whois(domain)
        print(w)
    except Exception as e:
        print(f"[ERROR] Whois Lookup failed: {e}")

# HTTP Headers Inspection
def http_headers(url):
    try:
        print("\n[INFO] HTTP Headers Inspection for URL:", url)
        response = requests.head(url)
        for header, value in response.headers.items():
            print(f"{header}: {value}")
    except requests.RequestException as e:
        print(f"[ERROR] HTTP Headers inspection failed: {e}")

# SSL/TLS Information
def ssl_info(domain):
    try:
        print("\n[INFO] SSL/TLS Information for domain:", domain)
        context = ssl.create_default_context()
        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=domain)
        conn.connect((domain, 443))
        cert = conn.getpeercert()
        subject = dict(x[0] for x in cert['subject'])
        issuer = dict(x[0] for x in cert['issuer'])
        print(f"Subject: {subject}")
        print(f"Issuer: {issuer}")
    except Exception as e:
        print(f"[ERROR] SSL/TLS Info retrieval failed: {e}")

# Subdomain Enumeration using DNS
def subdomain_enum(domain):
    try:
        print("\n[INFO] Subdomain Enumeration for domain:", domain)
        subdomains = ["www", "mail", "ftp", "webmail", "ns", "blog", "api"]
        for sub in subdomains:
            subdomain = f"{sub}.{domain}"
            try:
                answers = resolver.resolve(subdomain, 'A')
                for rdata in answers:
                    print(f"Subdomain {subdomain} IP: {rdata.to_text()}")
            except Exception as e:
                print(f"[INFO] Subdomain {subdomain} not found.")
    except Exception as e:
        print(f"[ERROR] Subdomain enumeration failed: {e}")

# Main function
def main():
    print("Web Reconnaissance Tool")
    
    url = input("\nEnter the target URL (with protocol, e.g., https://example.com): ").strip()
    domain = urlparse(url).netloc
    
    dns_lookup(domain)
    whois_lookup(domain)
    http_headers(url)
    ssl_info(domain)
    subdomain_enum(domain)

if __name__ == "__main__":
    main()

