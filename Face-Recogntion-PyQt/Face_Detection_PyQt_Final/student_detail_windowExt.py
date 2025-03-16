# File: student_detail_windowExt.py
import os
import sys
import csv
import cv2
from PyQt6.QtWidgets import QDialog, QFileDialog, QMessageBox, QApplication, QTableWidgetItem
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
from student_detail_window import Ui_StudentDetailDialog
from attendance_manager import QuanLyDiemDanh


class Ui_StudentDetailDialogExt(QDialog, Ui_StudentDetailDialog):
    def __init__(self, student_id, student_name, quan_ly_diem_danh=None):
        super(Ui_StudentDetailDialogExt, self).__init__()
        self.setupUi(self)

        # Lưu trữ thông tin sinh viên
        self.student_id = student_id
        self.student_name = student_name
        self.quan_ly_diem_danh = quan_ly_diem_danh if quan_ly_diem_danh else QuanLyDiemDanh()
        self.photo_path = None

        # Hiển thị thông tin sinh viên
        self.lineEditStudentID.setText(self.student_id)
        self.lineEditFullName.setText(self.student_name)

        # Hiển thị ảnh sinh viên nếu có
        self.load_student_photo()

        # Cài đặt bảng thông tin điểm danh
        self.setup_attendance_table()

        # Kết nối các nút bấm với hàm xử lý
        self.pushButtonUpload.clicked.connect(self.upload_photo)
        self.pushButtonCapture.clicked.connect(self.capture_photo)
        self.pushButtonSave.clicked.connect(self.save_student_info)
        self.pushButtonDelete.clicked.connect(self.delete_student)
        self.pushButtonCancel.clicked.connect(self.close)

    def load_student_photo(self):
        """Tải và hiển thị ảnh sinh viên nếu có"""
        photo_path = f"ImagesAttendance/{self.student_id}.jpg"
        if os.path.exists(photo_path):
            pixmap = QPixmap(photo_path)
            self.labelPhoto.setPixmap(pixmap.scaled(300, 250, Qt.AspectRatioMode.KeepAspectRatio))
            self.labelPhotoStatus.setText("Đã có ảnh")
        else:
            self.labelPhoto.setText("Chưa có ảnh")
            self.labelPhotoStatus.setText("Chưa đăng ký ảnh")

    def setup_attendance_table(self):
        """Thiết lập bảng thông tin điểm danh"""
        self.tableWidgetAttendance.setColumnCount(3)
        self.tableWidgetAttendance.setHorizontalHeaderLabels(["Ngày", "Giờ", "Trạng thái"])

        # Lấy danh sách điểm danh của sinh viên
        attendance_list = []

        # Tìm sinh viên trong quản lý điểm danh
        student = None
        for sv in self.quan_ly_diem_danh.lay_danh_sach_sinh_vien():
            if sv.ma_sv == self.student_id:
                student = sv
                break

        if student:
            # Lấy danh sách điểm danh của sinh viên
            for record in student.danh_sach_diem_danh:
                # Phân tách ngày và giờ
                time_str = record['thoi_gian']
                date_parts = time_str.split()
                date = date_parts[0] if len(date_parts) > 0 else time_str
                time = date_parts[1] if len(date_parts) > 1 else ""

                attendance_list.append({
                    'date': date,
                    'time': time,
                    'status': record['trang_thai']
                })

        # Sắp xếp danh sách điểm danh theo ngày, giờ mới nhất lên đầu
        attendance_list.sort(key=lambda x: (x['date'], x['time']), reverse=True)

        # Hiển thị dữ liệu lên bảng
        self.tableWidgetAttendance.setRowCount(len(attendance_list))
        for row, record in enumerate(attendance_list):
            self.tableWidgetAttendance.setItem(row, 0, QTableWidgetItem(record['date']))
            self.tableWidgetAttendance.setItem(row, 1, QTableWidgetItem(record['time']))
            self.tableWidgetAttendance.setItem(row, 2, QTableWidgetItem(record['status']))

        # Cài đặt kích thước cột
        header = self.tableWidgetAttendance.horizontalHeader()
        header.setSectionResizeMode(0, header.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, header.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, header.ResizeMode.Stretch)

    def upload_photo(self):
        """Tải lên ảnh từ máy tính"""
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            self, "Chọn ảnh sinh viên", "", "Image Files (*.png *.jpg *.jpeg)"
        )

        if file_path:
            self.photo_path = file_path
            pixmap = QPixmap(file_path)
            self.labelPhoto.setPixmap(pixmap.scaled(300, 250, Qt.AspectRatioMode.KeepAspectRatio))
            self.labelPhotoStatus.setText("Đã tải ảnh lên, nhấn Lưu để cập nhật")

    def capture_photo(self):
        """Chụp ảnh từ webcam"""
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            QMessageBox.critical(self, "Lỗi", "Không thể mở camera.")
            return

        ret, frame = cap.read()
        cap.release()

        if ret:
            # Lưu tạm thời và hiển thị
            temp_path = "temp_capture.jpg"
            cv2.imwrite(temp_path, frame)
            self.photo_path = temp_path

            # Chuyển đổi ảnh để hiển thị
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame_rgb.shape
            q_img = QImage(frame_rgb.data, w, h, ch * w, QImage.Format.Format_RGB888)
            pixmap = QPixmap.fromImage(q_img)
            self.labelPhoto.setPixmap(pixmap.scaled(300, 250, Qt.AspectRatioMode.KeepAspectRatio))
            self.labelPhotoStatus.setText("Đã chụp ảnh, nhấn Lưu để cập nhật")
        else:
            QMessageBox.warning(self, "Cảnh báo", "Không thể chụp ảnh.")

    def save_student_info(self):
        """Lưu thông tin sinh viên"""
        # Lấy thông tin từ các ô nhập liệu
        new_student_id = self.lineEditStudentID.text().strip()
        new_student_name = self.lineEditFullName.text().strip()

        if not new_student_id:
            QMessageBox.warning(self, "Cảnh báo", "Mã số sinh viên không được để trống.")
            return

        if not new_student_name:
            QMessageBox.warning(self, "Cảnh báo", "Họ tên sinh viên không được để trống.")
            return

        # Kiểm tra xem ID mới đã tồn tại chưa (nếu đã thay đổi)
        if new_student_id != self.student_id:
            for sv in self.quan_ly_diem_danh.lay_danh_sach_sinh_vien():
                if sv.ma_sv == new_student_id:
                    QMessageBox.warning(self, "Cảnh báo", f"Mã số sinh viên {new_student_id} đã tồn tại.")
                    return

        # Cập nhật thông tin sinh viên trong file CSV
        updated = False
        temp_file = "students_temp.csv"
        with open("students.csv", "r", newline="", encoding="utf-8") as csvfile, \
                open(temp_file, "w", newline="", encoding="utf-8") as tempfile:
            reader = csv.reader(csvfile)
            writer = csv.writer(tempfile)

            for row in reader:
                if len(row) >= 2 and row[0] == self.student_id:
                    writer.writerow([new_student_id, new_student_name])
                    updated = True
                else:
                    writer.writerow(row)

            # Nếu sinh viên chưa có trong file CSV, thêm mới
            if not updated:
                writer.writerow([new_student_id, new_student_name])

        # Thay thế file cũ bằng file tạm
        os.replace(temp_file, "students.csv")

        # Cập nhật ảnh nếu có
        if self.photo_path:
            # Tạo thư mục nếu chưa tồn tại
            if not os.path.exists("ImagesAttendance"):
                os.makedirs("ImagesAttendance")

            # Đọc ảnh và lưu với tên mới
            img = cv2.imread(self.photo_path)
            dest_path = f"ImagesAttendance/{new_student_id}.jpg"
            cv2.imwrite(dest_path, img)

            # Xóa ảnh tạm nếu có
            if self.photo_path == "temp_capture.jpg" and os.path.exists(self.photo_path):
                os.remove(self.photo_path)

            # Xóa ảnh cũ nếu ID đã thay đổi
            if new_student_id != self.student_id and os.path.exists(f"ImagesAttendance/{self.student_id}.jpg"):
                os.remove(f"ImagesAttendance/{self.student_id}.jpg")

        # Thông báo thành công
        QMessageBox.information(self, "Thành công", "Đã cập nhật thông tin sinh viên.")

        # Cập nhật thông tin trong quản lý điểm danh
        self.quan_ly_diem_danh.load_student_info()

        # Cập nhật thông tin trong giao diện
        self.student_id = new_student_id
        self.student_name = new_student_name
        self.load_student_photo()  # Đây là dòng cuối cùng được hiển thị trong file gốc

        # Cập nhật lại bảng điểm danh sau khi thay đổi thông tin
        self.setup_attendance_table()

    def delete_student(self):
        """Xóa sinh viên khỏi hệ thống"""
        # Hiển thị hộp thoại xác nhận
        reply = QMessageBox.question(
            self,
            "Xác nhận xóa",
            f"Bạn có chắc chắn muốn xóa sinh viên {self.student_name} ({self.student_id})?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            # Xóa sinh viên khỏi file CSV
            temp_file = "students_temp.csv"
            deleted = False

            with open("students.csv", "r", newline="", encoding="utf-8") as csvfile, \
                    open(temp_file, "w", newline="", encoding="utf-8") as tempfile:
                reader = csv.reader(csvfile)
                writer = csv.writer(tempfile)

                for row in reader:
                    if len(row) >= 2 and row[0] == self.student_id:
                        deleted = True
                        continue  # Bỏ qua dòng này để xóa
                    writer.writerow(row)

            # Thay thế file cũ bằng file tạm
            os.replace(temp_file, "students.csv")

            # Xóa ảnh sinh viên nếu có
            image_path = f"ImagesAttendance/{self.student_id}.jpg"
            if os.path.exists(image_path):
                os.remove(image_path)

            # Cập nhật danh sách sinh viên trong quản lý điểm danh
            self.quan_ly_diem_danh.load_student_info()

            # Thông báo và đóng cửa sổ
            if deleted:
                QMessageBox.information(self, "Thành công", f"Đã xóa sinh viên {self.student_name}.")
            else:
                QMessageBox.warning(self, "Thông báo", f"Không tìm thấy sinh viên {self.student_id} trong hệ thống.")

            self.close()