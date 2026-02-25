#!/usr/bin/env python3
import argparse
import sys
import subprocess
from pathlib import Path


def cmd_network_port_scan(args):
    import tools.network.port_scanner as ps
    open_ports = ps.scan_ports(args.target, args.ports)
    print(f"Open ports on {args.target}: {open_ports}")


def cmd_network_vuln_scan(args):
    import tools.network.vuln_scanner as vs
    vs.vuln_scanner(args.target)


def cmd_network_subnet_enum(args):
    import tools.network.subnet_enum as se
    start_port, end_port = map(int, args.ports.split("-"))
    from concurrent.futures import ThreadPoolExecutor
    print(f"Scanning {args.target} for open ports {start_port}-{end_port}...")
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(se.scan_port, args.target, port)
    if args.subdomains:
        try:
            subs = [line.strip() for line in Path(args.subdomains).read_text().splitlines() if line.strip()]
        except FileNotFoundError:
            print("[!] Subdomains file not found.")
        else:
            print(f"Enumerating subdomains for {args.target}...")
            se.subdomain_enum(args.target, subs)
    print("Scan complete.")


def cmd_network_sniff(args):
    import tools.network.packet_sniffer as sn
    sn.start_sniffing(interface=args.iface, filter=args.filter)


def cmd_web_sql(args):
    import tools.web.sql_injector as sql
    sql.test_sql_injection(args.url, sql.SQL_PAYLOADS, args.param)


def cmd_web_xss(args):
    import tools.web.xss_tester as xss
    xss.test_xss(args.url, args.param)


def cmd_web_recon(args):
    import tools.web.web_recon as recon
    from urllib.parse import urlparse
    domain = urlparse(args.url).netloc
    recon.dns_lookup(domain)
    recon.whois_lookup(domain)
    recon.http_headers(args.url)
    recon.ssl_info(domain)
    recon.subdomain_enum(domain)


def cmd_wireless_wifi_deauth(args):
    import tools.wireless.wifi_deauth as wifi
    wifi.check_monitor_mode(args.iface)
    print("Starting the deauthentication attack... Press Ctrl-C to stop.")
    try:
        while True:
            wifi.deauth(args.target_mac, args.gateway_mac, args.iface)
    except KeyboardInterrupt:
        print("\n[INFO] Deauthentication attack stopped.")


def cmd_wireless_bluetooth_scan(args):
    import tools.wireless.bluetooth_scanner as bt
    bt.scan_bluetooth_devices()


def cmd_exploit_encode(args):
    import tools.exploitation.shellcode_encoder as enc
    print(enc.encode_shellcode(args.text, args.type))


def cmd_exploit_decode(args):
    import tools.exploitation.shellcode_encoder as enc
    print(enc.decode_shellcode(args.encoded, args.type))


def cmd_exploit_buffer_overflow(args):
    import tools.exploitation.buffer_overflow as bo
    bo.buffer_overflow_simulation()


def cmd_exploit_keylogger(args):
    # Run as subprocess to avoid import side-effects
    import tools.exploitation.keylogger as _kl  # only to locate file
    script = Path(_kl.__file__).resolve()
    print("Starting keylogger; press ESC to stop. Logs in keylog.txt")
    subprocess.run([sys.executable, str(script)])


def cmd_auto_exploit(args):
    from autoexploit.AutoExploit import AutoExploit
    runner = AutoExploit(args.url)
    runner.scan_for_vulnerabilities()
    runner.generate_payloads()
    runner.test_exploits()
    runner.generate_report()
    if args.pdf:
        from autoexploit.AutoReport import AutoReport
        rpt = AutoReport(args.url, runner.vulnerabilities, runner.exploit_results)
        rpt.create_pdf_report()


def build_parser():
    p = argparse.ArgumentParser(prog="hnet", description="hnet pentest toolkit CLI")
    sub = p.add_subparsers(dest="cmd")

    # network
    pn = sub.add_parser("network", help="Network utilities")
    sn = pn.add_subparsers(dest="sub")

    pnp = sn.add_parser("port-scan", help="TCP port scan")
    pnp.add_argument("target")
    pnp.add_argument("ports", help="range like 1-1024 or list 80,443")
    pnp.set_defaults(func=cmd_network_port_scan)

    pnv = sn.add_parser("vuln-scan", help="Basic vuln scan")
    pnv.add_argument("target", help="hostname or URL")
    pnv.set_defaults(func=cmd_network_vuln_scan)

    pns = sn.add_parser("subnet-enum", help="Threaded port scan + subdomains")
    pns.add_argument("target")
    pns.add_argument("--ports", default="1-1024")
    pns.add_argument("--subdomains", help="file with subdomains")
    pns.set_defaults(func=cmd_network_subnet_enum)

    pni = sn.add_parser("sniff", help="Packet sniffer (requires sudo)")
    pni.add_argument("--iface", default="eth0")
    pni.add_argument("--filter", default="ip")
    pni.set_defaults(func=cmd_network_sniff)

    # web
    pw = sub.add_parser("web", help="Web utilities")
    sw = pw.add_subparsers(dest="sub")

    pws = sw.add_parser("sql-test", help="SQL injection checks")
    pws.add_argument("url")
    pws.add_argument("param")
    pws.set_defaults(func=cmd_web_sql)

    pwx = sw.add_parser("xss-test", help="Reflected XSS checks")
    pwx.add_argument("url")
    pwx.add_argument("param")
    pwx.set_defaults(func=cmd_web_xss)

    pwr = sw.add_parser("recon", help="Basic recon suite")
    pwr.add_argument("url")
    pwr.set_defaults(func=cmd_web_recon)

    # wireless
    pwi = sub.add_parser("wireless", help="Wireless utilities")
    swi = pwi.add_subparsers(dest="sub")

    pww = swi.add_parser("wifi-deauth", help="802.11 deauth (Linux monitor mode)")
    pww.add_argument("target_mac")
    pww.add_argument("gateway_mac")
    pww.add_argument("iface")
    pww.set_defaults(func=cmd_wireless_wifi_deauth)

    pwb = swi.add_parser("bluetooth-scan", help="Discover BT devices")
    pwb.set_defaults(func=cmd_wireless_bluetooth_scan)

    # exploitation
    pe = sub.add_parser("exploit", help="Exploitation helpers")
    se = pe.add_subparsers(dest="sub")

    pee = se.add_parser("encode", help="Encode text")
    pee.add_argument("text")
    pee.add_argument("type", choices=["hex", "base64"])
    pee.set_defaults(func=cmd_exploit_encode)

    ped = se.add_parser("decode", help="Decode text")
    ped.add_argument("encoded")
    ped.add_argument("type", choices=["hex", "base64"])
    ped.set_defaults(func=cmd_exploit_decode)

    peb = se.add_parser("buffer-overflow", help="Simulated buffer overflow")
    peb.set_defaults(func=cmd_exploit_buffer_overflow)

    pek = se.add_parser("keylogger", help="Run keylogger (authorized use only)")
    pek.set_defaults(func=cmd_exploit_keylogger)

    # auto
    pa = sub.add_parser("auto", help="Automation")
    sa = pa.add_subparsers(dest="sub")

    pae = sa.add_parser("exploit", help="AutoExploit + optional PDF")
    pae.add_argument("url")
    pae.add_argument("--pdf", action="store_true", help="Generate PDF report as well")
    pae.set_defaults(func=cmd_auto_exploit)

    return p


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if not hasattr(args, "func"):
        parser.print_help()
        return 1
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())

