# Form implementation generated from reading ui file 'C:\Users\Nicolee\Coding\Project\Face-Recogntion-PyQt\Face_Detection_PyQt_Final\login_window.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QtCore.QSize(700, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\Nicolee\\Coding\\Project\\Face-Recogntion-PyQt\\Face_Detection_PyQt_Final\\icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-5, -6, 709, 481))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\Nicolee\\Coding\\Project\\Face-Recogntion-PyQt\\Face_Detection_PyQt_Final\\background1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(35, 103, 633, 253))
        self.groupBox.setStyleSheet("background-color: rgba(255, 255, 255, 128);\n"
"color: rgb(255, 255, 255);\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"border-radius:5px;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(15, 19, 601, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setStyleSheet("font: 63 10pt \"Montserrat SemiBold\";\n"
"color: rgb(14, 23, 67);\n"
"padding: 5px;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEditUsername = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.lineEditUsername.setMinimumSize(QtCore.QSize(0, 60))
        self.lineEditUsername.setStyleSheet("background-color: rgb(242, 248, 255);\n"
"color: rgb(14, 23, 67);\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"border-radius: 10px;\n"
"padding: 5px;")
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.verticalLayout.addWidget(self.lineEditUsername)
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_3.setStyleSheet("font: 63 10pt \"Montserrat SemiBold\";\n"
"color: rgb(14, 23, 67);\n"
"padding: 5px;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEditPassword = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.lineEditPassword.setMinimumSize(QtCore.QSize(0, 60))
        self.lineEditPassword.setStyleSheet("background-color: rgb(242, 248, 255);\n"
"color: rgb(14, 23, 67);\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"border-radius: 10px;\n"
"padding: 5px;")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.verticalLayout.addWidget(self.lineEditPassword)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(48, 372, 601, 42))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(16)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonLogin = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButtonLogin.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButtonLogin.setStyleSheet("\n"
"QPushButton {\n"
" /* Màu nền mặc định */\n"
"    background-color: rgb(105, 248, 255);\n"
"    border-radius: 5px;\n"
"    color: rgb(9, 28, 84);\n"
"    font: 8pt \"CocogooseProTrial Semilight\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(137, 227, 254);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(105, 248, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.horizontalLayout.addWidget(self.pushButtonLogin)
        self.pushButtonClear = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButtonClear.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButtonClear.setStyleSheet("\n"
"QPushButton {\n"
" /* Màu nền mặc định */\n"
"    background-color: rgb(105, 248, 255);\n"
"    border-radius: 5px;\n"
"    color: rgb(9, 28, 84);\n"
"    font: 8pt \"CocogooseProTrial Semilight\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(137, 227, 254);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(105, 248, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.horizontalLayout.addWidget(self.pushButtonClear)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 36, 469, 49))
        self.label_4.setStyleSheet("font: 14pt \"CocogooseProTrial Darkmode\";\n"
"color: rgb(255, 255, 255);\n"
"padding:10px;\n"
"background-color: rgb(255, 255, 255,128);")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manager Login"))
        self.label_2.setText(_translate("MainWindow", "Username:"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.pushButtonLogin.setText(_translate("MainWindow", "Login"))
        self.pushButtonClear.setText(_translate("MainWindow", "Clear"))
        self.label_4.setText(_translate("MainWindow", "LOGIN MANAGEMENT"))
