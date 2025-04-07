from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon

app = QApplication([])
window = QWidget()
window.setWindowTitle("Test App")
window.setWindowIcon(QIcon("assets/icon.icns"))
window.show()
app.exec()
