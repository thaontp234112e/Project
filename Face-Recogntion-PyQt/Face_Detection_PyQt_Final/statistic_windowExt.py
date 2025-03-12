import os
import sys
from datetime import datetime
import matplotlib

matplotlib.use('QtAgg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QTableWidgetItem,
                             QHeaderView, QMessageBox, QApplication)
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QColor, QBrush
from statistic_window import Ui_StatisticsDialog


class MplCanvas(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)
        self.fig.tight_layout()


class Ui_StatisticDialog(QDialog, Ui_StatisticsDialog):
    def __init__(self, quan_ly_diem_danh):
        super(Ui_StatisticDialog, self).__init__()
        self.setupUi(self)
        self.quan_ly_diem_danh = quan_ly_diem_danh

        # Initialize variables
        self.attendance_chart = None
        self.time_chart = None

        # Set up date range
        danh_sach_ngay = self.quan_ly_diem_danh.lay_danh_sach_ngay()
        if danh_sach_ngay:
            # Set default date range (all available dates)
            start_date = self.parse_date(danh_sach_ngay[-1])  # Oldest date
            end_date = self.parse_date(danh_sach_ngay[0])  # Newest date

            self.dateEditStart.setDate(start_date)
            self.dateEditEnd.setDate(end_date)
        else:
            # Use current date if no attendance data
            today = QDate.currentDate()
            self.dateEditStart.setDate(today.addDays(-30))  # Last 30 days
            self.dateEditEnd.setDate(today)

        # Connect signals
        self.pushButtonGenerate.clicked.connect(self.generate_statistics)
        self.pushButtonClose.clicked.connect(self.close)

        # Initial statistics generation
        self.generate_statistics()

    def parse_date(self, date_str):
        """
        Parse a date string in format 'YY/MM/DD' to QDate.
        """
        try:
            if '/' in date_str:
                year, month, day = map(int, date_str.split('/'))
                # Adjust year if it's in 2-digit format
                if year < 100:
                    year += 2000 if year < 30 else 1900  # Assuming 20xx for years < 30, 19xx otherwise
                return QDate(year, month, day)
        except Exception as e:
            print(f"Error parsing date: {e}")

        # Return current date as fallback
        return QDate.currentDate()

    def format_date(self, qdate):
        """
        Format QDate to 'YY/MM/DD' format for consistency with the attendance data.
        """
        year = qdate.year() % 100  # Get last two digits of year
        return f"{year:02d}/{qdate.month():02d}/{qdate.day():02d}"

    def generate_statistics(self):
        """
        Generate and display statistics based on selected date range.
        """
        start_date = self.dateEditStart.date()
        end_date = self.dateEditEnd.date()

        if start_date > end_date:
            QMessageBox.warning(self, "Invalid Date Range",
                                "Start date cannot be after end date.")
            return

        # Convert QDate to string format used in attendance data
        start_date_str = self.format_date(start_date)
        end_date_str = self.format_date(end_date)

        # Get all dates in the selected range
        all_dates = self.get_dates_in_range(start_date_str, end_date_str)

        if not all_dates:
            QMessageBox.information(self, "No Data",
                                    "No attendance data found for the selected date range.")
            return

        # Generate statistics
        self.generate_attendance_rate_chart(all_dates)
        self.generate_time_distribution_chart(all_dates)
        self.generate_student_report(all_dates)

    def get_dates_in_range(self, start_date, end_date):
        """
        Get all dates from attendance data that fall within the given range.
        """
        all_dates = self.quan_ly_diem_danh.lay_danh_sach_ngay()

        # Filter dates that are within the range
        filtered_dates = []
        for date_str in all_dates:
            # Compare dates by parsing them and creating datetime objects
            try:
                date_parts = date_str.split('/')
                if len(date_parts) >= 3:
                    year = int(date_parts[0])
                    if year < 100:  # 2-digit year
                        year += 2000 if year < 30 else 1900
                    month = int(date_parts[1])
                    day = int(date_parts[2])
                    current_date = datetime(year, month, day)

                    # Parse start and end dates
                    start_parts = start_date.split('/')
                    end_parts = end_date.split('/')

                    start_year = int(start_parts[0])
                    if start_year < 100:
                        start_year += 2000 if start_year < 30 else 1900
                    start_month = int(start_parts[1])
                    start_day = int(start_parts[2])
                    start_datetime = datetime(start_year, start_month, start_day)

                    end_year = int(end_parts[0])
                    if end_year < 100:
                        end_year += 2000 if end_year < 30 else 1900
                    end_month = int(end_parts[1])
                    end_day = int(end_parts[2])
                    end_datetime = datetime(end_year, end_month, end_day)

                    if start_datetime <= current_date <= end_datetime:
                        filtered_dates.append(date_str)
            except Exception as e:
                print(f"Error processing date {date_str}: {e}")

        return filtered_dates

    def generate_attendance_rate_chart(self, dates):
        """
        Generate chart showing attendance rate by date.
        """
        # Clear previous chart if exists
        if self.attendance_chart:
            layout = self.widgetAttendanceRate.layout()
            if layout:
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.deleteLater()
            else:
                layout = QVBoxLayout(self.widgetAttendanceRate)
                self.widgetAttendanceRate.setLayout(layout)

        # Create new chart
        self.attendance_chart = MplCanvas(width=8, height=4, dpi=100)

        # Prepare data
        attendance_dates = []
        attendance_rates = []

        # Sort dates chronologically
        dates.sort(key=lambda x: datetime.strptime(x, '%y/%m/%d') if len(x.split('/')) >= 3 else datetime.now())

        for date in dates:
            stats = self.quan_ly_diem_danh.thong_ke_diem_danh()
            for day_stat in stats['theo_ngay']:
                if day_stat['ngay'] == date:
                    attendance_dates.append(date)
                    attendance_rates.append(day_stat['ti_le'])
                    break

        # Plot data
        if attendance_dates:
            self.attendance_chart.axes.bar(attendance_dates, attendance_rates, color='skyblue')
            self.attendance_chart.axes.set_xlabel('Date')
            self.attendance_chart.axes.set_ylabel('Attendance Rate (%)')
            self.attendance_chart.axes.set_title('Attendance Rate by Date')

            # Rotate x-axis labels for better readability
            self.attendance_chart.axes.set_xticklabels(attendance_dates, rotation=45, ha='right')

            # Add percentage values above bars
            for i, v in enumerate(attendance_rates):
                self.attendance_chart.axes.text(i, v + 2, f"{v}%", ha='center')

            # Set y-axis limit to 110% to have space for labels
            self.attendance_chart.axes.set_ylim(0, 110)

            self.attendance_chart.fig.tight_layout()

        # Add chart to layout
        layout = self.widgetAttendanceRate.layout()
        layout.addWidget(self.attendance_chart)

    def generate_time_distribution_chart(self, dates):
        """
        Generate chart showing distribution of check-in times.
        """
        # Clear previous chart if exists
        if self.time_chart:
            layout = self.widgetTimeDistribution.layout()
            if layout:
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.deleteLater()
            else:
                layout = QVBoxLayout(self.widgetTimeDistribution)
                self.widgetTimeDistribution.setLayout(layout)

        # Create new chart
        self.time_chart = MplCanvas(width=8, height=4, dpi=100)

        # Collect check-in times
        times = []

        # Read Attendance.csv to get times
        if os.path.exists('Attendance.csv'):
            try:
                import csv
                with open('Attendance.csv', newline='', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    next(reader, None)  # Skip header

                    for row in reader:
                        if len(row) >= 3 and row[2] == 'Clock In':
                            time_str = row[1]
                            date_part = time_str.split()[0] if ' ' in time_str else ""

                            if date_part in dates:
                                # Extract hour:minute
                                if ' ' in time_str and ':' in time_str.split()[1]:
                                    time_parts = time_str.split()[1].split(':')
                                    if len(time_parts) >= 2:
                                        hour = int(time_parts[0])
                                        minute = int(time_parts[1])
                                        # Convert to decimal hours for easier plotting
                                        times.append(hour + minute / 60)
            except Exception as e:
                print(f"Error reading attendance data: {e}")

        if times:
            # Plot histogram of check-in times
            self.time_chart.axes.hist(times, bins=24, range=(0, 24), edgecolor='black', alpha=0.7, color='lightgreen')
            self.time_chart.axes.set_xlabel('Time of Day (24-hour format)')
            self.time_chart.axes.set_ylabel('Number of Check-ins')
            self.time_chart.axes.set_title('Distribution of Check-in Times')

            # Set x-axis ticks to represent hours
            self.time_chart.axes.set_xticks(range(0, 24, 2))
            self.time_chart.axes.set_xlim(0, 24)

            self.time_chart.fig.tight_layout()

        # Add chart to layout
        layout = self.widgetTimeDistribution.layout()
        layout.addWidget(self.time_chart)

    def generate_student_report(self, dates):
        """
        Generate detailed report of student attendance for the selected date range.
        """
        # Get student attendance data
        stats = self.quan_ly_diem_danh.thong_ke_diem_danh()
        student_stats = stats['theo_sv']

        # Configure table
        self.tableWidgetReport.clearContents()
        self.tableWidgetReport.setRowCount(0)
        self.tableWidgetReport.setColumnCount(6)
        self.tableWidgetReport.setHorizontalHeaderLabels([
            "MSSV", "Họ tên", "Số buổi tham gia", "Tổng số buổi",
            "Tỷ lệ tham gia (%)", "Đã đăng ký ảnh"
        ])

        # Resize columns
        header = self.tableWidgetReport.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)

        # Fill table with data
        for row, student in enumerate(student_stats):
            self.tableWidgetReport.insertRow(row)

            # Calculate attendance for selected date range
            total_days = len(dates)
            attended_days = 0

            for date in dates:
                if self.quan_ly_diem_danh.danh_sach_sinh_vien.get(student['ma_sv']):
                    if self.quan_ly_diem_danh.danh_sach_sinh_vien[student['ma_sv']].kiem_tra_diem_danh(date,
                                                                                                       'Clock In'):
                        attended_days += 1

            attendance_rate = round((attended_days / total_days * 100), 2) if total_days > 0 else 0

            # Add data to table
            self.tableWidgetReport.setItem(row, 0, QTableWidgetItem(student['ma_sv']))
            self.tableWidgetReport.setItem(row, 1, QTableWidgetItem(student['ho_ten']))
            self.tableWidgetReport.setItem(row, 2, QTableWidgetItem(str(attended_days)))
            self.tableWidgetReport.setItem(row, 3, QTableWidgetItem(str(total_days)))
            self.tableWidgetReport.setItem(row, 4, QTableWidgetItem(f"{attendance_rate}%"))
            self.tableWidgetReport.setItem(row, 5, QTableWidgetItem("Có" if student['da_dang_ky_anh'] else "Không"))

            # Highlight students with low attendance or missing photos
            for col in range(6):
                if not student['da_dang_ky_anh']:
                    self.tableWidgetReport.item(row, col).setBackground(QBrush(QColor(255, 200, 200)))  # Red
                elif attendance_rate < 50:
                    self.tableWidgetReport.item(row, col).setBackground(QBrush(QColor(255, 255, 200)))  # Yellow

if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication
    from attendance_manager import QuanLyDiemDanh

    # Khởi tạo ứng dụng PyQt6
    app = QApplication(sys.argv)

    # Tạo đối tượng quản lý điểm danh từ class QuanLyDiemDanh
    quan_ly_diem_danh = QuanLyDiemDanh()

    # Tạo và hiển thị cửa sổ thống kê
    window = Ui_StatisticDialog(quan_ly_diem_danh)
    window.show()

    # Chạy vòng lặp sự kiện
    sys.exit(app.exec())
