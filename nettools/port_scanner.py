# nettools/port_scanner.py
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
}

def scan_port(host, port, timeout=0.3):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            return port, (result == 0)
    except Exception:
        return port, False

def parse_ports(port_input):
    ports = set()
    if not port_input.strip():
        return []  # Empty input returns no ports

    for part in port_input.split(','):
        part = part.strip()
        if not part:
            continue
        if '-' in part:
            try:
                start, end = map(int, part.split('-'))
                ports.update(range(start, end + 1))
            except ValueError:
                continue
        else:
            try:
                ports.add(int(part))
            except ValueError:
                continue
    return sorted(list(ports))

def port_scan(host, port_input, max_threads=100):
    ports = parse_ports(port_input)
    print(f"Parsed ports: {ports}")  # 👈 debug print
    if not ports:
        return {}

    results = {}
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(scan_port, host, port) for port in ports]
        for future in as_completed(futures):
            port, is_open = future.result()
            results[port] = is_open

    return results

