from datetime import datetime


def url_resolves(any_url: str) -> bool:
    """Checks if the given url resolves sucessfully

    Args:
        any_url (str): the full url of any media, article, content
    Returns:
        bool: returns False if it can't resolve the given link
    """
    from requests import get
    response = get(any_url)
    if response.status_code == 200:
        return True
    return False


def replace(given_text: str, sub_string: str, replacable_str: str) -> str:
    """Replace a substring with another string from a given text.

    Args:
        given_text (str): the full text where to be replaced
        sub_string (str): the string to be replaced
        replacable_str (str): the new replaced string

    Returns:
        str: stripped replaced text
    """
    from re import sub
    return sub(sub_string, replacable_str, given_text).strip()


def parse_date(given_string: str) -> datetime:
    """Parses datetimes from given string

    Args:
        given_string (str): string to parse from

    Returns:
        datetime: returns datetime object
    """
    from dateutil.parser import parse
    return parse(given_string)
