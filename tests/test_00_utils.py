import pytest


@pytest.mark.base
def test_dummy():
    # remove during dev
    bool_val = True
    assert type(bool_val) == bool
    assert bool_val


@pytest.mark.utils
def test_getdatetime():
    pass


@pytest.mark.utils
def test_get_date():
    pass


@pytest.mark.utils
def test_get_time():
    pass
