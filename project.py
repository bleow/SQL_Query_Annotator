import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox

from annotation import *
from preprocessing import get_dbs, LoginDetails, QueryInfo

from interface import Login, Error, MainUI


class Main:
    def __init__(self):
        self.login_details = LoginDetails
        self.login_details.host = "localhost"
        self.login_details.port = "5432"
        self.login_details.user = "postgres"
        self.login_details.password = "1111"
        self.login_details = self.login()
        print('host:', self.login_details.host)
        print('port:', self.login_details.port)
        print('user:', self.login_details.user)
        print('pwd:', self.login_details.password)

    def login(self):
        """
        Tell interface to show the login interface
        """
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        login_ui = Login(self.login_details)
        login_ui.setupUi(Form)
        Form.show()
        app.exec()
        return login_ui.login_details

    @staticmethod
    def show_error(msg):
        """
        Helper function to tell interface to show the error dialog box
        """
        app2 = QtWidgets.QApplication(sys.argv)
        Form2 = QtWidgets.QWidget()
        error_ui2 = Error(msg)
        error_ui2.setupUi(Form2)
        Form2.show()
        app2.exec()


    def load_main_UI(self, db_list):
        """
        Tell interface to start the main program loop
        """
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        main_ui = MainUI(self.login_details, db_list)
        main_ui.setupUi(Form)
        Form.show()
        app.exec()

    def main(self):
        """
        The CONTROLLER of the application. Drives the operation of the application.
        """
        # 1. Login to postgresql

        # 2. Connect to db using login details
        db_list = get_dbs(self.login_details)

        # 3. Let user choose database to load, get the tables and columns for that database, wait for user input
        self.load_main_UI(db_list)

    # 4. Get user input
    def get_user_query(self, database, query):
        """
        Callback function that interface.py will call when user clicks 'Run query'
        """
        queryInfo = QueryInfo
        queryInfo.database = database
        queryInfo.query = query
        from preprocessing import preprocessing
        qep = preprocessing(self.login_details, queryInfo)
        from interface import MainUI
        if qep is None:
            return "Invalid query! :("
        else:
            qep_annotated = Annotator().wrapper(qep)
            return str(qep_annotated)


if __name__ == '__main__':
    main = Main()
    main.main()
