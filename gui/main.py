import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QTextEdit, QTabWidget
)
from PySide6.QtCore import QThread, Signal, QObject

from PySide6.QtGui import QTextCharFormat, QColor, QIcon
from nettools.ping_sweeper import ping_sweep
from nettools.port_scanner import port_scan, COMMON_PORTS
from nettools.dns_lookup import perform_dns_lookup
from nettools.traceroute import run_traceroute

# ---------- Thread Workers ----------

class PingWorker(QObject):
    finished = Signal(object)

    def __init__(self, subnet):
        super().__init__()
        self.subnet = subnet

    def run(self):
        result = ping_sweep(self.subnet)
        self.finished.emit(result)


class PortScanWorker(QObject):
    finished = Signal(object)

    def __init__(self, host, port_range):
        super().__init__()
        self.host = host
        self.port_range = port_range

    def run(self):
        result = port_scan(self.host, self.port_range)
        self.finished.emit(result)

class DnsLookupWorker(QObject):
    finished = Signal(object)

    def __init__(self, domain):
        super().__init__()
        self.domain = domain

    def run(self):
        result = perform_dns_lookup(self.domain)
        self.finished.emit(result)

class TracerouteWorker(QObject):
    finished = Signal(object)

    def __init__(self, host):
        super().__init__()
        self.host = host

    def run(self):
        result = run_traceroute(self.host)
        self.finished.emit(result)

# ---------- Main GUI ----------

class NetToolsApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Net Tools")
        self.setMinimumSize(500, 400)

        self.tabs = QTabWidget()
        self.tabs.addTab(self.ping_tab_ui(), "Ping Sweeper")
        self.tabs.addTab(self.port_tab_ui(), "Port Scanner")
        self.tabs.addTab(self.dns_tab_ui(), "DNS Lookup")
        self.tabs.addTab(self.traceroute_tab_ui(), "Traceroute")

        self.setWindowTitle("Net Tools")
        self.setWindowIcon(QIcon("assets/icon.icns"))  

        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        self.setLayout(layout)

    def append_colored(self, text_edit, text, color):
        cursor = text_edit.textCursor()
        fmt = QTextCharFormat()
        fmt.setForeground(QColor(color))  # Convert string to QColor
        cursor.insertText(text + "\n", fmt)
        text_edit.setTextCursor(cursor)


    # --- Ping Tab ---

    def ping_tab_ui(self):
        widget = QWidget()
        layout = QVBoxLayout()

        self.ping_input = QLineEdit()
        self.ping_input.setPlaceholderText("Enter Subnet (e.g. 192.168.1.0/24)")
        self.ping_button = QPushButton("Scan")
        self.ping_output = QTextEdit()
        self.ping_output.setReadOnly(True)

        self.ping_button.clicked.connect(self.run_ping)

        layout.addWidget(self.ping_input)
        layout.addWidget(self.ping_button)
        layout.addWidget(self.ping_output)
        widget.setLayout(layout)
        return widget

    def run_ping(self):
        subnet = self.ping_input.text()
        self.ping_output.clear()
        self.ping_output.append("Scanning... please wait")

        self.ping_thread = QThread()
        self.ping_worker = PingWorker(subnet)
        self.ping_worker.moveToThread(self.ping_thread)

        self.ping_thread.started.connect(self.ping_worker.run)
        self.ping_worker.finished.connect(self.display_ping_results)
        self.ping_worker.finished.connect(self.ping_thread.quit)
        self.ping_worker.finished.connect(self.ping_worker.deleteLater)
        self.ping_thread.finished.connect(self.ping_thread.deleteLater)

        self.ping_thread.start()

    def display_ping_results(self, results):
        self.ping_output.clear()
        if "Error" in results:
            self.append_colored(self.ping_output, "Invalid subnet format.", "red")
            return
        for ip, status in results.items():
            color = "green" if status else "red"
            text = f"{ip} - {'Online' if status else 'Offline'}"
            self.append_colored(self.ping_output, text, color)


    # --- Port Scan Tab ---

    def port_tab_ui(self):
        widget = QWidget()
        layout = QVBoxLayout()

        self.port_host_input = QLineEdit()
        self.port_host_input.setPlaceholderText("Enter Host (e.g. 192.168.1.1)")

        self.port_range_input = QLineEdit()
        self.port_range_input.setPlaceholderText("Enter Ports (e.g. 20-25,80,443)")

        self.port_button = QPushButton("Scan")
        self.port_output = QTextEdit()
        self.port_output.setReadOnly(True)

        self.port_button.clicked.connect(self.run_port_scan)

        layout.addWidget(QLabel("Target Host:"))
        layout.addWidget(self.port_host_input)
        layout.addWidget(QLabel("Ports:"))
        layout.addWidget(self.port_range_input)
        layout.addWidget(self.port_button)
        layout.addWidget(self.port_output)
        widget.setLayout(layout)
        return widget

    def run_port_scan(self):
        host = self.port_host_input.text()
        port_range = self.port_range_input.text()

        self.port_output.clear()
        self.port_output.append("Scanning ports...")

        self.port_thread = QThread()
        self.port_worker = PortScanWorker(host, port_range)
        self.port_worker.moveToThread(self.port_thread)

        self.port_thread.started.connect(self.port_worker.run)
        self.port_worker.finished.connect(self.display_ports)
        self.port_worker.finished.connect(self.port_thread.quit)
        self.port_worker.finished.connect(self.port_worker.deleteLater)
        self.port_thread.finished.connect(self.port_thread.deleteLater)


        self.port_thread.start()

    def display_ports(self, results):
        self.port_output.clear()

        print("display_ports() called with:", results)  # Debug print

        if not results:
            self.append_colored(self.port_output, "No ports scanned (check input).", "red")
            return

        any_open = any(results.values())
        if not any_open:
            self.append_colored(self.port_output, "All ports are closed.", "red")

        for port in sorted(results):
            is_open = results[port]
            name = COMMON_PORTS.get(port, "")
            # Skip repeating closed message if already shown
            if not is_open and not any_open:
                continue
            color = "green" if is_open else "red"
            status = "Open" if is_open else "Closed"
            service_text = f" ({name})" if name else ""
            text = f"Port {port}: {status}{service_text}"
            self.append_colored(self.port_output, text, color)

    # --- DNS Lookup Tab ---

    def dns_tab_ui(self):
        widget = QWidget()
        layout = QVBoxLayout()

        self.dns_input = QLineEdit()
        self.dns_input.setPlaceholderText("Enter domain (e.g. google.com)")

        self.dns_button = QPushButton("Lookup")
        self.dns_output = QTextEdit()
        self.dns_output.setReadOnly(True)

        self.dns_button.clicked.connect(self.run_dns_lookup)

        layout.addWidget(self.dns_input)
        layout.addWidget(self.dns_button)
        layout.addWidget(self.dns_output)
        widget.setLayout(layout)
        return widget
    
    def run_dns_lookup(self):
        domain = self.dns_input.text().strip()
        self.dns_output.clear()
        self.dns_output.append("Looking up DNS records...")

        self.dns_thread = QThread()
        self.dns_worker = DnsLookupWorker(domain)
        self.dns_worker.moveToThread(self.dns_thread)

        self.dns_thread.started.connect(self.dns_worker.run)
        self.dns_worker.finished.connect(self.display_dns_results)
        self.dns_worker.finished.connect(self.dns_thread.quit)
        self.dns_worker.finished.connect(self.dns_worker.deleteLater)
        self.dns_thread.finished.connect(self.dns_thread.deleteLater)

        self.dns_thread.start()

    def display_dns_results(self, results):
        self.dns_output.clear()
        for record_type, records in results.items():
            self.append_colored(self.dns_output, f"{record_type} Records:", "blue")
            for record in records:
                self.append_colored(self.dns_output, f"  {record}", "green" if "Error" not in record else "red")

    # --- Traceroute Tab ---
    def traceroute_tab_ui(self):
        widget = QWidget()
        layout = QVBoxLayout()

        self.trace_input = QLineEdit()
        self.trace_input.setPlaceholderText("Enter domain or IP (e.g. 8.8.8.8)")

        self.trace_button = QPushButton("Trace Route")
        self.trace_output = QTextEdit()
        self.trace_output.setReadOnly(True)

        self.trace_button.clicked.connect(self.run_traceroute)

        layout.addWidget(self.trace_input)
        layout.addWidget(self.trace_button)
        layout.addWidget(self.trace_output)
        widget.setLayout(layout)
        return widget
    
    def run_traceroute(self):
        host = self.trace_input.text().strip()
        self.trace_output.clear()
        self.trace_output.append("Tracing route...")

        self.trace_thread = QThread()
        self.trace_worker = TracerouteWorker(host)
        self.trace_worker.moveToThread(self.trace_thread)

        self.trace_thread.started.connect(self.trace_worker.run)
        self.trace_worker.finished.connect(self.display_traceroute)
        self.trace_worker.finished.connect(self.trace_thread.quit)
        self.trace_worker.finished.connect(self.trace_worker.deleteLater)
        self.trace_thread.finished.connect(self.trace_thread.deleteLater)

        self.trace_thread.start()

    def display_traceroute(self, lines):
        self.trace_output.clear()
        for line in lines:
            self.append_colored(self.trace_output, line, "green" if "*" not in line else "red")


# ---------- Run App ----------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NetToolsApp()
    window.show()
    sys.exit(app.exec())
