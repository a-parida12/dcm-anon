from itertools import filterfalse
import hashlib


def encrypt_string(hash_string: str) -> str:
    """encrypt a string using the SHA256 algorithm

    Args:
        hash_string (str): The string that needs to be hashed

    Returns:
        str: the SHA256 hex digest
    """
    return hashlib.sha256(hash_string.encode()).hexdigest()


def get_digits(strin: str) -> str:
    """get all the digits from a mixed sequence

    Args:
        strin (str): mixed sequence string

    Returns:
        str: string of all digits
    """
    digits = "".join(filter(str.isdigit, strin))
    if digits[0] == "0":
        digits = "1" + digits
    return digits


def get_non_digits(strin: str) -> str:
    """get all the alphabets from a mixed sequence

    Args:
        strin (str): mixed sequence string

    Returns:
        str: string of all alphabets
    """
    return "".join(filterfalse(str.isdigit, strin))
