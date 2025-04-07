# Design Notes for NetTools App

### 1. **Overview**

The NetTools App is a simple network utility tool that includes the following features:

- **Ping Sweeper**: Sweep a subnet to identify online devices.
- **Port Scanner**: Scan a range of ports on a given host to check for open ports.
- **DNS Lookup**: Perform DNS lookups to resolve domain names.
- **Traceroute**: Trace the network path to a destination.

### 2. **App Architecture**

#### 2.1 **Frontend (GUI)**
The frontend is built using **PySide6 (Qt for Python)** to provide a cross-platform graphical user interface. It includes:

- **Tabs for each feature** (Ping Sweeper, Port Scanner, DNS Lookup, Traceroute).
- Interactive input fields for user configuration (e.g., IP addresses, port ranges).
- **Output text areas** for displaying the results (ping results, port scan results, etc.).
  
#### 2.2 **Backend (Functionality)**
Each feature is implemented as a separate module within the `nettools/` directory:

- **ping_sweeper.py**: Performs ICMP pings across a range of IP addresses.
- **port_scanner.py**: Scans specified ports on a given host using `socket` connections.
- **dns_lookup.py**: Uses the `dns.resolver` library to resolve domain names.
- **traceroute.py**: Implements a basic traceroute by sending packets with increasing TTL values and logging the responses.

### 3. **App Design Decisions**

#### 3.1 **Choice of Libraries**
- **PySide6 (Qt for Python)** was chosen for the GUI due to its cross-platform capabilities and its ability to create a rich and responsive UI.
- **PyInstaller** is used to bundle the app into a standalone executable, which simplifies distribution.
- **`pyobjc`** is used to interact with macOS-specific components (like setting the Dock icon).

#### 3.2 **Icon Design**
The app icon is designed to represent a network utility tool, with a simple and recognizable design. It is used in both the app window and in the macOS Dock.

#### 3.3 **Portability Considerations**
- The app is packaged as a **single file** on macOS using **PyInstaller** to ensure ease of deployment.
- The `AppKit` library is used to manage the **Dock icon**, which is a macOS-specific feature.
  
#### 3.4 **Error Handling**
The app is designed to gracefully handle errors such as invalid input or network errors. For example:
- Invalid IP addresses or port ranges result in error messages.
- Network issues during port scanning or traceroute result in appropriate messages displayed in the UI.

### 4. **Future Enhancements**

- **Add more network tools** like HTTP request testing, bandwidth monitoring, etc.
- **Support for additional platforms** (Linux, Windows) by testing and ensuring cross-platform compatibility.
- **Improved error handling** to catch specific network-related errors more effectively.

