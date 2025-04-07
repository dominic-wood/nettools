import sys
import os

from PySide6.QtWidgets import QApplication
from gui.main import NetToolsApp

if sys.platform == "darwin":
    # macOS-specific code to set the Dock icon
    from AppKit import NSApplication, NSImage
    from Foundation import NSURL

    icon_path = os.path.abspath("assets/icon.icns")  # Adjust path if needed
    app = NSApplication.sharedApplication()
    image = NSImage.alloc().initWithContentsOfFile_(icon_path)
    app.setApplicationIconImage_(image)

# Now run the main PySide6 app
app = QApplication(sys.argv)
window = NetToolsApp()
window.show()
sys.exit(app.exec())
