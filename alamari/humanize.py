from datetime import datetime
from typing import Optional, Union

import arrow

Number = Union[int, float, str]


def number(any_num: Number, padding: Optional[bool] = False) -> str:
    """Formats number in nepali counting form replacing the international format

    Args:
        any_num (Number): The number to be formatted
        padding (bool, optional): Defaults to False. If padding is required in any number less than 10.

    Syntax:
    >>> number(any_num, padding)

    Example:

    >>> number(any_num = 9, padding = True)
    09

    >>> number(any_num = 9.54, padding = True)
    09

    Returns:
        str: returns a string in comma separated number
    """
    int_part, *float_part = str(any_num).partition(".")
    separated_num = [int_part[x-2:x]
                     for x in range(-3, -len(int_part), -2)][::-1] + [int_part[-3:]]
    number_with_commas = ",".join(separated_num)
    if padding and int(int_part) < 10:
        return f"0{int_part}"
    return "".join([number_with_commas] + float_part)


def date(any_date: datetime) -> str:
    """Converts any given date into humanized form (UTC)

    Syntax:
    >>> date(any_date)

    Example:

    >>> date(any_date = 2021-06-02 05:55:55.185035)
    2 hours ago

    Args:
        any_date (datetime): any date with datetime format

    Returns:
        [type]: Returns date in humanized form
    """
    return arrow.get(any_date).to('US/Pacific').humanize()


def nepal_date(local_date: datetime) -> str:
    """Converts datetime into humanized form (NPT)

    Syntax:
    >>> nepal_date(local_date)

    Example:

    >>> nepal_date(local_date = 2021-06-02 05:55:55.185035)
    just now

    Args:
        local_date (datetime): any local date with datetime format

    Returns:
        [type]: Returns date in humanized form
    """
    return arrow.get(local_date).shift(minutes=-345).to('US/Pacific').humanize()
