from preprocessing import UserInput, INVALID_INPUT


class Interface:
    """
    The VIEW of the application.

    :returns: Dict['schema': str, 'query': str]
    """

    @staticmethod
    def get_user_input() -> UserInput:
        schema_val = "TPC_H"
        query_val = "SELECT * FROM db"
        res = UserInput()
        res['schema'] = schema_val
        res['query'] = query_val
        return res

    @staticmethod
    def print_invalid_input(self):
        print(INVALID_INPUT)
