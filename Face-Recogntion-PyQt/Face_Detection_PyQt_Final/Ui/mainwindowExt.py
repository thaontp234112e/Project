import sys
import os
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.uic import loadUi
from output_windowExt import Ui_OutputDialog

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file = os.path.join(current_dir, "mainwindow.ui")
        loadUi(ui_file, self)
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
