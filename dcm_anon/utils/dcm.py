from pydicom.errors import InvalidDicomError
from pathlib import Path
import pydicom
from dicom_csv import join_tree


def check_valid_dcm(path: Path) -> bool:
    """check whether given file is a dicom or not

    Args:
        path (Path): path to a dicom file

    Returns:
        bool: boolean value True for dicom else False
    """
    try:
        pydicom.dcmread(path, defer_size=1024)
    except (InvalidDicomError, IsADirectoryError):
        return False

    return True


def bare_bones_ui(ui: str) -> str:
    """Get the main bare bones UID from a dicom header UID

    Args:
        ui (str): incoming ui

    Returns:
        str: the bare bones uid
    """
    all_uids = list(pydicom._uid_dict.UID_dictionary.keys())

    def hammingDist(str1, str2):
        i = 0
        count = 0
        while i < min(len(str1), len(str2)):
            if str1[i].upper() != str2[i].upper():
                count += 1
            i += 1
        return count

    dists = []
    for uid in all_uids:
        hamm_dist = hammingDist(uid, ui)
        if hamm_dist == 0:
            return uid
        dists.append(hamm_dist)

    return all_uids[dists.index(min(dists))]


def get_dicom_csv(parent_folder: str):
    """Generate Dicom header csv

    Args:
        parent_folder (str): folder to crawl for dicoms

    Returns:
        _type_: generated pandas df
    """
    print("Creating CSV File")
    return join_tree(parent_folder, ignore_extensions=[".jpeg", ".jpg", ".png"], verbose=1)
