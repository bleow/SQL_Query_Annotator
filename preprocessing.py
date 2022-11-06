from typing import TypedDict

INVALID_INPUT = "Input query is not valid."

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


def preprocessing(user_input: UserInput) -> QueryInfo:
    """
    The pre-ALGORITHM of the application. Reads and parses input for the annotation class.
    Also contains the business objects related to the application.

    :returns: String of cleaned query OR False if user input is invalid
    """

    cleaned_query = user_input['query'].strip()
    aqp = 'aqp'
    qep = 'qep'

    invalid: bool = False
    if invalid:
        return QueryInfo(cleaned_query=INVALID_INPUT, qep=INVALID_INPUT, aqp=INVALID_INPUT)

    return QueryInfo(cleaned_query=cleaned_query, qep=qep, aqp=aqp)
