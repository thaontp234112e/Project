import csv
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import pandas as pd
from student import SinhVien

class QuanLyDiemDanh:
    def __init__(self):
        self.danh_sach_sinh_vien = {}
        self.load_student_info()

    def get_base_path(self):
        """Get the base path of the application"""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.dirname(current_dir)

    def load_student_info(self):
        base_path = self.get_base_path()
        students_csv_path = os.path.join(base_path, 'dataset', 'students.csv')
        
        if os.path.exists(students_csv_path):
            try:
                with open(students_csv_path, newline='', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    next(reader, None)
                    for row in reader:
                        if len(row) >= 2:
                            ma_sv = row[0]
                            ho_ten = row[1]
                            self.them_sinh_vien(ma_sv, ho_ten)
            except Exception as e:
                print(f"The error when reading the file student.csv: {e}")

    def them_sinh_vien(self, ma_sv, ho_ten):

        if ma_sv not in self.danh_sach_sinh_vien:
            self.danh_sach_sinh_vien[ma_sv] = SinhVien(ma_sv, ho_ten)
        return self.danh_sach_sinh_vien[ma_sv]

    def doc_tu_csv(self, duong_dan_file=None):
        if duong_dan_file is None:
            base_path = self.get_base_path()
            duong_dan_file = os.path.join(base_path, 'dataset', 'Attendance.csv')
            
        try:
            if not os.path.exists(duong_dan_file):
                with open(duong_dan_file, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(['StudentID', 'Time', 'Status'])
                return True

            with open(duong_dan_file, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader, None)

                for row in reader:
                    if len(row) >= 3:
                        ma_sv = row[0]
                        thoi_gian = row[1]
                        trang_thai = row[2]

                        sinh_vien = None
                        if ma_sv in self.danh_sach_sinh_vien:
                            sinh_vien = self.danh_sach_sinh_vien[ma_sv]
                        else:
                            ho_ten = self.tim_ten_sinh_vien(ma_sv)
                            sinh_vien = self.them_sinh_vien(ma_sv, ho_ten)

                        sinh_vien.them_diem_danh(thoi_gian, trang_thai)
            return True
        except Exception as e:
            print(f"The error when reading the CSV file: {e}")
            return False

    def tim_ten_sinh_vien(self, ma_sv):
        base_path = self.get_base_path()
        students_csv_path = os.path.join(base_path, 'dataset', 'students.csv')
        
        if os.path.exists(students_csv_path):
            try:
                with open(students_csv_path, newline='', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    next(reader, None)  # Skip the header
                    for row in reader:
                        if len(row) >= 2 and row[0] == ma_sv:
                            return row[1]
            except Exception as e:
                print(f"The error when searching for the student's name: {e}")
        return ma_sv

    def nhap_du_lieu_excel(self, duong_dan_file):

        try:
            df = pd.read_excel(duong_dan_file)

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

            for _, row in df.iterrows():
                ma_sv = str(row[student_id_col]).strip()
                ho_ten = str(row[fullname_col]).strip()
                if ma_sv and ho_ten:
                    self.them_sinh_vien(ma_sv, ho_ten)

            self.luu_danh_sach_sinh_vien()
            return True

        except Exception as e:
            print(f"The error when importing data from Excel: {e}")
            return False

    def luu_danh_sach_sinh_vien(self):
        base_path = self.get_base_path()
        students_csv_path = os.path.join(base_path, 'dataset', 'students.csv')
        
        try:
            with open(students_csv_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['StudentID', 'FullName'])

                for ma_sv, sinh_vien in self.danh_sach_sinh_vien.items():
                    writer.writerow([ma_sv, sinh_vien.ho_ten])

            return True
        except Exception as e:
            print(f"The error when saving the student list: {e}")
            return False

    def lay_danh_sach_sinh_vien(self):
        return list(self.danh_sach_sinh_vien.values())

    def lay_danh_sach_ngay(self):
        danh_sach_ngay = set()
        base_path = self.get_base_path()
        attendance_csv_path = os.path.join(base_path, 'dataset', 'Attendance.csv')
        
        if os.path.exists(attendance_csv_path):
            try:
                with open(attendance_csv_path, newline='', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    next(reader, None)  # Skip the header
                    for row in reader:
                        if len(row) >= 2:
                            thoi_gian = row[1]
                            ngay = thoi_gian.split()[0] if ' ' in thoi_gian else thoi_gian
                            danh_sach_ngay.add(ngay)
            except Exception as e:
                print(f"The error when reading the file Attendance.csv: {e}")
        return sorted(list(danh_sach_ngay), reverse=True)

    def loc_theo_ngay(self, ngay):
        ket_qua = []
        base_path = self.get_base_path()
        attendance_csv_path = os.path.join(base_path, 'dataset', 'Attendance.csv')
        
        if os.path.exists(attendance_csv_path):
            try:
                with open(attendance_csv_path, newline='', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    next(reader, None)
                    for row in reader:
                        if len(row) >= 3:
                            ma_sv = row[0]
                            thoi_gian = row[1]
                            trang_thai = row[2]

                            ngay_diem_danh = thoi_gian.split()[0] if ' ' in thoi_gian else thoi_gian

                            if ngay_diem_danh == ngay:
                                ho_ten = self.tim_ten_sinh_vien(ma_sv)

                                ket_qua.append({
                                    'ma_sv': ma_sv,
                                    'ho_ten': ho_ten,
                                    'thoi_gian': thoi_gian,
                                    'trang_thai': trang_thai
                                })
            except Exception as e:
                print(f"The error when reading the Attendance.csv file: {e}")
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

        try:
            import csv
            import pandas as pd

            df = pd.read_csv(file_path, encoding='utf-8')

            danh_sach_sv = []

            for _, row in df.iterrows():
                sv_data = {
                    'ma_sv': str(row['ma_sv']),
                    'ho_ten': row['ho_ten']
                }
                danh_sach_sv.append(sv_data)

            for ngay in self.lay_danh_sach_ngay():
                self.cap_nhat_danh_sach_lop(ngay, danh_sach_sv)

            return True
        except Exception as e:
            print(f"The error when reading the CSV file: {str(e)}")
            return False