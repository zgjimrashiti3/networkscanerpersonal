from scapy.all import ARP, Ether, srp

def scan_network(network):
    packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=network)

    answered = srp(packet, timeout=2, verbose=0)[0]

    devices = []

    for _, received in answered:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return devices