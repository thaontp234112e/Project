import os
import sys
import cv2
from PyQt6.QtWidgets import QDialog, QFileDialog, QMessageBox, QApplication
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.uic import loadUi
import shutil

class Ui_RegisterDialog(QDialog):
    def __init__(self):
        super(Ui_RegisterDialog, self).__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.base_dir = os.path.dirname(current_dir)
        ui_file = os.path.join(current_dir, "register_window.ui")
        loadUi(ui_file, self)
        self.student_photo = None
        self.photo_path = None
        self.pushButtonUpload.clicked.connect(self.upload_photo)
        self.pushButtonCapture.clicked.connect(self.capture_photo)
        self.pushButtonRegister.clicked.connect(self.register_student)
        self.pushButtonCancel.clicked.connect(self.close)

    def upload_photo(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            self, "Select Student Photo", "", "Image Files (*.png *.jpg *.jpeg)"
        )

        if file_path:
            self.photo_path = file_path
            pixmap = QPixmap(file_path)
            self.labelPhoto.setPixmap(pixmap.scaled(400, 300))
            self.labelStatus.setText("Photo uploaded successfully")

    def capture_photo(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            QMessageBox.critical(self, "Error", "Could not open camera.")
            return
        ret, frame = cap.read()
        cap.release()

        if ret:
            temp_path = "temp_capture.jpg"
            cv2.imwrite(temp_path, frame)
            self.photo_path = temp_path
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame_rgb.shape
            q_img = QImage(frame_rgb.data, w, h, ch * w, QImage.Format.Format_RGB888)
            pixmap = QPixmap.fromImage(q_img)
            self.labelPhoto.setPixmap(pixmap.scaled(400, 300))
            self.labelStatus.setText("Photo captured successfully")
        else:
            QMessageBox.warning(self, "Warning", "Failed to capture photo.")

    def register_student(self):
        student_id = self.lineEditStudentID.text().strip()
        if not student_id:
            QMessageBox.warning(self, "Warning", "Student ID is mandatory.")
            return

        if not self.photo_path:
            QMessageBox.warning(self, "Warning", "Student photo is mandatory.")
            return

        images_dir = os.path.join(self.base_dir, "ImagesAttendance")
        if not os.path.exists(images_dir):
            os.makedirs(images_dir)

        dest_path = os.path.join(images_dir, f"{student_id}.jpg")
        try:
            img = cv2.imread(self.photo_path)
            cv2.imwrite(dest_path, img)

            if self.photo_path == "temp_capture.jpg" and os.path.exists(self.photo_path):
                os.remove(self.photo_path)

            QMessageBox.information(
                self, "Success", f"Face registration has been completed for the student with ID {student_id}."
            )
            self.clearLayout()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Unable to register face: {str(e)}")

    def clearLayout(self):
        self.lineEditStudentID.setText('')
        self.lineEditFullName.setText('')
        self.labelPhoto.clear()
        self.labelStatus.setText("")
        self.lineEditStudentID.setFocus( )



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_RegisterDialog()
    window.show()
    sys.exit(app.exec())