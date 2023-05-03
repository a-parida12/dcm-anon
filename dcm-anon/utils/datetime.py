import re, string
import datetime

def get_datetime()->str:
    """Get the datetime equivalent to DT DICOM VR

    Returns:
        str: datetime
    """
    x = str(datetime.datetime.now()).replace(' ', '')
    return re.sub('[%s]' % re.escape(string.punctuation), '', x)[:14]

def get_date()->str:
    """ Get the date equivalent to DA DICOM VR

    Returns:
        str: date
    """
    return  get_datetime()[:8]

def get_time()->str:
    """Get the time equivalent to TM DICOM VR

    Returns:
        str: time
    """
    return  get_datetime()[8:]