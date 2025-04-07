from concurrent.futures import ThreadPoolExecutor, as_completed
import ipaddress
import subprocess
import platform

def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    result = subprocess.run(
        ["ping", param, "1", str(host)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return str(host), result.returncode == 0

def ping_sweep(subnet, max_threads=50):
    try:
        network = ipaddress.ip_network(subnet, strict=False)
    except ValueError:
        return {"Error": False}

    results = {}
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(ping, ip) for ip in network.hosts()]
        for future in as_completed(futures):
            ip, is_up = future.result()
            results[ip] = is_up
    return results
