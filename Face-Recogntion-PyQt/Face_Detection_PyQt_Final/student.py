# File: student.py
class SinhVien:
    """
    Lớp SinhVien lưu trữ thông tin về một sinh viên và các lần điểm danh của sinh viên đó.
    """

    def __init__(self, ma_sv, ho_ten):
        """
        Khởi tạo một đối tượng SinhVien.

        Args:
            ma_sv (str): Mã số sinh viên
            ho_ten (str): Họ và tên sinh viên
        """
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.danh_sach_diem_danh = []  # Danh sách các lần điểm danh

    def them_diem_danh(self, thoi_gian, trang_thai):
        """
        Thêm một lần điểm danh mới vào danh sách điểm danh của sinh viên.

        Args:
            thoi_gian (str): Thời gian điểm danh (định dạng: 'yy/mm/dd HH:MM:SS')
            trang_thai (str): Trạng thái điểm danh ('Clock In' hoặc 'Clock Out')
        """
        self.danh_sach_diem_danh.append({
            'thoi_gian': thoi_gian,
            'trang_thai': trang_thai
        })

    def lay_diem_danh_theo_ngay(self, ngay):
        """
        Lấy danh sách điểm danh của sinh viên theo ngày cụ thể.

        Args:
            ngay (str): Ngày cần lọc (định dạng: 'yy/mm/dd')

        Returns:
            list: Danh sách các lần điểm danh trong ngày đó
        """
        return [dd for dd in self.danh_sach_diem_danh if dd['thoi_gian'].startswith(ngay)]

    def kiem_tra_diem_danh(self, ngay, trang_thai):
        """
        Kiểm tra xem sinh viên đã điểm danh với trạng thái cụ thể trong ngày hay chưa.

        Args:
            ngay (str): Ngày cần kiểm tra (định dạng: 'yy/mm/dd')
            trang_thai (str): Trạng thái điểm danh ('Clock In' hoặc 'Clock Out')

        Returns:
            bool: True nếu đã điểm danh, False nếu chưa
        """
        for dd in self.danh_sach_diem_danh:
            if dd['thoi_gian'].startswith(ngay) and dd['trang_thai'] == trang_thai:
                return True
        return False

    def da_dang_ky_anh(self):
        """
        Kiểm tra xem sinh viên đã đăng ký ảnh hay chưa.

        Returns:
            bool: True nếu đã đăng ký ảnh, False nếu chưa
        """
        import os
        return os.path.exists(f"ImagesAttendance/{self.ma_sv}.jpg")

    def __str__(self):
        """
        Trả về biểu diễn chuỗi của đối tượng SinhVien.

        Returns:
            str: Biểu diễn chuỗi của đối tượng SinhVien
        """
        return f"{self.ma_sv} - {self.ho_ten}"