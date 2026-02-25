import bluetooth


def scan_bluetooth_devices():
    print("Scanning for Bluetooth devices...")

    # Discover nearby devices for ~8 seconds and include device names
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True)

    if not nearby_devices:
        print("No Bluetooth devices found.")
        return

    print(f"{'Device Address':<20} {'Device Name'}")
    print("-" * 40)
    for addr, name in nearby_devices:
        print(f"{addr:<20} {name}")


def main():
    scan_bluetooth_devices()


if __name__ == "__main__":
    main()
