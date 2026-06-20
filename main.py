from scanner.discovery import scan_network

def main():
    network = input("Network (e.g. 192.168.1.0/24): ")

    print("\nScanning...\n")

    devices = scan_network(network)

    if not devices:
        print("No devices found.")
        return

    for d in devices:
        print(f"{d['ip']} -> {d['mac']}")

if __name__ == "__main__":
    main()