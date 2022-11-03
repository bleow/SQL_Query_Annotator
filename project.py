from interface import Interface
from preprocessing import preprocessing, INVALID_INPUT
from annotation import annotation


def main():
    """
    The CONTROLLER of the application. Drives the operation of the application.
    """
    # 1. Choose the database SCHEMA (e.g. TPC-H) and specify the QUERY in the query panel
    res = Interface.get_user_input()

    # 2. Validate the QUERY. If valid, retrieve its QEP and AQP.
    query_info = preprocessing(res)
    if query_info['cleaned_query'] == INVALID_INPUT:
        Interface.invalid_query_input()

    # 3. Use the QEP and AQP to annotate the file.
    annotations = annotation(query_info)

    # 3. Query panel is updated with annotations

    # 4. Corresponding QEP is visualised in another panel.


if __name__ == '__main__':
    main()
