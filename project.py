from interface import Interface
from preprocessing import preprocessing, INVALID_INPUT, LoginDetails
from annotation import annotation


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

    # 1. Choose the database SCHEMA (e.g. TPC-H) and specify the QUERY in the query panel
    res = interface.get_user_input()

    # 2. Validate the QUERY. If valid, retrieve its QEP and AQP.
    query_info = preprocessing(res)
    if query_info['cleaned_query'] == INVALID_INPUT:
        interface.invalid_query_input()

    # 3. Use the QEP and AQP to annotate the file.
    annotations = annotation()

    # 3. Query panel is updated with annotations

    # 4. Corresponding QEP is visualised in another panel.


if __name__ == '__main__':
    main()
