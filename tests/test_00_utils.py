import pytest
from dcm_anon.utils.datetime import get_datetime, get_date, get_time
from dcm_anon.utils.hash import encrypt_string, get_digits, get_non_digits
from dcm_anon.utils.dcm import check_valid_dcm  # , bare_bones_ui, get_dicom_csv


@pytest.fixture
def tests_data():
    yield "./tests/data/"


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


@pytest.mark.utils
def test_check_valid_dcm(tests_data):
    dicom_file = tests_data + "test1"
    assert check_valid_dcm(dicom_file) is True

    dicom_file = tests_data + "test2"
    assert check_valid_dcm(dicom_file) is True


@pytest.mark.utils
def test_check_invalid_dcm(tests_data):
    file = tests_data + "test_dcm.txt"
    assert check_valid_dcm(file) is False


@pytest.mark.utils
def test_bare_bones_ui():
    pass


@pytest.mark.utils
def test_get_dicom_csv():
    pass