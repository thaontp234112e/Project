import csv
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
csv_path = os.path.join(parent_dir, 'dataset', 'Attendance.csv')

with open(csv_path, newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    for row in reader:
        if len(row) >= 3:
            print(f"{row[0]}\t{row[1]}\t{row[2]}")
        else:
            print("Định dạng hàng không hợp lệ:", row)