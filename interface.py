from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTreeWidgetItem
import pyqtgraph as pg

COLOUR_PALETTE = ["#CCE4FF", "#B3B7FF", "#99CAFF", "#80BDFF", "#66AFFF", "#4DA2FF", "#3395FF", "#1987FF", "#006EE6",
                  "#0055B3", "#003D80"]


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
        self.label_2.setGeometry(QtCore.QRect(300, 20, 31, 20))
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

    ########### START: ui boilerplate for error ###########

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

        ########### END: ui boilerplate for error ###########

        self.label.setText(self.msg)
        self.button.clicked.connect(QtCore.QCoreApplication.instance().quit)


class MainUI(object):

    def __init__(self, login_details, db_list):
        self.db_list = db_list
        self.login_details = login_details

    ########### START: ui boilerplate for main ###########
    def setupUi(self, MainUi):
        MainUi.setObjectName("MainUi")
        MainUi.resize(1104, 882)
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
        self.input_comboBox.setGeometry(QtCore.QRect(10, 50, 151, 41))
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
                                               "font: 12px;\n"
                                               "padding: 5px")
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
        self.label_2.setGeometry(QtCore.QRect(10, 480, 111, 16))
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
        self.input_treeWidget.setGeometry(QtCore.QRect(10, 500, 151, 361))
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
        self.label_qep = QtWidgets.QLabel(MainUi)
        self.label_qep.setGeometry(QtCore.QRect(180, 350, 871, 211))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_qep.setFont(font)
        self.label_qep.setStyleSheet("color: \"#eaebf2\";\n"
                                     "font: 12px;\n"
                                     "background-color: \"#2b2f3b\";\n"
                                     "padding: 5px")
        self.label_qep.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_qep.setWordWrap(True)
        self.label_qep.setObjectName("label_qep")
        self.label_5 = QtWidgets.QLabel(MainUi)
        self.label_5.setGeometry(QtCore.QRect(180, 330, 471, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: \"#6a6b79\";\n"
                                   "font: 12px")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(MainUi)
        self.label_6.setGeometry(QtCore.QRect(180, 590, 871, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: \"#6a6b79\";\n"
                                   "font: 12px")
        self.label_6.setObjectName("label_6")
        self.label_graph = pg.PlotWidget(MainUi)
        self.label_graph.setGeometry(QtCore.QRect(180, 610, 625, 251))
        self.label_graph.setStyleSheet("color: \"#eaebf2\";\n"
                                       "font: 12px;\n"
                                       "background-color: \"#2b2f3b\";\n"
                                       "padding: 0px;\n"
                                       "border-width: 0px;")
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_graph.setObjectName("label_graph")


        self.label_graph_data = QtWidgets.QTreeWidget(MainUi)
        self.label_graph_data.setGeometry(QtCore.QRect(822, 610, 230, 251))
        self.label_graph_data.setStyleSheet("color: \"#eaebf2\";\n"
                                            "font: 12px")
        self.label_graph_data.setColumnCount(1)
        self.label_graph_data.setObjectName("label_graph_data")
        self.label_graph_data.headerItem().setText(0, "1")

        # checkbox
        self.cb_bitmap = QtWidgets.QCheckBox(MainUi)
        self.cb_bitmap.setGeometry(QtCore.QRect(20, 140, 141, 20))
        self.cb_bitmap.setObjectName("cb_bitmap")
        self.label_4 = QtWidgets.QLabel(MainUi)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: \"#6a6b79\";\n""font: 12px")
        self.label_4.setObjectName("label_4")
        self.cb_index = QtWidgets.QCheckBox(MainUi)
        self.cb_index.setGeometry(QtCore.QRect(20, 170, 141, 20))
        self.cb_index.setObjectName("cb_index")
        self.cb_indexonly = QtWidgets.QCheckBox(MainUi)
        self.cb_indexonly.setGeometry(QtCore.QRect(20, 200, 141, 20))
        self.cb_indexonly.setObjectName("cb_indexonly")
        self.cb_seq = QtWidgets.QCheckBox(MainUi)
        self.cb_seq.setGeometry(QtCore.QRect(20, 230, 141, 20))
        self.cb_seq.setObjectName("cb_seq")
        self.cb_tid = QtWidgets.QCheckBox(MainUi)
        self.cb_tid.setGeometry(QtCore.QRect(20, 260, 141, 20))
        self.cb_tid.setObjectName("cb_tid")
        self.cb_nestedloop = QtWidgets.QCheckBox(MainUi)
        self.cb_nestedloop.setGeometry(QtCore.QRect(20, 350, 151, 20))
        self.cb_nestedloop.setObjectName("cb_nestedloop")
        self.cb_hash = QtWidgets.QCheckBox(MainUi)
        self.cb_hash.setGeometry(QtCore.QRect(20, 290, 141, 20))
        self.cb_hash.setObjectName("cb_hash")
        self.cb_merge = QtWidgets.QCheckBox(MainUi)
        self.cb_merge.setGeometry(QtCore.QRect(20, 320, 151, 20))
        self.cb_merge.setObjectName("cb_merge")
        self.cb_hashagg = QtWidgets.QCheckBox(MainUi)
        self.cb_hashagg.setGeometry(QtCore.QRect(20, 380, 151, 20))
        self.cb_hashagg.setObjectName("cb_hashagg")
        self.cb_material = QtWidgets.QCheckBox(MainUi)
        self.cb_material.setGeometry(QtCore.QRect(20, 410, 141, 20))
        self.cb_material.setObjectName("cb_material")
        self.cb_explicit = QtWidgets.QCheckBox(MainUi)
        self.cb_explicit.setGeometry(QtCore.QRect(20, 440, 141, 20))
        self.cb_explicit.setObjectName("cb_explicit")

        self.cb_bitmap.setStyleSheet("color: \"#6a6b79\";\n" "font: 12px")
        self.cb_index.setStyleSheet("color: \"#6a6b79\";\n" "font: 12px")
        self.cb_indexonly.setStyleSheet("color: \"#6a6b79\";\n" "font: 12px")
        self.cb_seq.setStyleSheet("color: \"#6a6b79\";\n" "font: 12px")
        self.cb_tid.setStyleSheet("color: \"#6a6b79\";\n" "font: 12px")
        self.cb_hash.setStyleSheet("color: \"#6a6b79\";\n" "font: 12px")
        self.cb_merge.setStyleSheet("color: \"#6a6b79\";\n" "font: 12px")
        self.cb_nestedloop.setStyleSheet("color: \"#6a6b79\";\n" "font: 12px")
        self.cb_hashagg.setStyleSheet("color: \"#6a6b79\";\n" "font: 12px")
        self.cb_material.setStyleSheet("color: \"#6a6b79\";\n" "font: 12px")
        self.cb_explicit.setStyleSheet("color: \"#6a6b79\";\n" "font: 12px")

        self.cb_bitmap.raise_()
        self.cb_index.raise_()
        self.cb_indexonly.raise_()
        self.cb_seq.raise_()
        self.cb_tid.raise_()
        self.cb_nestedloop.raise_()
        self.cb_hash.raise_()
        self.cb_merge.raise_()
        self.cb_hashagg.raise_()
        self.cb_material.raise_()
        self.cb_explicit.raise_()
        self.label_4.raise_()

        self.ExecuteQuery.raise_()
        self.input_comboBox.raise_()
        self.input_plainTextEdit.raise_()
        self.label.raise_()
        self.input_treeWidget.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.label_qep.raise_()
        self.label_5.raise_()
        self.label_6.raise_()

        self.retranslateUi(MainUi)

        QtCore.QMetaObject.connectSlotsByName(MainUi)

    def retranslateUi(self, MainUi):
        _translate = QtCore.QCoreApplication.translate
        MainUi.setWindowTitle(_translate("MainUi", "CZ4031 Group 58 Project 2"))
        self.ExecuteQuery.setText(_translate("MainUi", "⯈ Run Query"))
        self.label.setText(_translate("MainUi", "Choose database"))
        self.label_2.setText(_translate("MainUi", "Tables:"))
        self.label_3.setText(_translate("MainUi", "Input a query:"))
        self.label_qep.setText(_translate("MainUi",
                                          "The Query Execution Plan in natural language will be printed here after you click \"Run Query\""))
        self.label_5.setText(_translate("MainUi", "HOW // Query Plan:"))
        self.label_6.setText(
            _translate("MainUi", "WHY // Alternative Plan Comparisons of TOTAL COST vs PLAN CONFIGURATION:"))

        self.label_4.setText(_translate("MainUi", "Select Parameters"))
        self.cb_bitmap.setText(_translate("MainUi", "Bitmap Scan"))
        self.cb_index.setText(_translate("MainUi", "Index Scan"))
        self.cb_indexonly.setText(_translate("MainUi", "Index-only Scan"))
        self.cb_seq.setText(_translate("MainUi", "Sequential Scan"))
        self.cb_tid.setText(_translate("MainUi", "Tid Scan"))
        self.cb_nestedloop.setText(_translate("MainUi", "Nested Loop Join"))
        self.cb_hash.setText(_translate("MainUi", "Hash Join"))
        self.cb_merge.setText(_translate("MainUi", "Merge Join"))
        self.cb_hashagg.setText(_translate("MainUi", "Hashed Aggregation"))
        self.cb_material.setText(_translate("MainUi", "Materialization"))
        self.cb_explicit.setText(_translate("MainUi", "Explicit Sort"))

        ########### END: ui boilerplate for main ###########

        self.cb_bitmap.setChecked(True)
        self.cb_index.setChecked(True)
        self.cb_indexonly.setChecked(True)
        self.cb_seq.setChecked(True)
        self.cb_tid.setChecked(True)
        self.cb_nestedloop.setChecked(True)
        self.cb_hash.setChecked(True)
        self.cb_merge.setChecked(True)
        self.cb_hashagg.setChecked(True)
        self.cb_material.setChecked(True)
        self.cb_explicit.setChecked(True)

        self.input_comboBox.addItems(self.db_list)
        if "TPC-H" in self.db_list:
            self.input_comboBox.setCurrentText("TPC-H")
        self.populate_pane()

        self.input_comboBox.currentIndexChanged.connect(self.populate_pane)
        self.input_treeWidget.itemDoubleClicked.connect(self.add_to_text)
        self.input_plainTextEdit.setPlainText(
            'SELECT * FROM region LEFT JOIN nation on region.r_regionkey = nation.n_regionkey ORDER BY r_name DESC ')

        self.ExecuteQuery.clicked.connect(self.show_annotations)

    def doCheck(self):
        checked = []
        if self.cb_bitmap.isChecked():
            checked.append("Bitmap Scan")
        if self.cb_index.isChecked():
            checked.append("Index Scan")
        if self.cb_indexonly.isChecked():
            checked.append("Index-only Scan")
        if self.cb_seq.isChecked():
            checked.append("Sequential Scan")
        if self.cb_tid.isChecked():
            checked.append("Tid Scan")
        if self.cb_hash.isChecked():
            checked.append("Hash Join")
        if self.cb_merge.isChecked():
            checked.append("Merge Join")
        if self.cb_nestedloop.isChecked():
            checked.append("Nested Loop Join")
        if self.cb_hashagg.isChecked():
            checked.append("Hashed Aggregation")
        if self.cb_material.isChecked():
            checked.append("Materialization")
        if self.cb_explicit.isChecked():
            checked.append("Explicit Sort")

        return checked

    def populate_pane(self) -> QTreeWidgetItem:
        from preprocessing import get_tables_for_db, get_columns_for_table
        self.input_treeWidget.clear()
        tables = get_tables_for_db(self.login_details, self.input_comboBox.currentText())
        treeWid = {}
        for table in tables:
            treeWid[table] = get_columns_for_table(self.login_details, self.input_comboBox.currentText(), table)
        print(treeWid)
        for table in treeWid:
            tbl = QTreeWidgetItem([table])
            for column in treeWid[table]:
                col = QTreeWidgetItem([column])
                tbl.addChild(col)
            self.input_treeWidget.addTopLevelItem(tbl)

    def add_to_text(self, item: QTreeWidgetItem, col: int):
        self.input_plainTextEdit.appendPlainText(f'{item.text(col)}, ')

    def show_annotations(self):
        from project import Main
        annotation, qep_cost = Main.get_annotated_qep(self, self.input_comboBox.currentText(),
                                                      self.input_plainTextEdit.toPlainText())
        self.label_qep.setText(annotation)

        import preprocessing
        perm_list = preprocessing.permutation(self)

        if qep_cost != -1:
            self.plot_aqps(perm_list, qep_cost)

    def plot_aqps(self, perm_list, qep_cost):
        self.label_graph.clear()

        from project import Main
        alt_plans = Main.get_aqp(self, perm_list, self.input_comboBox.currentText(),
                                 self.input_plainTextEdit.toPlainText())
        print('perm', perm_list)
        print('alt', alt_plans)

        configs = ["QEP"]
        for i in range(0, len(alt_plans)):
            configs.append("AQP" + str(i + 1))
        print('configs', configs)

        costs = [qep_cost]
        for i in alt_plans:
            total_cost = i['Total Cost']
            costs.append(total_cost)
        print('costs', costs)

        BINS = len(COLOUR_PALETTE)
        COST_DIFFERENTIAL = max(costs) - min(costs)
        colour = []
        for cost in costs:
            diff = cost - min(costs)
            bin = int((diff / COST_DIFFERENTIAL) * (BINS - 1))
            colour.append(COLOUR_PALETTE[bin])

        bar_graphs = pg.BarGraphItem(x0=[_ for _ in range(len(configs))], y0=0, width=1, height=costs, brushes=colour)
        self.label_graph.addItem(bar_graphs)
        ticks = [list(zip([i + 0.5 for i in range(len(configs))], configs))]
        xax = self.label_graph.getAxis('bottom')
        xax.setTicks(ticks)

        treeWid_aqp = {}
        for i in range(len(configs)):
            key = str(configs[i]) + str(' : ') + str(costs[i])
            value = []
            if i == 0:
                value.append("This is the QEP chosen by the DBMS.")
            else:
                for k, v in perm_list[i-1].items():
                    value.append(str(k) + ' : ' + str(v))
            treeWid_aqp[key] = value

        self.label_graph_data.clear()

        for table in treeWid_aqp:
            tbl = QTreeWidgetItem([table])
            for column in treeWid_aqp[table]:
                col = QTreeWidgetItem([column])
                tbl.addChild(col)
            self.label_graph_data.addTopLevelItem(tbl)
