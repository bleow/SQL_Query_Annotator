# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Error(object):
    def setupUi(self, Error):
        Error.setObjectName("Error")
        Error.resize(410, 154)
        Error.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        Error.setStyleSheet("QWidget {\n"
"background-color: \"#232429\"\n"
"}")
        self.button = QtWidgets.QPushButton(Error)
        self.button.setGeometry(QtCore.QRect(140, 100, 140, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button.setFont(font)
        self.button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.button.setMouseTracking(False)
        self.button.setStyleSheet("background-color: \"#1d5ffe\";\n"
"color: white;\n"
"border-style: outset;\n"
"border-radius: 10px;\n"
"font: 12px")
        self.button.setAutoDefault(False)
        self.button.setDefault(False)
        self.button.setObjectName("button")
        self.label = QtWidgets.QLabel(Error)
        self.label.setGeometry(QtCore.QRect(30, 30, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: \"#eaebf2\";\n"
"font: 12px")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Error)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: \"#6a6b79\";\n"
"font: 11px")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Error)
        QtCore.QMetaObject.connectSlotsByName(Error)

    def retranslateUi(self, Error):
        _translate = QtCore.QCoreApplication.translate
        Error.setWindowTitle(_translate("Error", "Error Encountered"))
        self.button.setText(_translate("Error", "Ok :("))
        self.label.setText(_translate("Error", "TextLabel"))
        self.label_4.setText(_translate("Error", "Error:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Error = QtWidgets.QWidget()
    ui = Ui_Error()
    ui.setupUi(Error)
    Error.show()
    sys.exit(app.exec())
