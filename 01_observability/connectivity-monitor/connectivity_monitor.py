#!/usr/bin/env python3
"""
CONNECTIVITY MONITOR - ICMP Observability Tool
Author: Reuben Empere
Description:
Monitors network connectivity to a target host using ICMP ping.
Detects outages based on consecutive failures and logs outage
start and recovery events with timestamps.
"""

import subprocess
import time
from datetime import datetime
import sys
import os

LOG_FILE = "outage_log.txt"


def ping_host(host="8.8.8.8", count=1, timeout=2):
    """
    Send ICMP ping to specified host.

    Returns:
        bool: True if host is reachable, False otherwise
    """
    try:
        if sys.platform.startswith("win"):
            command = ["ping", "-n", str(count), "-w", str(timeout * 1000), host]
        else:
            command = ["ping", "-c", str(count), "-W", str(timeout), host]

        result = subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=timeout + 2
        )

        return result.returncode == 0

    except subprocess.TimeoutExpired:
        return False
    except Exception:
        return False


def log_outage(host, event):
    """
    Write outage events to log file.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {host}: {event}\n"

    with open(LOG_FILE, "a") as f:
        f.write(entry)


def print_status(host, is_up, failures, check_count):
    status = "REACHABLE" if is_up else "UNREACHABLE"
    icon = "✅" if is_up else "❌"

    print("\n" + "=" * 50)
    print(f"Check #{check_count}: {host} is {status} {icon}")
    print(f"Consecutive failures: {failures}")
    print(f"Time: {datetime.now().strftime('%H:%M:%S')}")
    print("=" * 50)


def print_log_summary():
    """
    Display a short summary of logged outages on shutdown.
    """
    if not os.path.exists(LOG_FILE):
        print("\nNo outage log file found.")
        return

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    if not lines:
        print("\nLog file is empty.")
        return

    outage_count = sum(1 for line in lines if "OUTAGE_START" in line)

    print("\n" + "=" * 50)
    print("OUTAGE LOG SUMMARY")
    print(f"Total outages recorded: {outage_count}")
    print(f"Total log entries: {len(lines)}")
    print("Most recent events:")
    for line in lines[-5:]:
        print(f"  {line.strip()}")
    print("=" * 50)


def monitor_connectivity(host="8.8.8.8", interval=10, max_failures=3):
    print(f"""
╔══════════════════════════════════════════╗
║     NETWORK CONNECTIVITY MONITOR         ║
║     Author: Reuben Empere                ║
╚══════════════════════════════════════════╝

Target Host: {host}
Check Interval: {interval}s
Failure Threshold: {max_failures} consecutive failures

Press Ctrl+C to stop
""")

    consecutive_failures = 0
    check_count = 0
    was_up = None  # Correct initialization: unknown initial state

    try:
        while True:
            check_count += 1
            is_up = ping_host(host)

            if is_up:
                consecutive_failures = 0
            else:
                consecutive_failures += 1

            print_status(host, is_up, consecutive_failures, check_count)

            # Detect outage start at threshold crossing
            if not is_up and consecutive_failures == max_failures:
                log_outage(host, "OUTAGE_START")

            # Detect recovery (only log when coming from DOWN state)
            if is_up and was_up is False:
                log_outage(host, "OUTAGE_END")

            was_up = is_up
            time.sleep(interval)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
        print_log_summary()
        sys.exit(0)


if __name__ == "__main__":
    TARGET_HOST = "8.8.8.8"
    CHECK_INTERVAL = 10
    FAILURE_THRESHOLD = 3

    monitor_connectivity(
        host=TARGET_HOST,
        interval=CHECK_INTERVAL,
        max_failures=FAILURE_THRESHOLD
    )