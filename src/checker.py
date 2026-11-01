import csv #laporan
import platform 
import re   #regex
import subprocess
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
REPORT_FILE = BASE_DIR / "network_report.csv"

def checker(ip_host):
    print("Checking Connectivity...")

    if not ip_host or not ip_host.strip():
        raise ValueError("Host Cannot be empty!")

    ip_host = ip_host.strip()


    if platform.system().lower == "windows":
        command = ["ping", "-n", "1", "-w", "2000", ip_host]  #khusus windows
    else:
        command = ["ping", "-c", "1", ip_host]   #buat linux ama macOS

    try:
        hasil = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=5
        )
    except (subprocess.TimeoutExpired, OSError):
        return {
            "host": ip_host,
            "status": "DOWN",
            "latency_ms": None
        }

    output = hasil.stdout + hasil.stderr #digabung soalnya ada yang di kiri atau ga di kanan hasil ping nya??

    if hasil.returncode != 0:
        status = "DOWN"
        latency = "None"
    else:
        status = "UP"

        # cari latency pake regexc
        match = re.search(
            r"time[=<]\s*(\d+(?:\.\d+)?)\s*ms",
            output,
            re.IGNORECASE
        )

        latency = float(match.group(1)) if match else None #kalo match ambil group 1

        return{
            "Host" : ip_host,
            "Status" : status,
            "Latency" : latency 
        }
    
    
    

def save_report(hasil):
    """Append a check result to a CSV report."""

    file_exists = REPORT_FILE.exists()

def main():
    print("=" *40)
    print("       Network Health Checker")
    print("=" *40)

    ip_host = input("Enter IP adders or Domain: ").strip()

    try:
        hasil = checker(ip_host)
    except ValueError as err:       #error handling
        print(f"Error: {err}")
        return

    print("\n--- CHECK RESULT ---")
    print(f"Host    : {hasil['Host']}")
    print(f"Status  : {hasil['Status']}")

    Latency = hasil["Latency"]
    print(
        f"Latency: {Latency}" if Latency is not None
        else "Latency: N/A"
    )

    save_report(hasil)



if __name__ == "__main__":
    main()
    

# a = input("input : ").strip()
# print(a.strip())