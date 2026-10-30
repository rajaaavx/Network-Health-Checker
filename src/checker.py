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

    if not ip_host or ip_host.strip():
        raise ValueError("Host Cannot be empty!")

    ip_host = ip_host.strip()
     

def main():
    print("=" *40)
    print("       Network Health Checker")
    print("=" *40)

    ip_host = input("Enter IP adders or Domain: ").strip()

    try:
        hasil = checker(ip_host)
    except ValueError as err:       #error handling
        print(f"Error: {err}")


if __name__ == "__main__":
    main()

# a = input("input : ").strip()
# print(a.strip())