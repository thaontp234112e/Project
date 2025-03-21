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
        self.Videocapture_ = "0"
    def runSlot(self):
        print("Clicked Run")
        self.refreshAll()
        print(f"Camera: {self.Videocapture_}")
        self.hide()
        self.outputWindow_()

    def outputWindow_(self):
        self._new_window = Ui_OutputDialog()
        self._new_window.show()
        self._new_window.startVideo(self.Videocapture_)
        print("Video Started")
