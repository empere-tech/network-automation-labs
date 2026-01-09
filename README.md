Network Automation Labs

A repository of Python-based automation tools bridging foundational networking and security concepts (CompTIA Network+ / Security+) with hands-on operational engineering.

🎯 Mission

Demonstrate the transition from theoretical networking and security principles to automated observability, fault detection, and secure system operations. Each tool is actively developed to reflect real-world operational workflows.

🛠️ Tech Stack

Language: Python 3.10+

Libraries: subprocess, time, datetime, socket

Protocols: ICMP, TCP/IP, UDP, DNS

Environment: Linux / Windows / macOS

Deployment: CLI-first, future-ready for Docker/VPS deployment

📂 Active Project Portfolio
1. Connectivity Monitor (In Progress)

Objective: Automate network uptime tracking and outage logging.

Logic: Pings external targets (e.g., 8.8.8.8) every 30 seconds and logs failures with ISO-8601 timestamps.

Fail-Safe: Avoids false positives by implementing a 2-fail threshold before logging.

CompTIA Mapping:

Network+: Network Troubleshooting, ICMP fundamentals

Security+: Availability, operational resilience
