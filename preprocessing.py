import psycopg2

from typing import TypedDict, List
from PyQt6.QtWidgets import QMessageBox

"""
This file also contains the business objects related to the application,
e.g. database connector, data structures for logging in etc
"""


class LoginDetails(TypedDict):
    host: str
    port: int
    user: str
    password: str


class QueryInfo(TypedDict):
    database: str
    query: str


class DatabaseConnector(object):
    """
    The connector to connect to the postgresql database.
    """

    def __init__(self, login_details: LoginDetails, dbname=None):
        if dbname is None:
            self.connector = psycopg2.connect(host=login_details.host, port=login_details.port,
                                              user=login_details.user, password=login_details.password).cursor()
        else:
            self.connector = psycopg2.connect(host=login_details.host, port=login_details.port,
                                              user=login_details.user, password=login_details.password,
                                              dbname=dbname).cursor()

    def __enter__(self):
        return self.connector

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connector.close()


"""
Functions to help process database-related queries 
"""


def get_dbs(login_details: LoginDetails) -> List[str]:
    """
    Get list of databases.
    """
    try:
        with DatabaseConnector(login_details) as cursor:
            query = "SELECT datname FROM pg_database WHERE datistemplate = false;"
            cursor.execute(query)
            db_list = cursor.fetchall()
            db_list = [i[0] for i in db_list]
            return db_list
    except psycopg2.OperationalError as e:
        from project import Main
        Main.show_error(str(e))


def get_tables_for_db(login_details: LoginDetails, db: str) -> List[str]:
    """
    Get list of tables present in a given database.
    """
    try:
        with DatabaseConnector(login_details, db) as cursor:
            query = "SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE';"
            cursor.execute(query)
            res = cursor.fetchall()
            res = [i[0] for i in res]
            return res
    except psycopg2.OperationalError as e:
        from project import main
        main.show_error(str(e))


def get_columns_for_table(login_details: LoginDetails, db: str, schema: str) -> List[str]:
    """
    Get list of columns present in a given table.
    """
    try:
        with DatabaseConnector(login_details, db) as cursor:
            query = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{schema}' AND table_catalog = '{db}';"
            cursor.execute(query)
            res = cursor.fetchall()
            res = [_[0] for _ in res]
            return res
    except psycopg2.OperationalError as e:
        from project import Main
        Main.show_error(str(e))


def run_query(login_details: LoginDetails, queryInfo: QueryInfo):
    """
    The pre-ALGORITHM of the application. Reads and parses input for the annotation class.

    :returns: String of cleaned query OR False if user input is invalid
    """
    with DatabaseConnector(login_details, queryInfo.database) as cursor:
        query = f'EXPLAIN (FORMAT JSON) {str(queryInfo.query)}'
        try:
            cursor.execute(query)
            res = cursor.fetchall()
            return res
        except:
            return None
