# Form implementation generated from reading ui file 'C:\Users\Nicolee\Coding\Project\Face-Recogntion-PyQt\Face_Detection_PyQt_Final\output_window.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_OutputDialog(object):
    def setupUi(self, OutputDialog):
        OutputDialog.setObjectName("OutputDialog")
        OutputDialog.resize(971, 613)
        OutputDialog.setMinimumSize(QtCore.QSize(0, 0))
        OutputDialog.setMaximumSize(QtCore.QSize(1280, 720))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        OutputDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\Nicolee\\Coding\\Project\\Face-Recogntion-PyQt\\Face_Detection_PyQt_Final\\icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        OutputDialog.setWindowIcon(icon)
        self.imgLabel = QtWidgets.QLabel(parent=OutputDialog)
        self.imgLabel.setGeometry(QtCore.QRect(10, 10, 640, 480))
        self.imgLabel.setMinimumSize(QtCore.QSize(4, 0))
        self.imgLabel.setMaximumSize(QtCore.QSize(640, 480))
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=OutputDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 500, 641, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ClockInButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ClockInButton.setFont(font)
        self.ClockInButton.setCheckable(True)
        self.ClockInButton.setObjectName("ClockInButton")
        self.horizontalLayout.addWidget(self.ClockInButton)
        self.ClockOutButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ClockOutButton.setFont(font)
        self.ClockOutButton.setCheckable(True)
        self.ClockOutButton.setObjectName("ClockOutButton")
        self.horizontalLayout.addWidget(self.ClockOutButton)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=OutputDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(660, 10, 281, 75))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.Date_Label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Date_Label.setFont(font)
        self.Date_Label.setObjectName("Date_Label")
        self.gridLayout_2.addWidget(self.Date_Label, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.Time_Label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Time_Label.setFont(font)
        self.Time_Label.setObjectName("Time_Label")
        self.gridLayout_2.addWidget(self.Time_Label, 1, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(parent=OutputDialog)
        self.groupBox.setGeometry(QtCore.QRect(660, 110, 271, 271))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 141, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(120, 30, 131, 211))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.NameLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.NameLabel.setFont(font)
        self.NameLabel.setText("")
        self.NameLabel.setObjectName("NameLabel")
        self.verticalLayout_2.addWidget(self.NameLabel)
        self.StatusLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.StatusLabel.setFont(font)
        self.StatusLabel.setText("")
        self.StatusLabel.setObjectName("StatusLabel")
        self.verticalLayout_2.addWidget(self.StatusLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.HoursLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.HoursLabel.setFont(font)
        self.HoursLabel.setText("")
        self.HoursLabel.setObjectName("HoursLabel")
        self.horizontalLayout_2.addWidget(self.HoursLabel)
        self.MinLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.MinLabel.setFont(font)
        self.MinLabel.setText("")
        self.MinLabel.setObjectName("MinLabel")
        self.horizontalLayout_2.addWidget(self.MinLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=OutputDialog)
        self.groupBox_2.setGeometry(QtCore.QRect(659, 391, 277, 193))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.groupBox_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(15, 31, 253, 145))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButtonRegist = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.pushButtonRegist.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButtonRegist.setSizeIncrement(QtCore.QSize(0, 50))
        self.pushButtonRegist.setObjectName("pushButtonRegist")
        self.verticalLayout_3.addWidget(self.pushButtonRegist)
        self.pushButtonManage = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.pushButtonManage.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButtonManage.setObjectName("pushButtonManage")
        self.verticalLayout_3.addWidget(self.pushButtonManage)

        self.retranslateUi(OutputDialog)
        QtCore.QMetaObject.connectSlotsByName(OutputDialog)

    def retranslateUi(self, OutputDialog):
        _translate = QtCore.QCoreApplication.translate
        OutputDialog.setWindowTitle(_translate("OutputDialog", "Face Recognition Attendance App"))
        self.ClockInButton.setText(_translate("OutputDialog", "Clock In"))
        self.ClockOutButton.setText(_translate("OutputDialog", "Clock Out"))
        self.label.setText(_translate("OutputDialog", "Date :"))
        self.Date_Label.setText(_translate("OutputDialog", "-"))
        self.label_2.setText(_translate("OutputDialog", "Time :"))
        self.Time_Label.setText(_translate("OutputDialog", "-"))
        self.groupBox.setTitle(_translate("OutputDialog", "Details"))
        self.label_3.setText(_translate("OutputDialog", "Name : "))
        self.label_4.setText(_translate("OutputDialog", "Status :"))
        self.label_5.setText(_translate("OutputDialog", "Clocked Time : "))
        self.groupBox_2.setTitle(_translate("OutputDialog", "GroupBox"))
        self.pushButtonRegist.setText(_translate("OutputDialog", "Register Information"))
        self.pushButtonManage.setText(_translate("OutputDialog", "Management"))
