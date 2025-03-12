import csv
import os

# Lấy đường dẫn đến file Attendance.csv
# Giả định script này nằm trong thư mục Statistic
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
csv_path = os.path.join(parent_dir, 'Face_Detection_PyQt_Final', 'Attendance.csv')

# Đọc và hiển thị nội dung của file CSV
with open(csv_path, newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    for row in reader:
        if len(row) >= 3:  # Đảm bảo có ít nhất 3 cột
            # In dữ liệu theo định dạng bảng
            print(f"{row[0]}\t{row[1]}\t{row[2]}")
        else:
            print("Định dạng hàng không hợp lệ:", row)