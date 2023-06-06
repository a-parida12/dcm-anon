import pytest
from dcm_anon.utils.datetime import get_datetime, get_date, get_time
from dcm_anon.utils.hash import encrypt_string, get_digits, get_non_digits




@pytest.mark.base
def test_dummy():
    # remove during dev
    bool_val = True
    assert type(bool_val) == bool
    assert bool_val


@pytest.mark.utils
def test_get_datetime() -> None:
    dt_string = get_datetime()
    assert type(dt_string) == str
    assert len(dt_string) == 14


@pytest.mark.utils
def test_get_date() -> None:
    date = get_date()
    assert type(date) == str
    assert len(date) == 8


@pytest.mark.utils
def test_get_time() -> None:
    time = get_time()
    assert type(time) == str
    assert len(time) == 6


@pytest.mark.utils
def test_encrypt_string() -> None:
    test_string = "test_string"
    hash = encrypt_string(test_string)
    hex_value = "4b641e9a923d1ea57e18fe41dcb543e2c4005c41ff210864a710b0fbb2654c11"
    assert hash == hex_value


@pytest.mark.utils
def test_get_digits() -> None:
    test_string = "1a2b3c"
    op = get_digits(test_string)
    assert op == "123"
    assert type(op) == str


@pytest.mark.utils
def test_get_non_digits() -> None:
    test_string = "1a2b3c"
    op = get_non_digits(test_string)
    assert op == "abc"
    assert type(op) == str