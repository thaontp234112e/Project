# File: register_windowExt.py
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
        loadUi("register_window.ui", self)
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
            # Save temporarily and display
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
        full_name = self.lineEditFullName.text().strip()
        if not student_id:
            QMessageBox.warning(self, "Warning", "Student ID is required.")
            return
        if not full_name:
            QMessageBox.warning(self, "Warning", "Full name is required.")
            return
        if not self.photo_path:
            QMessageBox.warning(self, "Warning", "Student photo is required.")
            return
        images_dir = "ImagesAttendance"
        if not os.path.exists(images_dir):
            os.makedirs(images_dir)
        dest_path = os.path.join(images_dir, f"{student_id}.jpg")
        try:
            shutil.copy(self.photo_path, dest_path)
            if self.photo_path == "temp_capture.jpg" and os.path.exists(self.photo_path):
                os.remove(self.photo_path)
            self.save_student_info(student_id, full_name)
            QMessageBox.information(
                self, "Success", f"Student {full_name} ({student_id}) registered successfully."
            )
            self.accept()  # Close dialog with success
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to register student: {str(e)}")
    def save_student_info(self, student_id, full_name):
        import csv
        file_exists = os.path.isfile('students.csv')
        with open('students.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(['StudentID', 'FullName'])
            writer.writerow([student_id, full_name])
# For testing
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_RegisterDialog()
    window.show()
    sys.exit(app.exec())