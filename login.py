# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(398, 289)
        login.setStyleSheet("QWidget {\n"
"background-color: \"#232429\"\n"
"}")
        self.button = QtWidgets.QPushButton(login)
        self.button.setGeometry(QtCore.QRect(120, 230, 161, 41))
        font = QtGui.QFont()
       font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button.setFont(font)
        self.button.setStyleSheet("background-color: \"#1d5ffe\";\n"
"color: white;\n"
"border-style: outset;\n"
"border-radius: 10px;\n"
"font: 14px")
        self.button.setObjectName("button")
        self.input_host = QtWidgets.QLineEdit(login)
        self.input_host.setGeometry(QtCore.QRect(40, 40, 231, 31))
        font = QtGui.QFont()
       font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.input_host.setFont(font)
        self.input_host.setStyleSheet("color: \"#eaebf2\";\n"
"font: 12px")
        self.input_host.setObjectName("input_host")
        self.label = QtWidgets.QLabel(login)
        self.label.setGeometry(QtCore.QRect(40, 20, 31, 16))
        font = QtGui.QFont()
       font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: \"#6a6b79\";\n"
"font: 12px")
        self.label.setObjectName("label")
        self.input_user = QtWidgets.QLineEdit(login)
        self.input_user.setGeometry(QtCore.QRect(40, 110, 321, 31))
        font = QtGui.QFont()
       font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.input_user.setFont(font)
        self.input_user.setStyleSheet("color: \"#eaebf2\";\n"
"font: 12px")
        self.input_user.setObjectName("input_user")
        self.input_port = QtWidgets.QLineEdit(login)
        self.input_port.setGeometry(QtCore.QRect(280, 40, 81, 31))
        font = QtGui.QFont()
       font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.input_port.setFont(font)
        self.input_port.setStyleSheet("color: \"#eaebf2\";\n"
"font: 12px")
        self.input_port.setObjectName("input_port")
        self.label_2 = QtWidgets.QLabel(login)
        self.label_2.setGeometry(QtCore.QRect(330, 20, 31, 20))
        font = QtGui.QFont()
       font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.label_2.setStyleSheet("color: \"#6a6b79\";\n"
"font: 12px;")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(login)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 31, 16))
        font = QtGui.QFont()
       font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: \"#6a6b79\";\n"
"font: 12px")
        self.label_3.setObjectName("label_3")
        self.input_password = QtWidgets.QLineEdit(login)
        self.input_password.setGeometry(QtCore.QRect(40, 180, 321, 31))
        font = QtGui.QFont()
       font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.input_password.setFont(font)
        self.input_password.setStyleSheet("color: \"#eaebf2\";\n"
"font: 12px")
        self.input_password.setObjectName("input_password")
        self.label_4 = QtWidgets.QLabel(login)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 61, 16))
        font = QtGui.QFont()
       font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: \"#6a6b79\";\n"
"font: 12px")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Login to Postgresql"))
        self.button.setText(_translate("login", "Login"))
        self.label.setText(_translate("login", "Host"))
        self.label_2.setText(_translate("login", "Port"))
        self.label_3.setText(_translate("login", "User"))
        self.label_4.setText(_translate("login", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QWidget()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec())
