import psycopg2

from typing import TypedDict, List
import itertools
import numpy as np
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
            self.connector = psycopg2.connect(host=login_details.host,
                                              port=login_details.port,
                                              user=login_details.user,
                                              password=login_details.password).cursor()
        else:
            self.connector = psycopg2.connect(host=login_details.host,
                                              port=login_details.port,
                                              user=login_details.user,
                                              password=login_details.password,
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


def preprocessing(login_details: LoginDetails, queryInfo: QueryInfo):
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


# code
def permutation(temp_input):
    # perm = permutation

    # initialize variable
    scan_count, join_count, hash_agg_count, material_count, explicit_count = 0, 0, 0, 0, 0
    scan_selected, join_selected, hash_agg_selected, material_selected, explicit_selected = [], [], [], [], []

    # group into respective node types
    for i in temp_input:
        if 'Scan' in i:
            scan_selected.append(i)
            scan_count += 1
        if 'Join' in i:
            join_selected.append(i)
            join_count += 1
        if 'Hashed Aggregation' in i:
            hash_agg_selected.append(i)
            hash_agg_count += 1
        if 'Materialization' in i:
            material_selected.append(i)
            material_count += 1
        if 'Explicit Sort' in i:
            explicit_selected.append(i)
            explicit_count += 1

    # add scan and join node type together
    all_list = [scan_selected, join_selected]

    # append the other node type into list
    if not hash_agg_selected and not material_selected and not explicit_selected:
        all_list.append(['Hashed Aggregation'])
        all_list.append(['Materialization'])
        all_list.append(['Explicit Sort'])
    else:
        all_list.append(hash_agg_selected)
        all_list.append(material_selected)
        all_list.append(explicit_selected)

    # the first 2 (scan and join) list item will always change
    # the last 3 (others) list item will always be the same as thy are only 1 element
    filtered = [e for e in all_list if e != []]
    perm_list = [p for p in itertools.product(*filtered)]

    tuple1 = perm_list[0]
    check_others = np.array([0, 0, 0])
    category = ['Hashed Aggregation', 'Materialization', 'Explicit Sort']

    if 'Hashed Aggregation' in tuple1:
        check_others[0] = 1
    if 'Materialization' in tuple1:
        check_others[1] = 1
    if 'Explicit Sort' in tuple1:
        check_others[2] = 1

    # enable indexes will be set to FALSE
    indexes = np.where(check_others == 0)[0]
    indexes1 = np.where(check_others == 1)[0]
    # print(indexes)

    perm_temp_list = []
    for i in perm_list:
        total_tuple = i
        for j in indexes:
            total_tuple = (*total_tuple, category[j])

        perm_temp_list.append(total_tuple)

    perm_temp_list2 = []
    for i in perm_temp_list:
        for j in indexes1:
            new_tuple = i
            idx = new_tuple.index(category[j])
            new_tuple = new_tuple[:idx] + new_tuple[idx + 1:]
            perm_temp_list2.append(new_tuple)

    perm_tuple_list = perm_temp_list + perm_temp_list2

    perm_query_list = []

    first_default_query = {"enable_bitmapscan": True,
                           "enable_indexscan": True,
                           "enable_indexonlyscan": True,
                           "enable_seqscan": True,
                           "enable_tidscan": True,
                           "enable_hashjoin": True,
                           "enable_mergejoin": True,
                           "enable_nestloop": True,
                           "enable_hashagg": True,
                           "enable_material": True,
                           "enable_sort": True,
                           }

    reference_query = {"enable_bitmapscan": False,
                       "enable_indexscan": False,
                       "enable_indexonlyscan": False,
                       "enable_seqscan": False,
                       "enable_tidscan": False,
                       "enable_hashjoin": False,
                       "enable_mergejoin": False,
                       "enable_nestloop": False,
                       "enable_hashagg": False,
                       "enable_material": False,
                       "enable_sort": False,
                       }

    perm_query_list.append(first_default_query)

    node_array = {
        "Bitmap Scan": "enable_bitmapscan",
        "Index Scan": "enable_indexscan",
        "Index-only Scan": "enable_indexonlyscan",
        "Sequential Scan": "enable_seqscan",
        "Tid Scan": "enable_tidscan",
        "Hash Join": "enable_hashjoin",
        "Merge Join": "enable_mergejoin",
        "Nested Loop Join": "enable_nestloop",
        "Hashed Aggregation": "enable_hashagg",
        "Materialization": "enable_material",
        "Explicit Sort": "enable_sort"
    }

    for i in perm_tuple_list:
        new_dict = reference_query.copy()
        for j in i:
            if j in node_array:
                key_value = node_array[j]
                if key_value in new_dict:
                    new_dict[key_value] = True

        perm_query_list.append(new_dict)

    for i in perm_query_list:
        print(i)
        print("\n")