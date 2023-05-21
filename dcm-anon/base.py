from abc import ABC, abstractmethod
from utils.datetime import get_date, get_datetime, get_time
from utils.dcm import bare_bones_ui
from utils.hash import get_digits, get_non_digits, encrypt_string
from utils.tags import anon_tags
from pydicom.dataelem import DataElement


class Anonimizer(ABC):
    def __init__(self, deep_anon: bool = False):
        """Base Anonimizer Class

        Args:
            deep_anon (bool, optional): update all fields with None. Defaults to False.
        """
        self.deep_anon = deep_anon

        if self.deep_anon:
            raise Warning("Deep Anonimisation has been set; Ignoring DCM standard conformality")
        self.annon_tags = anon_tags

    def anonimise_element(self, elem: DataElement) -> DataElement:
        """Anonimize a DataElement type object based on its DICOM VR

        Args:
            elem (DataElement): elem to be anonimised

        Raises:
            NotImplementedError: unknown VR identified

        Returns:
            DataElement: anonimized elem
        """
        # not anonimising
        if elem.VR in ["CS"]:
            # ['Code Strings']
            return elem

        # skipping VRs
        if elem.VR in [
            "AE",
            "AS",
            "AT",
            "DS",
            "FL",
            "FD",
            "IS",
            "SL",
            "SS",
            "SV",
            "UC",
            "UL",
            "US",
            "UV",
        ]:
            # ['Application Entity', 'Age String', 'Attribute Tag', 'Decimal String', 'Floating Point Single', 'Floating Point Double'
            # 'Integer String', 'Signed Long', 'Signed Short', 'Signed 64-bit Very Long', 'Unlimited Characters', 'Unsigned Long', 'Unsigned Short'
            # 'Unsigned 64-bit Very Long']
            return elem

        if self.deep_anon:
            elem.value = "None"
            return elem

        # Anonimize UIDs
        if "UI" == elem.VR:
            base_ui = bare_bones_ui(elem.value)
            if base_ui != elem.value:
                new_ui = base_ui + "." + get_digits(encrypt_string(elem.value))
                if len(new_ui) > 64:
                    new_ui = new_ui[:64]
                elem.value = new_ui

        # Anonimize Person Name
        elif "PN" == elem.VR:
            elem.value = get_non_digits(encrypt_string(elem.value))

        # Anonimise Dates and time
        elif "DA" == elem.VR:
            elem.value = get_date()
        elif "DT" == elem.VR:
            elem.value = get_datetime()
        elif "TM" == elem.VR:
            elem.value = get_time()

        # optional text fields --> remove
        elif elem.VR in ["LT", "ST", "UR", "UT"]:
            if str(elem.tag)[1:-1].replace(" ", "") in self.annon_tags:
                elem.value = "None"

        # optional byte fields --> remove
        elif elem.VR in ["OB", "OD", "OF", "OL", "OV", "OW", "UN"]:
            if str(elem.tag)[1:-1].replace(" ", "") in self.annon_tags:
                elem.value = ""

        # Anonimise all short and long text in dicom tags that need to be removed
        elif elem.VR in ["SH", "LO"]:
            if elem.value != "" and str(elem.tag)[1:-1].replace(" ", "") in self.annon_tags:
                if (
                    "NUMBER" in elem.name.upper()
                    or "SEQUENCE" in elem.name.upper()
                    or "ID" in elem.name.upper()
                ):
                    elem.value = (
                        get_digits(encrypt_string(elem.value))
                        if elem.VR == "LO"
                        else get_digits(encrypt_string(elem.value))[:16]
                    )  # 'None'
                else:
                    elem.value = (
                        get_non_digits(encrypt_string(str(elem.value)))
                        if elem.VR == "LO"
                        else get_digits(encrypt_string(elem.value))[:16]
                    )  # 'None'

        # annonimize sequences data
        elif "SQ" == elem.VR:
            for seqelem in elem:
                for inelem in seqelem:
                    seqelem[inelem.tag] = self.anonimise_element(inelem)
        else:
            raise NotImplementedError(
                f"Unknown VR {elem.VR}.Please report to the developers of dcm-anon."
            )
        return elem

    @abstractmethod
    def run(self, input: str, output: str) -> None:
        raise NotImplementedError("Implementation of the conversion method coming soon")
