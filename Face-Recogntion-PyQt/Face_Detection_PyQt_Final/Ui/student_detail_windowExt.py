import os
import csv
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import cv2
from PyQt6.QtWidgets import QDialog, QFileDialog, QMessageBox, QTableWidgetItem
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
from student_detail_window import Ui_StudentDetailDialog
from models.attendance_manager import QuanLyDiemDanh


class Ui_StudentDetailDialogExt(QDialog, Ui_StudentDetailDialog):
    def __init__(self, student_id, student_name, quan_ly_diem_danh=None):
        super(Ui_StudentDetailDialogExt, self).__init__()
        self.setupUi(self)

        self.student_id = student_id
        self.student_name = student_name
        self.quan_ly_diem_danh = quan_ly_diem_danh if quan_ly_diem_danh else QuanLyDiemDanh()
        self.photo_path = None
        
        # Get base directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.base_dir = os.path.dirname(current_dir)

        self.lineEditStudentID.setText(self.student_id)
        self.lineEditFullName.setText(self.student_name)

        self.load_student_photo()

        self.setup_attendance_table()

        self.pushButtonUpload.clicked.connect(self.upload_photo)
        self.pushButtonCapture.clicked.connect(self.capture_photo)
        self.pushButtonSave.clicked.connect(self.save_student_info)
        self.pushButtonDelete.clicked.connect(self.delete_student)
        self.pushButtonCancel.clicked.connect(self.close)

    def load_student_photo(self):
        photo_path = os.path.join(self.base_dir, "ImagesAttendance", f"{self.student_id}.jpg")
        if os.path.exists(photo_path):
            pixmap = QPixmap(photo_path)
            self.labelPhoto.setPixmap(pixmap.scaled(300, 250, Qt.AspectRatioMode.KeepAspectRatio))
            self.labelPhotoStatus.setText("Photo already exists")
        else:
            self.labelPhoto.setText("No photo available")
            self.labelPhotoStatus.setText("Photo not registered")

    def setup_attendance_table(self):

        self.tableWidgetAttendance.setColumnCount(3)
        self.tableWidgetAttendance.setHorizontalHeaderLabels(["Ngày", "Giờ", "Trạng thái"])

        attendance_list = []

        student = None
        for sv in self.quan_ly_diem_danh.lay_danh_sach_sinh_vien():
            if sv.ma_sv == self.student_id:
                student = sv
                break

        if student:
            for record in student.danh_sach_diem_danh:
                time_str = record['thoi_gian']
                date_parts = time_str.split()
                date = date_parts[0] if len(date_parts) > 0 else time_str
                time = date_parts[1] if len(date_parts) > 1 else ""

                attendance_list.append({
                    'date': date,
                    'time': time,
                    'status': record['trang_thai']
                })

        attendance_list.sort(key=lambda x: (x['date'], x['time']), reverse=True)

        self.tableWidgetAttendance.setRowCount(len(attendance_list))
        for row, record in enumerate(attendance_list):
            self.tableWidgetAttendance.setItem(row, 0, QTableWidgetItem(record['date']))
            self.tableWidgetAttendance.setItem(row, 1, QTableWidgetItem(record['time']))
            self.tableWidgetAttendance.setItem(row, 2, QTableWidgetItem(record['status']))

        header = self.tableWidgetAttendance.horizontalHeader()
        header.setSectionResizeMode(0, header.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, header.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, header.ResizeMode.Stretch)

    def upload_photo(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            self, "Select student photo", "", "Image Files (*.png *.jpg *.jpeg)"
        )

        if file_path:
            self.photo_path = file_path
            pixmap = QPixmap(file_path)
            self.labelPhoto.setPixmap(pixmap.scaled(300, 250, Qt.AspectRatioMode.KeepAspectRatio))
            self.labelPhotoStatus.setText("Photo uploaded, click Save to update")

    def capture_photo(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            QMessageBox.critical(self, "Error", "Unable to open camera.")
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
            self.labelPhoto.setPixmap(pixmap.scaled(300, 250, Qt.AspectRatioMode.KeepAspectRatio))
            self.labelPhotoStatus.setText("Photo taken, click Save to update")
        else:
            QMessageBox.warning(self, "Warning", "Unable to take photo.")

    def save_student_info(self):
        new_student_id = self.lineEditStudentID.text().strip()
        new_student_name = self.lineEditFullName.text().strip()

        if not new_student_id:
            QMessageBox.warning(self, "Warning", "Student ID cannot be empty.")
            return

        if not new_student_name:
            QMessageBox.warning(self, "Warning", "Student name cannot be empty.")
            return

        if new_student_id != self.student_id:
            for sv in self.quan_ly_diem_danh.lay_danh_sach_sinh_vien():
                if sv.ma_sv == new_student_id:
                    QMessageBox.warning(self, "Warning", f"Student ID {new_student_id} already exists.")
                    return

        updated = False
        students_csv = os.path.join(self.base_dir, "dataset", "students.csv")
        temp_file = os.path.join(self.base_dir, "dataset", "students_temp.csv")
        
        with open(students_csv, "r", newline="", encoding="utf-8") as csvfile, \
                open(temp_file, "w", newline="", encoding="utf-8") as tempfile:
            reader = csv.reader(csvfile)
            writer = csv.writer(tempfile)

            for row in reader:
                if len(row) >= 2 and row[0] == self.student_id:
                    writer.writerow([new_student_id, new_student_name])
                    updated = True
                else:
                    writer.writerow(row)

            if not updated:
                writer.writerow([new_student_id, new_student_name])

        os.replace(temp_file, students_csv)

        if self.photo_path:
            images_dir = os.path.join(self.base_dir, "ImagesAttendance")
            if not os.path.exists(images_dir):
                os.makedirs(images_dir)

            img = cv2.imread(self.photo_path)
            dest_path = os.path.join(images_dir, f"{new_student_id}.jpg")
            cv2.imwrite(dest_path, img)

            if self.photo_path == "temp_capture.jpg" and os.path.exists(self.photo_path):
                os.remove(self.photo_path)

            old_image_path = os.path.join(images_dir, f"{self.student_id}.jpg")
            if new_student_id != self.student_id and os.path.exists(old_image_path):
                os.remove(old_image_path)

        QMessageBox.information(self, "Successfully", "Student information updated.")

        self.quan_ly_diem_danh.load_student_info()

        self.student_id = new_student_id
        self.student_name = new_student_name
        self.load_student_photo()

        self.setup_attendance_table()

    def delete_student(self):
        reply = QMessageBox.question(
            self,
            "Deleted confirmation",
            f"Are you sure you want to delete student {self.student_name} ({self.student_id})?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            students_csv = os.path.join(self.base_dir, "dataset", "students.csv")
            temp_file = os.path.join(self.base_dir, "dataset", "students_temp.csv")
            deleted = False

            with open(students_csv, "r", newline="", encoding="utf-8") as csvfile, \
                    open(temp_file, "w", newline="", encoding="utf-8") as tempfile:
                reader = csv.reader(csvfile)
                writer = csv.writer(tempfile)

                for row in reader:
                    if len(row) >= 2 and row[0] == self.student_id:
                        deleted = True
                        continue
                    writer.writerow(row)

            os.replace(temp_file, students_csv)

            image_path = os.path.join(self.base_dir, "ImagesAttendance", f"{self.student_id}.jpg")
            if os.path.exists(image_path):
                os.remove(image_path)

            self.quan_ly_diem_danh.load_student_info()

            if deleted:
                QMessageBox.information(self, "Successfully", f"Deleted student {self.student_name}.")
            else:
                QMessageBox.warning(self, "Notification", f"Student {self.student_id} not found in the system.")

            self.close() 