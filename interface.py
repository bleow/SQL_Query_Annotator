from PyQt6 import QtCore, QtGui, QtWidgets
import sys

from PyQt6.QtWidgets import QTreeWidgetItem

from preprocessing import LoginDetails, get_tables_for_db, get_columns_for_table


class Interface:
    """
    The VIEW of the application.

    :returns: Dict['schema': str, 'query': str]
    """

    @classmethod
    def login(cls, login_details: LoginDetails) -> LoginDetails:
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        login_ui = Login(login_details)
        login_ui.setupUi(Form)
        Form.show()
        app.exec()
        return login_ui.login_details

    @classmethod
    def show_error(cls, msg):
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        error_ui = Error(msg)
        error_ui.setupUi(Form)
        Form.show()
        app.exec()
        return

    @classmethod
    def get_query(cls, login_details, db_list):
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        main_ui = MainUI(login_details, db_list)
        main_ui.setupUi(Form)
        Form.show()
        app.exec()
        print('program should not reach here lmao')
        return


"""
Login screen objects that are children of the above Interface() class:
"""


class Login(object):
    def __init__(self, login_details):
        self.login_details = login_details

    ########### START: ui boilerplate for login ###########

    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(398, 289)
        login.setStyleSheet("QWidget {\n"
                            "background-color: \"#232429\"\n"
                            "}")
        self.button = QtWidgets.QPushButton(login)
        self.button.setGeometry(QtCore.QRect(120, 230, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
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
        font.setPointSize(-1)
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
        font.setPointSize(-1)
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
        font.setPointSize(-1)
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
        font.setPointSize(-1)
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
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.label_2.setStyleSheet("color: \"#6a6b79\";\n"
                                   "font: 12px;")
        self.label_2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(login)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
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
        font.setPointSize(-1)
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
        font.setPointSize(-1)
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

        ########### END: ui boilerplate for login ###########

        self.input_host.setText(self.login_details.host)
        self.input_port.setText(self.login_details.port)
        self.input_user.setText(self.login_details.user)
        self.input_password.setText(self.login_details.password)
        self.button.clicked.connect(self.show_line)
        self.button.clicked.connect(QtCore.QCoreApplication.instance().quit)

    def show_line(self):
        self.login_details.host = self.input_host.text()
        self.login_details.port = self.input_port.text()
        self.login_details.user = self.input_user.text()
        self.login_details.password = self.input_password.text()


class Error(object):
    def __init__(self, msg):
        self.msg = msg

    ########### START: ui boilerplate for login ###########

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
        self.label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
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

        ########### END: ui boilerplate for login ###########

        self.label.setText(self.msg)
        self.button.clicked.connect(QtCore.QCoreApplication.instance().quit)


class MainUI(object):

    def __init__(self, login_details, db_list):
        self.db_list = db_list
        self.login_details = login_details

    ########### START: ui boilerplate for login ###########
    def setupUi(self, MainUi):
        MainUi.setObjectName("MainUi")
        MainUi.resize(1106, 889)
        MainUi.setStyleSheet("QWidget {\n"
                             "\n"
                             "background-color: \"#232429\"\n"
                             "\n"
                             "}")
        self.ExecuteQuery = QtWidgets.QPushButton(MainUi)
        self.ExecuteQuery.setGeometry(QtCore.QRect(890, 300, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ExecuteQuery.setFont(font)
        self.ExecuteQuery.setStyleSheet("background-color: \"#1d5ffe\";\n"
                                        "color: white;\n"
                                        "border-style: outset;\n"
                                        "border-radius: 10px;\n"
                                        "font: 14px")
        self.ExecuteQuery.setObjectName("ExecuteQuery")
        self.input_comboBox = QtWidgets.QComboBox(MainUi)
        self.input_comboBox.setGeometry(QtCore.QRect(20, 50, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.input_comboBox.setFont(font)
        self.input_comboBox.setStyleSheet("background-color: \"#2b2f3b\";\n"
                                          "color: \"#eaebf2\";\n"
                                          "font: 12px")
        self.input_comboBox.setCurrentText("")
        self.input_comboBox.setObjectName("input_comboBox")
        self.input_plainTextEdit = QtWidgets.QPlainTextEdit(MainUi)
        self.input_plainTextEdit.setGeometry(QtCore.QRect(180, 50, 871, 231))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.input_plainTextEdit.setFont(font)
        self.input_plainTextEdit.setStyleSheet("color: \"#eaebf2\";\n"
                                               "font: 12px")
        self.input_plainTextEdit.setObjectName("input_plainTextEdit")
        self.label = QtWidgets.QLabel(MainUi)
        self.label.setGeometry(QtCore.QRect(20, 30, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: \"#6a6b79\";\n"
                                 "font: 12px")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MainUi)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: \"#6a6b79\";\n"
                                   "font: 12px")
        self.label_2.setObjectName("label_2")
        self.input_treeWidget = QtWidgets.QTreeWidget(MainUi)
        self.input_treeWidget.setGeometry(QtCore.QRect(20, 130, 151, 731))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.input_treeWidget.setFont(font)
        self.input_treeWidget.setStyleSheet("color: \"#eaebf2\";\n"
                                            "font: 12px")
        self.input_treeWidget.setColumnCount(1)
        self.input_treeWidget.setObjectName("input_treeWidget")
        self.input_treeWidget.headerItem().setText(0, "1")
        self.label_3 = QtWidgets.QLabel(MainUi)
        self.label_3.setGeometry(QtCore.QRect(180, 30, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: \"#6a6b79\";\n"
                                   "font: 12px")
        self.label_3.setObjectName("label_3")
        self.ExecuteQuery.raise_()
        self.input_comboBox.raise_()
        self.input_plainTextEdit.raise_()
        self.label.raise_()
        self.input_treeWidget.raise_()
        self.label_3.raise_()
        self.label_2.raise_()

        self.retranslateUi(MainUi)
        QtCore.QMetaObject.connectSlotsByName(MainUi)

    def retranslateUi(self, MainUi):
        _translate = QtCore.QCoreApplication.translate
        MainUi.setWindowTitle(_translate("MainUi", "CZ4031 Group 58 Project 2"))
        self.ExecuteQuery.setText(_translate("MainUi", "⯈ Run Query"))
        self.label.setText(_translate("MainUi", "Choose database"))
        self.label_2.setText(_translate("MainUi", "Tables:"))
        self.label_3.setText(_translate("MainUi", "Input a query:"))

        ########### END: ui boilerplate for login ###########

        self.input_comboBox.addItems(self.db_list)
        if "TPC-H" in self.db_list:
            self.input_comboBox.setCurrentText("TPC-H")
        self.populate_pane()

        self.input_comboBox.currentIndexChanged.connect(self.populate_pane)
        self.input_treeWidget.itemDoubleClicked.connect(self.add_to_text)
        self.input_plainTextEdit.setPlainText('SELECT ')

    def populate_pane(self):
        self.input_treeWidget.clear()
        tables = get_tables_for_db(self.login_details, self.input_comboBox.currentText())
        treeWid = {}
        for table in tables:
            treeWid[table] = get_columns_for_table(self.login_details, self.input_comboBox.currentText(), table)
        for table in treeWid:
            tbl = QTreeWidgetItem([table])
            for column in treeWid[table]:
                col = QTreeWidgetItem([column])
                tbl.addChild(col)
            self.input_treeWidget.addTopLevelItem(tbl)

    def add_to_text(self, item: QTreeWidgetItem, col: int):
        self.input_plainTextEdit.appendPlainText(f'{item.text(col)}, ')
