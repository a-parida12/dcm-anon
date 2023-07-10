import datetime


def get_datetime() -> str:
    """Get the datetime equivalent to DT DICOM VR

    Returns:
        str: datetime
    """
    dt = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    return dt


def get_date() -> str:
    """Get the date equivalent to DA DICOM VR

    Returns:
        str: date
    """
    date = str(datetime.datetime.now().strftime("%Y%m%d"))
    return date


def get_time() -> str:
    """Get the time equivalent to TM DICOM VR

    Returns:
        str: time
    """
    time = str(datetime.datetime.now().strftime("%H%M%S"))
    return time
