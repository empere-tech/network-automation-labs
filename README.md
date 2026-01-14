# Network Automation Labs

A curated portfolio of Python-based networking and security automation projects demonstrating the practical application of CompTIA Network+ and Security+ concepts through real-world operational tooling.

This repository bridges **theoretical networking and security fundamentals** with **hands-on observability, fault detection, and automation engineering**.

---

## 🎯 Mission

To demonstrate the transition from foundational networking and security theory into **production-minded automation tools** used in real technical operations, SOC, and infrastructure environments.

Each project:
- Solves a concrete operational problem
- Implements protocol-aware logic (ICMP, TCP, UDP, DNS)
- Emphasizes reliability, fault tolerance, and clean logging
- Is **interview-ready and defensible**

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Core Libraries:** `subprocess`, `time`, `datetime`, `socket`
- **Protocols:** ICMP, TCP/IP, UDP, DNS
- **Environment:** Windows, Linux, macOS
- **Execution Model:** CLI-first (future-ready for Docker/VPS deployment)

---

## 🚀 Portfolio Projects

### ✅ Connectivity Monitor v1.0  
📁 `/connectivity-monitor/`

**AUDITED & DEPLOYED** — An ICMP-based network observability tool that monitors host reachability and logs outages with intelligent state-aware detection.

#### Key Features
- **Threshold-based outage detection**  
  Prevents false positives by logging outages only after configurable consecutive failures
- **State-change logging**  
  Records `OUTAGE_START` and `OUTAGE_END` events with ISO-8601 timestamps
- **Cross-platform compatibility**  
  Works consistently across Windows, Linux, and macOS
- **Professional logging**  
  Clean, parser-friendly logs (`outage_log.txt`) suitable for audits and analysis
- **Graceful shutdown behavior**  
  Displays an outage summary upon controlled termination

#### Technologies
Python 3.8+, ICMP Protocol, Subprocess, File I/O, State Machine Logic

#### Learning Objectives Demonstrated
- Practical ICMP protocol implementation
- Fault tolerance and false-positive reduction
- Event-driven logging for operational visibility
- Cross-platform scripting best practices
- Defensive error handling and user experience design

🔗 [View Code](./connectivity-monitor/connectivity_monitor.py)  
📄 [View Documentation](./connectivity-monitor/README.md)

---

## 📂 Project Status

### Active Development
1. **Port Scanner Lite** *(Security Logic)* — *In Development*
   - CLI-based TCP port scanner (ports 22, 80, 443)
   - Demonstrates TCP handshake fundamentals and safe scanning practices

2. **DNS Lookup Tool** *(Network Resolution)* — *Planned*
   - Batch DNS resolution utility for domain lists
   - Focus on UDP/DNS behavior, timeouts, and exception handling

### Completed Projects
- **✅ Connectivity Monitor** — **v1.0 (Audited & Deployed)**

---

## 🎓 CompTIA Objective Mapping

**Network+**
- ICMP fundamentals
- Network troubleshooting methodologies
- TCP/IP and DNS concepts

**Security+**
- Availability and resilience
- Operational monitoring
- Secure scripting practices
- Signal vs noise awareness in detection systems

---

## 👨‍💻 Author

**Reuben Empere**  
*Entry-Level Technical Operations & Security Automation Professional*  
CompTIA Security+ | CompTIA Network+

📍 Lekki, Lagos, Nigeria (UTC+1)  
📧 rb.empere@gmail.com  
📱 +234 810 863 2175  
🔗 [LinkedIn](https://linkedin.com/in/reuben-empere-0173493a4)  
💻 [GitHub](https://github.com/empere-tech)

---

## 🧠 Learning Philosophy

This portfolio emphasizes **applied understanding over theory memorization**.

> *“Theory without practice is sterile; practice without theory is blind.”*  
> — Adapted from Immanuel Kant

