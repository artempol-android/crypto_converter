import re

from AppExceptions import IncorrectInputError


def check_input(data):
    if not re.fullmatch(r"[0-9]+(\.[0-9]+)?", data):
        raise IncorrectInputError()
