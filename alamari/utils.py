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


def crop_image(image):
    # Image object : Pillow Image
    # crops the image from the center
    full_width, full_height = image.size
    width = min(image.size)
    height = min(image.size)
    return image.crop(((full_width - width) // 2, (full_height - height) // 2, (full_width + width) // 2, (full_height + height) // 2))


def ordinalize(given_number: int) -> str:
    """Ordinalize the number from the given number

    Args:
        given_number (int): integer number

    Example:
    >>> ordinalize(34)
    '34th'

    Returns:
        str: string in ordinal form
    """
    suffix = ["th", "st", "nd", "rd"]
    thenum = int(given_number)
    if thenum % 10 in [1, 2, 3] and thenum not in [11, 12, 13]:
        return f'{thenum}{suffix[thenum % 10]}'
    else:
        return f'{thenum}{suffix[0]}'


def pluralize(given_noun: str, quantity: int = 2, suffix: str = None) -> str:
    """Pluralize the given noun with suitable suffix

    Args:
        given_noun (str): string to be pluralized
        quantity (int): quantity to be pluralized (defaults to 2)
        suffix (str, optional): custom suffix to be used if not specified before (defaults to None)

    Returns:
        str: string in plural form
    """
    from re import search, sub
    if quantity > 1:
        if search('[sxz]$', given_noun):
            return sub('$', 'es', given_noun)
        elif search('[^aeioudgkprt]h$', given_noun):
            return sub('$', 'es', given_noun)
        elif search('[aeiou]y$', given_noun):
            return sub('y$', 'ies', given_noun)
        else:
            if suffix is not None:
                return given_noun + suffix
            return given_noun + 's'
    return given_noun
