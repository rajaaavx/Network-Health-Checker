import csv #laporan
import platform 
import re   #regex
import subprocess
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
REPORT_FILE = BASE_DIR / "network_report.csv"

