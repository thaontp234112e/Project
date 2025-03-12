import sys
from PyQt6.QtWidgets import QApplication
from mainwindowExt import MainWindow  # Import class đã sửa đổi

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())

