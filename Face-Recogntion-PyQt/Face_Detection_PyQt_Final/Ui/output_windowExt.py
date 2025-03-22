from PyQt6.QtGui import QImage, QPixmap
from PyQt6.uic import loadUi
from PyQt6.QtCore import pyqtSlot, QTimer, QDate, Qt
from PyQt6.QtWidgets import QDialog, QMessageBox
import cv2
import face_recognition
import numpy as np
import datetime
import os
import csv


class Ui_OutputDialog(QDialog):
    def __init__(self):
        super(Ui_OutputDialog, self).__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.base_dir = os.path.dirname(current_dir)
        ui_file = os.path.join(current_dir, "output_window.ui")
        loadUi(ui_file, self)

        now = QDate.currentDate()
        current_date = now.toString('ddd dd MMMM yyyy')
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.Date_Label.setText(current_date)
        self.Time_Label.setText(current_time)

        # Kết nối các nút với chức năng mới
        self.pushButtonManage.clicked.connect(self.open_login_window)
        self.pushButtonRegist.clicked.connect(self.open_register_window)

        self.image = None

    def open_login_window(self):
        from login_windowExt import LoginWindow
        self.login_window = LoginWindow(self)
        self.login_window.show()

    def handle_successful_login(self):
        # This method will be called when login is successful
        self.open_manage_window()

    def open_manage_window(self):
        from manage_windowExt import Ui_ManageDialog
        self.hide()  # Ẩn cửa sổ output hiện tại
        self.manage_dialog = Ui_ManageDialog()
        # Khi cửa sổ manage đóng, hiển thị lại cửa sổ output
        self.manage_dialog.exec()
        self.show()  # Hiển thị lại cửa sổ output

    def open_register_window(self):
        from register_windowExt import Ui_RegisterDialog
        self.hide()  # Ẩn cửa sổ output hiện tại
        self.register_dialog = Ui_RegisterDialog()
        # Khi cửa sổ register đóng, hiển thị lại cửa sổ output
        self.register_dialog.exec()
        self.show()  # Hiển thị lại cửa sổ output

    @pyqtSlot()
    def startVideo(self, camera_name):
        if len(camera_name) == 1:
            self.capture = cv2.VideoCapture(int(camera_name))
        else:
            self.capture = cv2.VideoCapture(camera_name)
        self.timer = QTimer(self)
        
        # Get absolute path for ImagesAttendance directory
        path = os.path.join(self.base_dir, 'ImagesAttendance')
        
        if not os.path.exists(path):
            os.mkdir(path)
        images = []
        self.class_names = []
        self.encode_list = []
        self.TimeList1 = []
        self.TimeList2 = []
        attendance_list = os.listdir(path)

        for cl in attendance_list:
            cur_img = cv2.imread(f'{path}/{cl}')
            images.append(cur_img)
            self.class_names.append(os.path.splitext(cl)[0])
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            boxes = face_recognition.face_locations(img)
            encodes_cur_frame = face_recognition.face_encodings(img, boxes)[0]
            self.encode_list.append(encodes_cur_frame)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(10)

    def face_rec_(self, frame, encode_list_known, class_names):

        def mark_attendance(name):
            # Get absolute path for Attendance.csv file
            attendance_path = os.path.join(self.base_dir, 'dataset', 'Attendance.csv')

            if self.pushButtonIn.isChecked():
                self.pushButtonOut.setEnabled(False)
                with open(attendance_path, 'a') as f:
                    if (name != 'unknown'):
                        buttonReply = QMessageBox.question(self, 'Welcome ' + name, 'Are you Clocking In?',
                                                           QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                                           QMessageBox.StandardButton.No)
                        if buttonReply == QMessageBox.StandardButton.Yes:
                            date_time_string = datetime.datetime.now().strftime("%y/%m/%d %H:%M:%S")
                            f.writelines(f'\n{name},{date_time_string},Clock In')
                            self.pushButtonIn.setChecked(False)

                            self.NameLabel.setText(name)
                            self.StatusLabel.setText('Clocked In')
                            self.HoursLabel.setText('Measuring')
                            self.MinLabel.setText('')

                            self.Time1 = datetime.datetime.now()

                            self.pushButtonIn.setEnabled(True)
                        else:
                            print('Not clicked.')
                            self.pushButtonIn.setEnabled(True)
            elif self.pushButtonOut.isChecked():
                self.pushButtonOut.setEnabled(False)
                with open(attendance_path, 'a') as f:
                    if (name != 'unknown'):
                        buttonReply = QMessageBox.question(self, 'Cheers ' + name, 'Are you Clocking Out?',
                                                           QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                                           QMessageBox.StandardButton.No)
                        if buttonReply == QMessageBox.StandardButton.Yes:
                            date_time_string = datetime.datetime.now().strftime("%y/%m/%d %H:%M:%S")
                            f.writelines(f'\n{name},{date_time_string},Clock Out')
                            self.pushButtonOut.setChecked(False)

                            self.NameLabel.setText(name)
                            self.StatusLabel.setText('Clocked Out')
                            self.Time2 = datetime.datetime.now()

                            self.ElapseList(name)
                            self.TimeList2.append(datetime.datetime.now())
                            CheckInTime = self.TimeList1[-1]
                            CheckOutTime = self.TimeList2[-1]
                            self.ElapseHours = (CheckOutTime - CheckInTime)
                            self.MinLabel.setText(
                                "{:.0f}".format(abs(self.ElapseHours.total_seconds() / 60) % 60) + 'm')
                            self.HoursLabel.setText(
                                "{:.0f}".format(abs(self.ElapseHours.total_seconds() / 60 ** 2)) + 'h')
                            self.pushButtonOut.setEnabled(True)
                        else:
                            print('Not clicked.')
                            self.pushButtonOut.setEnabled(True)

        faces_cur_frame = face_recognition.face_locations(frame)
        encodes_cur_frame = face_recognition.face_encodings(frame, faces_cur_frame)
        for encodeFace, faceLoc in zip(encodes_cur_frame, faces_cur_frame):
            match = face_recognition.compare_faces(encode_list_known, encodeFace, tolerance=0.50)
            face_dis = face_recognition.face_distance(encode_list_known, encodeFace)
            name = "unknown"
            best_match_index = np.argmin(face_dis)
            if match[best_match_index]:
                name = class_names[best_match_index].upper()
                y1, x2, y2, x1 = faceLoc
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 20), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
            mark_attendance(name)

        return frame

    def showdialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)

        msg.setText("This is a message box")
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("MessageBox demo")
        msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)

    def ElapseList(self, name):
        # Get absolute path for Attendance.csv file
        attendance_path = os.path.join(self.base_dir, 'dataset', 'Attendance.csv')
        
        with open(attendance_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 2

            Time1 = datetime.datetime.now()
            Time2 = datetime.datetime.now()
            for row in csv_reader:
                for field in row:
                    if field in row:
                        if field == 'Clock In':
                            if row[0] == name:
                                Time1 = (datetime.datetime.strptime(row[1], '%y/%m/%d %H:%M:%S'))
                                self.TimeList1.append(Time1)
                        if field == 'Clock Out':
                            if row[0] == name:
                                Time2 = (datetime.datetime.strptime(row[1], '%y/%m/%d %H:%M:%S'))
                                self.TimeList2.append(Time2)

    def update_frame(self):
        ret, self.image = self.capture.read()
        self.displayImage(self.image, self.encode_list, self.class_names, 1)

    def displayImage(self, image, encode_list, class_names, window=1):

        image = cv2.resize(image, (640, 480))
        try:
            image = self.face_rec_(image, encode_list, class_names)
        except Exception as e:
            print(e)
        qformat = QImage.Format.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformat = QImage.Format.Format_RGBA8888
            else:
                qformat = QImage.Format.Format_RGB888
        outImage = QImage(image, image.shape[1], image.shape[0], image.strides[0], qformat)
        outImage = outImage.rgbSwapped()

        if window == 1:
            self.imgLabel.setPixmap(QPixmap.fromImage(outImage))
            self.imgLabel.setScaledContents(True)

    def closeEvent(self, event):
        """Xử lý sự kiện đóng cửa sổ"""
        # Nếu đang chạy video, dừng lại
        if hasattr(self, 'capture') and self.capture is not None and self.capture.isOpened():
            self.capture.release()

        # Nếu đang có timer, dừng lại
        if hasattr(self, 'timer') and self.timer is not None and self.timer.isActive():
            self.timer.stop()

        event.accept()


# Nếu file được chạy trực tiếp, cho phép test cửa sổ
if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = Ui_OutputDialog()
    window.show()
    sys.exit(app.exec())