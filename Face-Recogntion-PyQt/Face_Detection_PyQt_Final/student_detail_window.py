# Form implementation generated from reading ui file 'C:\Users\Nicolee\Coding\Project\Face-Recogntion-PyQt\Face_Detection_PyQt_Final\student_detail_window.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_StudentDetailDialog(object):
    def setupUi(self, StudentDetailDialog):
        StudentDetailDialog.setObjectName("StudentDetailDialog")
        StudentDetailDialog.resize(600, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\Nicolee\\Coding\\Project\\Face-Recogntion-PyQt\\Face_Detection_PyQt_Final\\icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        StudentDetailDialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(StudentDetailDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=StudentDetailDialog)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEditStudentID = QtWidgets.QLineEdit(parent=StudentDetailDialog)
        self.lineEditStudentID.setReadOnly(False)
        self.lineEditStudentID.setObjectName("lineEditStudentID")
        self.verticalLayout_2.addWidget(self.lineEditStudentID)
        self.label_2 = QtWidgets.QLabel(parent=StudentDetailDialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEditFullName = QtWidgets.QLineEdit(parent=StudentDetailDialog)
        self.lineEditFullName.setObjectName("lineEditFullName")
        self.verticalLayout_2.addWidget(self.lineEditFullName)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButtonSave = QtWidgets.QPushButton(parent=StudentDetailDialog)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.horizontalLayout_3.addWidget(self.pushButtonSave)
        self.pushButtonDelete = QtWidgets.QPushButton(parent=StudentDetailDialog)
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.horizontalLayout_3.addWidget(self.pushButtonDelete)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.pushButtonCancel = QtWidgets.QPushButton(parent=StudentDetailDialog)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.verticalLayout_2.addWidget(self.pushButtonCancel)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=StudentDetailDialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.labelPhoto = QtWidgets.QLabel(parent=StudentDetailDialog)
        self.labelPhoto.setMinimumSize(QtCore.QSize(300, 250))
        self.labelPhoto.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.labelPhoto.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelPhoto.setObjectName("labelPhoto")
        self.verticalLayout_3.addWidget(self.labelPhoto)
        self.labelPhotoStatus = QtWidgets.QLabel(parent=StudentDetailDialog)
        self.labelPhotoStatus.setText("")
        self.labelPhotoStatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelPhotoStatus.setObjectName("labelPhotoStatus")
        self.verticalLayout_3.addWidget(self.labelPhotoStatus)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonUpload = QtWidgets.QPushButton(parent=StudentDetailDialog)
        self.pushButtonUpload.setObjectName("pushButtonUpload")
        self.horizontalLayout_2.addWidget(self.pushButtonUpload)
        self.pushButtonCapture = QtWidgets.QPushButton(parent=StudentDetailDialog)
        self.pushButtonCapture.setObjectName("pushButtonCapture")
        self.horizontalLayout_2.addWidget(self.pushButtonCapture)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBoxAttendance = QtWidgets.QGroupBox(parent=StudentDetailDialog)
        self.groupBoxAttendance.setObjectName("groupBoxAttendance")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBoxAttendance)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableWidgetAttendance = QtWidgets.QTableWidget(parent=self.groupBoxAttendance)
        self.tableWidgetAttendance.setObjectName("tableWidgetAttendance")
        self.tableWidgetAttendance.setColumnCount(0)
        self.tableWidgetAttendance.setRowCount(0)
        self.tableWidgetAttendance.horizontalHeader().setSortIndicatorShown(True)
        self.verticalLayout_4.addWidget(self.tableWidgetAttendance)
        self.verticalLayout.addWidget(self.groupBoxAttendance)

        self.retranslateUi(StudentDetailDialog)
        QtCore.QMetaObject.connectSlotsByName(StudentDetailDialog)

    def retranslateUi(self, StudentDetailDialog):
        _translate = QtCore.QCoreApplication.translate
        StudentDetailDialog.setWindowTitle(_translate("StudentDetailDialog", "Student Details "))
        self.label.setText(_translate("StudentDetailDialog", "Student ID:"))
        self.label_2.setText(_translate("StudentDetailDialog", "Full Name:"))
        self.pushButtonSave.setText(_translate("StudentDetailDialog", "Save student "))
        self.pushButtonDelete.setText(_translate("StudentDetailDialog", "Delete student"))
        self.pushButtonCancel.setText(_translate("StudentDetailDialog", "Cancel"))
        self.label_3.setText(_translate("StudentDetailDialog", "Ảnh sinh viên:"))
        self.pushButtonUpload.setText(_translate("StudentDetailDialog", "Upload photo"))
        self.pushButtonCapture.setText(_translate("StudentDetailDialog", "Capture photo"))
        self.groupBoxAttendance.setTitle(_translate("StudentDetailDialog", "Thông tin điểm danh"))
        self.tableWidgetAttendance.setSortingEnabled(True)
