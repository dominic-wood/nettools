import platform
import subprocess
import re

def run_traceroute(host):
    system = platform.system().lower()
    if system == "windows":
        cmd = ["tracert", host]
    else:
        cmd = ["traceroute", host]

    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.splitlines()
    except Exception as e:
        return [f"Error: {e}"]
