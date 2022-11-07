import psycopg2

from typing import TypedDict, List

import interface

"""
This file also contains the business objects related to the application,
e.g. database connector, data structures for logging in etc
"""


class LoginDetails(TypedDict):
    host: str
    port: int
    user: str
    password: str


class UserInput(TypedDict):
    schema: str
    query: str


class QueryInfo(TypedDict):
    cleaned_query: str
    qep: str
    aqp: str


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
    try:
        with DatabaseConnector(login_details) as cursor:
            query = "SELECT datname FROM pg_database WHERE datistemplate = false;"
            cursor.execute(query)
            db_list = cursor.fetchall()
            db_list = [i[0] for i in db_list]
            return db_list
    except psycopg2.OperationalError as e:
        interface.show_error(str(e))


def get_tables_for_db(login_details: LoginDetails, db: str) -> List[str]:
    try:
        with DatabaseConnector(login_details, db) as cursor:
            query = "SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE';"
            cursor.execute(query)
            res = cursor.fetchall()
            res = [i[0] for i in res]
            return res
    except psycopg2.OperationalError as e:
        interface.show_error(str(e))


def get_columns_for_table(login_details: LoginDetails, db: str, schema: str) -> List[str]:
    try:
        with DatabaseConnector(login_details, db) as cursor:
            query = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{schema}' AND table_catalog = '{db}';"
            cursor.execute(query)
            res = cursor.fetchall()
            res = [_[0] for _ in res]
            return res
    except psycopg2.OperationalError as e:
        interface.show_error(str(e))

# def preprocessing(user_input: UserInput) -> QueryInfo:
#     """
#     The pre-ALGORITHM of the application. Reads and parses input for the annotation class.
#
#     :returns: String of cleaned query OR False if user input is invalid
#     """
#
#     cleaned_query = user_input['query'].strip()
#     aqp = 'aqp'
#     qep = 'qep'
#
#     invalid: bool = False
#     if invalid:
#         return QueryInfo(cleaned_query=INVALID_INPUT, qep=INVALID_INPUT, aqp=INVALID_INPUT)
#
#     return QueryInfo(cleaned_query=cleaned_query, qep=qep, aqp=aqp)
