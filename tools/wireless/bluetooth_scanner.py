import bluetooth

def scan_bluetooth_devices():
    print("Scanning for Bluetooth devices...")
    
    nearby_devices = bluetooth.discover_devices(lookup_names=True, lookup_oui=True, lookup_oui=True, device_id=0, lookup_oui=True, lookup_oui=True)

    if not nearby_devices:
        print("No Bluetooth devices found.")
    else:
        print(f"{'Device Address':<20} {'Device Name'}")
        print("-" * 40)
        for addr, name in nearby_devices:
            print(f"{addr:<20} {name}")

def main():
    scan_bluetooth_devices()

if __name__ == "__main__":
    main()

