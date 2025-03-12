import sys
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.uic import loadUi
from output_windowExt import Ui_OutputDialog

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("mainwindow.ui", self)
        self.pushButtonRun.clicked.connect(self.runSlot)
        self._new_window = None
        self.Videocapture_ = None
    def refreshAll(self):
        """Lấy giá trị từ giao diện"""
        self.Videocapture_ = "0"
    def runSlot(self):
        """Chạy khi người dùng bấm nút Run"""
        print("Clicked Run")
        self.refreshAll()
        print(f"Camera: {self.Videocapture_}")
        self.hide()  # Ẩn cửa sổ chính
        self.outputWindow_()  # Mở cửa sổ kết quả

    def outputWindow_(self):
        """Mở cửa sổ hiển thị video"""
        self._new_window = Ui_OutputDialog()  # Khởi tạo cửa sổ mới
        self._new_window.show()
        self._new_window.startVideo(self.Videocapture_)  # Truyền dữ liệu camera vào
        print("Video Started")
