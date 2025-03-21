class SinhVien:
    def __init__(self, ma_sv, ho_ten):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.danh_sach_diem_danh = []

    def them_diem_danh(self, thoi_gian, trang_thai):

        self.danh_sach_diem_danh.append({
            'thoi_gian': thoi_gian,
            'trang_thai': trang_thai
        })

    def lay_diem_danh_theo_ngay(self, ngay):

        return [dd for dd in self.danh_sach_diem_danh if dd['thoi_gian'].startswith(ngay)]

    def kiem_tra_diem_danh(self, ngay, trang_thai):
        for dd in self.danh_sach_diem_danh:
            if dd['thoi_gian'].startswith(ngay) and dd['trang_thai'] == trang_thai:
                return True
        return False

    def da_dang_ky_anh(self):
        import os
        return os.path.exists(f"ImagesAttendance/{self.ma_sv}.jpg")

    def __str__(self):
        return f"{self.ma_sv} - {self.ho_ten}"