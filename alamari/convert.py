from datetime import date


def to_integer(given_input: str):
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
    from re import findall
    if isinstance(given_input, str):
        match = findall('\d+', given_input)
        if match:
            return ",".join(match)
        return 0  # default value
    return given_input  # if not string type


def to_roman(given_text: str) -> str:
    """Converts the given devanagiri text into roman form

    Args:
        given_text (str): devanagiri text

    Returns:
        str: romanized text
    """
    import nepali_roman as nr
    return nr.romanize_text(given_text)


def to_nepali_miti(english_date: date) -> date:
    """Converts english formmated date (international date) into nepali miti

    Args:
        english_date (date): international date

    Returns:
        date: returns nepali date in YY-M-D
    """
    from nepali_datetime import date as nepdate
    return nepdate.from_datetime_date(english_date)
