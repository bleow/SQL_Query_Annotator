import psycopg2

from interface import Interface
from preprocessing import LoginDetails, get_dbs


def main():
    """
    The CONTROLLER of the application. Drives the operation of the application.
    """
    interface = Interface()

    # 1. Login to postgresql
    login_details = LoginDetails
    login_details.host = "localhost"
    login_details.port = "5432"
    login_details.user = "postgres"
    login_details.password = "1111"
    login_details = interface.login(login_details)
    print('host:', login_details.host)
    print('port:', login_details.port)
    print('user:', login_details.user)
    print('pwd:', login_details.password)

    # 2. Connect to db using login details
    db_list = get_dbs(login_details)

    # 1. Choose the database SCHEMA (e.g. TPC-H) and specify the QUERY in the query panel
    query = interface.get_query(login_details, db_list)

    # # 2. Validate the QUERY. If valid, retrieve its QEP and AQP.
    # query_info = preprocessing(res)
    # if query_info['cleaned_query'] == INVALID_INPUT:
    #     interface.invalid_query_input()
    #
    # # 3. Use the QEP and AQP to annotate the file.
    # annotations = annotation()

    # 3. Query panel is updated with annotations

    # 4. Corresponding QEP is visualised in another panel.


if __name__ == '__main__':
    main()
