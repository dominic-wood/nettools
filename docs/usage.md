# Usage Guide for NetTools App

## 1. **Overview**

NetTools is a network utility app that provides several essential tools for network diagnostics, including:

- **Ping Sweeper**: Identify active devices in a subnet.
- **Port Scanner**: Check if specified ports are open on a given host.
- **DNS Lookup**: Resolve domain names to IP addresses.
- **Traceroute**: Trace the network route to a destination.

The app is packaged as a standalone executable, which can be run directly without the need for Python installation.

## 2. **Installation**

### 2.1 **Pre-built Application**

After building the app with PyInstaller, you can find the **`NetToolsApp`** in the `dist` folder. Simply navigate to the `dist` folder and double-click on the **`NetToolsApp`** to start using the application.

### 2.2 **Running from Source**

To run the application from source, ensure you have Python 3.13 and the required dependencies installed:

```bash
pip install -r requirements.txt
```

Then, run the app using:

```bash
python run.py
```

## 3. **Usage Instructions**

### 3.1 **Ping Sweeper**

1. In the **Ping Sweeper** tab, enter a subnet (e.g., `192.168.1.0/24`).
2. Click **Scan** to check which devices are online in the subnet.
3. The results will display with IP addresses and their status (online/offline).

### 3.2 **Port Scanner**

1. In the **Port Scanner** tab, enter a target host (e.g., `192.168.1.1`) and a range of ports (e.g., `20-25, 80, 443`).
2. Click **Scan** to check if the specified ports are open.
3. The results will display the status of each port (open/closed) and the corresponding service if detected.

### 3.3 **DNS Lookup**

1. In the **DNS Lookup** tab, enter the domain name you want to look up (e.g., `google.com`).
2. Click **Lookup** to resolve the domain to its associated IP addresses.
3. The results will display DNS records (A, AAAA, etc.) for the given domain.

### 3.4 **Traceroute**

1. In the **Traceroute** tab, enter an IP address or domain (e.g., `8.8.8.8`).
2. Click **Trace Route** to trace the network route to the destination.
3. The results will display each hop along the path with response times.

## 4. **Troubleshooting**

### 4.1 **Common Errors**

- **"Invalid subnet format"**: Ensure the subnet is entered correctly (e.g., `192.168.1.0/24`).
- **"No ports scanned (check input)"**: Double-check the host and port range entered. Make sure the host is reachable.
- **"Failed to resolve domain"**: If the DNS lookup fails, check your network connection or the domain entered.

### 4.2 **Permissions on macOS**

If running the app on macOS, you might need to allow it in **Security & Privacy** settings if it’s blocked by macOS Gatekeeper.

## 5. **Future Features**

The following features are being considered for future versions:

- **Support for additional network tools** (e.g., bandwidth testing, HTTP requests).
- **Cross-platform improvements** to ensure better compatibility with Windows and Linux.
- **Improved user interface** for more user-friendly interaction.

## 6. **Contribution**

If you'd like to contribute to the development of NetTools, feel free to fork the repository and submit pull requests. For more details on contributing, please refer to the [CONTRIBUTING](CONTRIBUTING.md).
