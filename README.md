# NetTools - Network Utility Suite 🛠️🌐

NetTools is a Python-based GUI application that bundles essential network utilities into a clean, beginner-friendly interface. It’s designed for sysadmins, students, and anyone curious about their network.

## 🚀 Features

### 🔍 Ping Sweeper
Scan a local subnet and find live hosts with a threaded ping utility.

### 🔐 Port Scanner
Check for open ports on a given host (e.g. 22, 80, 443). Fast, threaded, and color-coded.

### 🌐 DNS Lookup
Get A, AAAA, MX, and NS records for any domain using dnspython.

## 📸 Screenshots

<p align="center">
  <img src="gui/assets/dns_lookup.png" width="500" style="margin-bottom: -70px;">
  <img src="gui/assets/port_scanner.png" width="500" style="margin-bottom: -70px;">
  <img src="gui/assets/dns_lookup.png" width="500">
</p>

## 🧱 Tech Stack

- Python 3.11+
- PySide6 – GUI
- dnspython – DNS queries
- `socket`, `ipaddress`, `concurrent.futures` – network logic

## 🧰 Setup

```bash
git clone https://github.com/yourname/nettools.git
cd nettools
pip install -r requirements.txt
python -m gui.main
```

## 📦 Requirements
``` txt
pyside6
dnspython
```

## ✍️ About
This project was created to combine my background in network engineering and software development with my passion for technical writing. Each tool is carefully documented and designed to demonstrate clarity, structure, and usefulness.