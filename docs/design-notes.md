# NetTools – Design Notes

## 1. Overview

NetTools is a GUI app that combines essential network tools:

- **Ping Sweeper** – Identify online devices in a subnet.
- **Port Scanner** – Check for open ports on a target host.
- **DNS Lookup** – Resolve domain names to IPs.
- **Traceroute** – Map the path to a destination.

## 2. Architecture

### 2.1 Frontend (GUI)

Built with **PySide6 (Qt for Python)**, the GUI includes:

- A tabbed layout for each tool
- Input fields for IPs, ports, domains, etc.
- Output areas to display results

### 2.2 Backend (Logic)

Each tool is modular and lives in the `nettools/` directory:

- `ping_sweeper.py` – ICMP ping sweeps across subnets
- `port_scanner.py` – Uses sockets to check open ports
- `dns_lookup.py` – DNS resolution via `dns.resolver`
- `traceroute.py` – Sends packets with increasing TTLs to trace routes

## 3. Key Design Decisions

### 3.1 Libraries

- **PySide6** for a cross-platform GUI
- **dnspython** for DNS queries
- **PyInstaller** to bundle the app
- **pyobjc + AppKit** (macOS) to set a Dock icon

### 3.2 Packaging

- On macOS, the app is bundled as a single `.app` file using PyInstaller
- Custom Dock icon is set via `AppKit`

### 3.3 Error Handling

Handled gracefully through the UI:

- Invalid IPs or port ranges trigger clear messages
- DNS failures and network errors are caught and displayed

## 4. Planned Features

- More tools (e.g., HTTP requests, bandwidth checks)
- Better cross-platform support (Windows, Linux)
- Smarter error messages and exception handling
