
# Network Health Checker

A lightweight Python CLI tool for checking host
connectivity and measuring network latency.

## Features

- Check connectivity to an IP address or domain
- Display host status (UP/DOWN)
- Extract latency from ping output when available
- Save check results to a CSV report
- Include basic unit tests

## Tech Stack

- Python
- Subprocess
- CSV
- Unit Testing

## Requirements

- Python 3.10+
- A system with the `ping` command available

## Getting Started

Clone the repository:

    git clone YOUR_REPOSITORY_URL
    cd network-health-checker

Create and activate a virtual environment:

    python -m venv .venv

On Windows PowerShell:

    .\.venv\Scripts\Activate.ps1

Run the application:

    python src/checker.py

## Testing

Run the unit tests:

    python -m unittest discover -s tests -v

## Sample Output

    NETWORK HEALTH CHECKER
    Enter IP address or domain: example.com

    --- CHECK RESULT ---
    Host    : example.com
    Status  : UP
    Latency : 20.0 ms

    Report saved to: network_report.csv

*Sample output is illustrative, not a live measurement.*

## Limitations

- Uses ICMP ping rather than checking application ports.
- Some hosts may block ping requests.
- Latency parsing depends on the operating system's
  ping output format.
- A successful ping does not guarantee that every
  service on the host is operational.

## Future Improvements

- Check multiple hosts in one run
- Add packet loss statistics
- Generate latency charts
- Build a Streamlit dashboard
