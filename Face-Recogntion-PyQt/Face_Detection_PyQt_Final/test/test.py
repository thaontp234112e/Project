import sys
import os

# Thêm đường dẫn tới thư mục Ui để có thể import từ đó
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
ui_dir = os.path.join(parent_dir, 'Ui')
sys.path.append(ui_dir)

from PyQt6.QtWidgets import QApplication
from mainwindowExt import MainWindow  # Import class từ thư mục Ui

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())

