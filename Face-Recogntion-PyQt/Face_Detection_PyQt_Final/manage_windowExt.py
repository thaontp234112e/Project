# File: manage_windowExt.py
import os
import sys
from PyQt6.QtWidgets import (QDialog, QApplication, QPushButton, QTableWidgetItem,
                             QHeaderView, QFileDialog, QMessageBox, QTableWidget)
from PyQt6.QtGui import QColor, QBrush
from PyQt6.uic import loadUi
from attendance_manager import QuanLyDiemDanh
from statistic_windowExt import Ui_StatisticDialog


class Ui_ManageDialog(QDialog):
    def __init__(self):
        super(Ui_ManageDialog, self).__init__()
        loadUi("manage_window.ui", self)
        self.quan_ly_diem_danh = QuanLyDiemDanh()
        self.quan_ly_diem_danh.doc_tu_csv('Attendance.csv')
        self.pushButtonClose.clicked.connect(self.close)
        self.pushButtonImport.clicked.connect(self.import_excel)
        self.pushButtonStatistic.clicked.connect(self.open_statistic)
        self.pushButtonShowAll.clicked.connect(self.hien_thi_tat_ca_sinh_vien)
        self.thiet_lap_bang()
        self.hien_thi_danh_sach_ngay()
        self.selected_date = None
        if self.quan_ly_diem_danh.lay_danh_sach_ngay():
            self.selected_date = self.quan_ly_diem_danh.lay_danh_sach_ngay()[0]

    def thiet_lap_bang(self):
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["Mã SV", "Họ tên", "Thời gian", "Trạng thái", "Đã đăng ký ảnh"])
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)

    def hien_thi_danh_sach_ngay(self):
        # Clear existing buttons
        for i in reversed(range(self.dateButtonLayout.count())):
            widget = self.dateButtonLayout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        danh_sach_ngay = self.quan_ly_diem_danh.lay_danh_sach_ngay()
        # Sort the dates to display newest first
        danh_sach_ngay.sort(reverse=True)

        for ngay in danh_sach_ngay:
            button = QPushButton(ngay)
            button.setMinimumHeight(30)
            button.clicked.connect(lambda checked, n=ngay: self.hien_thi_diem_danh_theo_ngay(n))
            self.dateButtonLayout.addWidget(button)

        if danh_sach_ngay:
            self.hien_thi_diem_danh_theo_ngay(danh_sach_ngay[0])

    def hien_thi_diem_danh_theo_ngay(self, ngay):
        self.selected_date = ngay
        self.label_selected_date.setText(f"Ngày: {ngay}")
        danh_sach_diem_danh = self.quan_ly_diem_danh.loc_theo_ngay(ngay)
        self.tableWidget.setRowCount(len(danh_sach_diem_danh))

        for row, item in enumerate(danh_sach_diem_danh):
            # Set basic data
            self.tableWidget.setItem(row, 0, QTableWidgetItem(item['ma_sv']))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item['ho_ten']))

            # Extract time from datetime if available
            thoi_gian_parts = item['thoi_gian'].split() if 'thoi_gian' in item and item['thoi_gian'] else ["", ""]
            if len(thoi_gian_parts) > 1:
                thoi_gian_hien_thi = thoi_gian_parts[1]
            else:
                thoi_gian_hien_thi = item.get('thoi_gian', '')

            self.tableWidget.setItem(row, 2, QTableWidgetItem(thoi_gian_hien_thi))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(item.get('trang_thai', 'Chưa điểm danh')))

            # Check if student has registered a photo
            ma_sv = item['ma_sv']
            da_dang_ky_anh = os.path.exists(f"ImagesAttendance/{ma_sv}.jpg")
            item_dang_ky = QTableWidgetItem("Có" if da_dang_ky_anh else "Không")
            self.tableWidget.setItem(row, 4, item_dang_ky)

            # Highlight rows based on status
            for col in range(5):
                cell_item = self.tableWidget.item(row, col)
                if not da_dang_ky_anh:
                    cell_item.setBackground(QBrush(QColor(255, 200, 200)))  # Red for no photo

    def hien_thi_tat_ca_sinh_vien(self):
        if self.selected_date is None:
            QMessageBox.warning(self, "Cảnh báo", "Chưa có ngày điểm danh nào.")
            return

        danh_sach_sv = self.quan_ly_diem_danh.lay_danh_sach_diem_danh_lop(self.selected_date)
        self.tableWidget.setRowCount(len(danh_sach_sv))

        for row, item in enumerate(danh_sach_sv):
            # Set basic student info
            self.tableWidget.setItem(row, 0, QTableWidgetItem(item['ma_sv']))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item['ho_ten']))

            # Extract time if available
            thoi_gian = item.get('thoi_gian', '')
            thoi_gian_parts = thoi_gian.split() if thoi_gian else []
            if len(thoi_gian_parts) > 1:
                thoi_gian_hien_thi = thoi_gian_parts[1]
            else:
                thoi_gian_hien_thi = thoi_gian

            self.tableWidget.setItem(row, 2, QTableWidgetItem(thoi_gian_hien_thi))

            # Set attendance status
            trang_thai = item.get('trang_thai', 'Chưa điểm danh')
            self.tableWidget.setItem(row, 3, QTableWidgetItem(trang_thai))

            # Check if student has a registered photo
            ma_sv = item['ma_sv']
            da_dang_ky_anh = os.path.exists(f"ImagesAttendance/{ma_sv}.jpg")
            item_dang_ky = QTableWidgetItem("Có" if da_dang_ky_anh else "Không")
            self.tableWidget.setItem(row, 4, item_dang_ky)

            # Highlight rows based on status
            for col in range(5):
                cell_item = self.tableWidget.item(row, col)
                if not da_dang_ky_anh:
                    cell_item.setBackground(QBrush(QColor(255, 200, 200)))  # Red for no photo
                elif trang_thai == 'Chưa điểm danh':
                    cell_item.setBackground(QBrush(QColor(255, 255, 200)))  # Yellow for not attended

    def import_excel(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            self, "Chọn file Excel", "", "Excel Files (*.xlsx *.xls)"
        )
        if file_path:
            success = self.quan_ly_diem_danh.nhap_du_lieu_excel(file_path)

            if success:
                QMessageBox.information(self, "Thành công", "Đã nhập dữ liệu sinh viên từ file Excel.")
                if self.selected_date:
                    self.hien_thi_tat_ca_sinh_vien()
            else:
                QMessageBox.warning(self, "Lỗi", "Không thể nhập dữ liệu từ file Excel.")

    def open_statistic(self):
        statistic_dialog = Ui_StatisticDialog(self.quan_ly_diem_danh)
        statistic_dialog.exec()


def main():
    app = QApplication(sys.argv)
    window = Ui_ManageDialog()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()