# File: attendance_manager.py
import csv
import os
import pandas as pd
from student import SinhVien

class QuanLyDiemDanh:
    def __init__(self):
        self.danh_sach_sinh_vien = {}  # Dictionary với key là mã sinh viên, value là đối tượng SinhVien
        self.load_student_info()

    def load_student_info(self):
        if os.path.exists('students.csv'):
            try:
                with open('students.csv', newline='', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    # Always skip the first row (header)
                    next(reader, None)
                    for row in reader:
                        if len(row) >= 2:
                            ma_sv = row[0]
                            ho_ten = row[1]
                            self.them_sinh_vien(ma_sv, ho_ten)
            except Exception as e:
                print(f"Lỗi khi đọc file student.csv: {e}")

    def them_sinh_vien(self, ma_sv, ho_ten):
        """
        Thêm một sinh viên mới vào danh sách hoặc trả về sinh viên đã tồn tại.

        Args:
            ma_sv (str): Mã số sinh viên
            ho_ten (str): Họ và tên sinh viên

        Returns:
            SinhVien: Đối tượng SinhVien đã thêm hoặc đã tồn tại
        """
        if ma_sv not in self.danh_sach_sinh_vien:
            self.danh_sach_sinh_vien[ma_sv] = SinhVien(ma_sv, ho_ten)
        return self.danh_sach_sinh_vien[ma_sv]

    def doc_tu_csv(self, duong_dan_file):
        """
        Đọc dữ liệu điểm danh từ file CSV.

        Args:
            duong_dan_file (str): Đường dẫn đến file CSV

        Returns:
            bool: True nếu đọc thành công, False nếu có lỗi
        """
        try:
            # Nếu file không tồn tại, tạo mới file với header
            if not os.path.exists(duong_dan_file):
                with open(duong_dan_file, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(['StudentID', 'Time', 'Status'])
                return True

            with open(duong_dan_file, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader, None)  # Skip header if exists

                for row in reader:
                    if len(row) >= 3:
                        ma_sv = row[0]
                        thoi_gian = row[1]
                        trang_thai = row[2]

                        # Tìm sinh viên trong danh sách hoặc tạo mới
                        sinh_vien = None
                        if ma_sv in self.danh_sach_sinh_vien:
                            sinh_vien = self.danh_sach_sinh_vien[ma_sv]
                        else:
                            # Tìm thông tin tên sinh viên từ students.csv
                            ho_ten = self.tim_ten_sinh_vien(ma_sv)
                            sinh_vien = self.them_sinh_vien(ma_sv, ho_ten)

                        # Thêm thông tin điểm danh
                        sinh_vien.them_diem_danh(thoi_gian, trang_thai)
            return True
        except Exception as e:
            print(f"Lỗi khi đọc file CSV: {e}")
            return False

    def tim_ten_sinh_vien(self, ma_sv):
        """
        Tìm tên sinh viên từ mã số sinh viên.

        Args:
            ma_sv (str): Mã số sinh viên

        Returns:
            str: Tên sinh viên hoặc mã sinh viên nếu không tìm thấy
        """
        if os.path.exists('students.csv'):
            try:
                with open('students.csv', newline='', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    next(reader, None)  # Skip the header
                    for row in reader:
                        if len(row) >= 2 and row[0] == ma_sv:
                            return row[1]
            except Exception as e:
                print(f"Lỗi khi tìm tên sinh viên: {e}")
        return ma_sv  # Trả về mã sinh viên nếu không tìm thấy

    def nhap_du_lieu_excel(self, duong_dan_file):
        """
        Nhập danh sách sinh viên từ file Excel.

        Args:
            duong_dan_file (str): Đường dẫn đến file Excel

        Returns:
            bool: True nếu nhập thành công, False nếu có lỗi
        """
        try:
            df = pd.read_excel(duong_dan_file)

            # Kiểm tra và xác định tên cột
            student_id_col = None
            fullname_col = None

            for col in df.columns:
                col_lower = col.lower()
                if col_lower in ["studentid", "student_id", "ma_sv", "masv", "ma sv", "id"]:
                    student_id_col = col
                elif col_lower in ["fullname", "full_name", "ho_ten", "hoten", "ho ten", "name"]:
                    fullname_col = col

            if not student_id_col or not fullname_col:
                return False

            # Tạo danh sách sinh viên mới
            for _, row in df.iterrows():
                ma_sv = str(row[student_id_col]).strip()
                ho_ten = str(row[fullname_col]).strip()
                if ma_sv and ho_ten:
                    self.them_sinh_vien(ma_sv, ho_ten)

            # Lưu danh sách sinh viên
            self.luu_danh_sach_sinh_vien()
            return True

        except Exception as e:
            print(f"Lỗi khi nhập dữ liệu từ Excel: {e}")
            return False

    def luu_danh_sach_sinh_vien(self):
        try:
            with open('students.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['StudentID', 'FullName'])

                for ma_sv, sinh_vien in self.danh_sach_sinh_vien.items():
                    writer.writerow([ma_sv, sinh_vien.ho_ten])

            return True
        except Exception as e:
            print(f"Lỗi khi lưu danh sách sinh viên: {e}")
            return False

    def lay_danh_sach_sinh_vien(self):
        return list(self.danh_sach_sinh_vien.values())

    def lay_danh_sach_ngay(self):
        danh_sach_ngay = set()
        if os.path.exists('Attendance.csv'):
            try:
                with open('Attendance.csv', newline='', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    next(reader, None)  # Skip the header
                    for row in reader:
                        if len(row) >= 2:
                            thoi_gian = row[1]
                            ngay = thoi_gian.split()[0] if ' ' in thoi_gian else thoi_gian
                            danh_sach_ngay.add(ngay)
            except Exception as e:
                print(f"Lỗi khi đọc file Attendance.csv: {e}")
        return sorted(list(danh_sach_ngay), reverse=True)

    def loc_theo_ngay(self, ngay):
        ket_qua = []
        if os.path.exists('Attendance.csv'):
            try:
                with open('Attendance.csv', newline='', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    next(reader, None)  # Skip the header
                    for row in reader:
                        if len(row) >= 3:
                            ma_sv = row[0]
                            thoi_gian = row[1]
                            trang_thai = row[2]

                            # Trích xuất ngày từ chuỗi thời gian
                            ngay_diem_danh = thoi_gian.split()[0] if ' ' in thoi_gian else thoi_gian

                            if ngay_diem_danh == ngay:
                                # Tìm tên sinh viên
                                ho_ten = self.tim_ten_sinh_vien(ma_sv)

                                ket_qua.append({
                                    'ma_sv': ma_sv,
                                    'ho_ten': ho_ten,
                                    'thoi_gian': thoi_gian,
                                    'trang_thai': trang_thai
                                })
            except Exception as e:
                print(f"Lỗi khi đọc file Attendance.csv: {e}")
        return ket_qua

    def lay_danh_sach_diem_danh_lop(self, ngay):
        danh_sach_sv = self.lay_danh_sach_sinh_vien()
        danh_sach_diem_danh = self.loc_theo_ngay(ngay)
        dict_diem_danh = {}
        for item in danh_sach_diem_danh:
            ma_sv = item['ma_sv']
            if ma_sv not in dict_diem_danh:
                dict_diem_danh[ma_sv] = []
            dict_diem_danh[ma_sv].append(item)
        ket_qua = []
        for sv in danh_sach_sv:
            if sv.ma_sv in dict_diem_danh:
                for diem_danh in dict_diem_danh[sv.ma_sv]:
                    ket_qua.append(diem_danh)
            else:
                diem_danh_item = {
                    'ma_sv': sv.ma_sv,
                    'ho_ten': sv.ho_ten,
                    'thoi_gian': '',
                    'trang_thai': 'Chưa điểm danh',
                    'da_dang_ky_anh': sv.da_dang_ky_anh()
                }
                ket_qua.append(diem_danh_item)

        return ket_qua

    def thong_ke_diem_danh(self):
        danh_sach_ngay = self.lay_danh_sach_ngay()
        thong_ke_theo_ngay = []
        tong_so_sv = len(self.danh_sach_sinh_vien)

        for ngay in danh_sach_ngay:
            danh_sach_diem_danh = self.loc_theo_ngay(ngay)
            sv_da_diem_danh = set()
            for item in danh_sach_diem_danh:
                if item['trang_thai'] == 'Clock In':
                    sv_da_diem_danh.add(item['ma_sv'])

            so_sv_diem_danh = len(sv_da_diem_danh)
            ti_le = 0 if tong_so_sv == 0 else (so_sv_diem_danh / tong_so_sv) * 100

            thong_ke_theo_ngay.append({
                'ngay': ngay,
                'so_sv_diem_danh': so_sv_diem_danh,
                'tong_so_sv': tong_so_sv,
                'ti_le': round(ti_le, 2)
            })
        thong_ke_theo_sv = []
        for ma_sv, sv in self.danh_sach_sinh_vien.items():
            so_buoi_diem_danh = 0
            for ngay in danh_sach_ngay:
                if sv.kiem_tra_diem_danh(ngay, 'Clock In'):
                    so_buoi_diem_danh += 1

            ti_le = 0 if len(danh_sach_ngay) == 0 else (so_buoi_diem_danh / len(danh_sach_ngay)) * 100

            thong_ke_theo_sv.append({
                'ma_sv': ma_sv,
                'ho_ten': sv.ho_ten,
                'so_buoi_diem_danh': so_buoi_diem_danh,
                'tong_so_buoi': len(danh_sach_ngay),
                'ti_le': round(ti_le, 2),
                'da_dang_ky_anh': sv.da_dang_ky_anh()
            })
        thong_ke_theo_sv.sort(key=lambda x: x['ti_le'], reverse=True)
        return {
            'theo_ngay': thong_ke_theo_ngay,
            'theo_sv': thong_ke_theo_sv,
            'tong_so_sv': tong_so_sv,
            'tong_so_ngay': len(danh_sach_ngay)
        }

    def nhap_du_lieu_csv(self, file_path):
        """
        Nhập dữ liệu sinh viên từ file CSV và cập nhật danh sách lớp
        """
        try:
            import csv
            import pandas as pd

            # Read CSV data
            df = pd.read_csv(file_path, encoding='utf-8')

            # Create a list to store student data
            danh_sach_sv = []

            # Process each row
            for _, row in df.iterrows():
                sv_data = {
                    'ma_sv': str(row['ma_sv']),
                    'ho_ten': row['ho_ten']
                }
                danh_sach_sv.append(sv_data)

            # Update the class list for each date
            for ngay in self.lay_danh_sach_ngay():
                self.cap_nhat_danh_sach_lop(ngay, danh_sach_sv)

            return True
        except Exception as e:
            print(f"Lỗi khi đọc file CSV: {str(e)}")
            return False