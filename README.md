<p align="center">
  <img src="assets/nettools_logo.png" alt="NetTools Logo" width="250">
</p>

# NetTools - Network Utility Suite 🛠️🌐

**NetTools** is a Python-based GUI app that brings together key network tools in a simple, user-friendly interface. It’s built for sysadmins, students, and curious tinkerers who want quick access to useful diagnostics.

## 🚀 Features

### 🔍 **Ping Sweeper**
Scan a local subnet and find live hosts with a threaded ping utility.

### 🔐 **Port Scanner**
Check for open ports on a given host (e.g. 22, 80, 443). Fast, threaded, and color-coded for quick results.

### 🌐 **DNS Lookup**
Get **A**, **AAAA**, **MX**, and **NS** records for any domain using the **dnspython** library.

### 🧭 **Traceroute**
Trace the path your connection takes to reach a domain or IP. View each hop, including IPs, hostnames, and response times.

## 📸 Screenshots

<p align="center">
  <div style="display: flex; justify-content: center; margin-top: -10px;">
    <img src="assets/ping_sweeper.png" width="350">
    <img src="assets/port_scanner.png" width="350">
  </div>
  <div style="display: flex; justify-content: center; margin-top: -20px;">
    <img src="assets/dns_lookup.png" width="350">
    <img src="assets/traceroute.png" width="350">
  </div>
</p>

## 🧱 Tech Stack

- **Python 3.13+**
- **PySide6** – GUI framework
- **dnspython** – DNS queries
- **`socket`, `ipaddress`, `concurrent.futures`** – Network logic

## 🧰 Usage

See the [Usage Guide](docs/usage.md) for step-by-step instructions on each tool.

## 📝 Design Notes

Curious about how it works? Check out the [Design Notes](docs/design-notes.md) for an architectural breakdown and future roadmap.

## ✍️ About

This project combines my background in networking and software development with a love for clean, clear tool design. NetTools is built to be practical, easy to understand, and useful.