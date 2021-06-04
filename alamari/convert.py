from alamari.humanize import Number
import nepali_roman as nr
import re


def to_integer(given_input: str) -> Number:
    """
    Finds the number in a given input(should be a string with numbers) using regular expression.

    >>> to_integer('abc')
    0
    >>> to_integer('1')
    1
    >>> to_integer('abc123')
    123
    >>> to_integer('abc123abc')
    123
    >>> to_integer('abc123abc456')
    123,456

    Args:
        given_input (str): any text with numbers in it

    Returns:
        Number: returns number in a comma separated form if found else returns 0
    """

    if isinstance(given_input, str):
        match = re.findall('\d+', given_input)
        if match:
            return ",".join(match)
        return 0  # default value
    return given_input  # if not string type

