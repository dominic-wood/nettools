# run.py
from gui.main import NetToolsApp
from PySide6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NetToolsApp()
    window.show()
    sys.exit(app.exec())
