import pytest
from dcm_anon.utils.datetime import get_datetime, get_date, get_time


@pytest.mark.base
def test_dummy():
    # remove during dev
    bool_val = True
    assert type(bool_val) == bool
    assert bool_val


@pytest.mark.utils
def test_get_datetime():
    dt_string = get_datetime()
    assert type(dt_string) == str
    assert len(dt_string) == 14


@pytest.mark.utils
def test_get_date():
    date = get_date()
    assert type(date) == str
    assert len(date) == 8


@pytest.mark.utils
def test_get_time():
    time = get_time()
    assert type(time) == str
    assert len(time) == 6
