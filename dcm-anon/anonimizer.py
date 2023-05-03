from .base import Anonimizer
from pydicom.dataset import FileDataset
import tqdm
import os
import pydicom
from utils.dcm import check_valid_dcm
import glob

class dsAnonimizer(Anonimizer):
    def __init__(self, deep_anon:bool=False, remove_pvt_tags:bool=True):
        super().__init__(deep_anon)
        self.remove_pvt_tags = remove_pvt_tags

    def anonimize(self, dataset:FileDataset)->FileDataset:
        """ anonimise a pydicom dataset

        Args:
            dataset (FileDataset): dataset to be anonimised

        Returns:
            FileDataset: anonimised dataset
        """
        # remove private tags
        if self.remove_pvt_tags:
            dataset.remove_private_tags()
        # store all anonimised tag
        for elem in dataset:
            elem = self.anonimise_element(elem)
            dataset[elem.tag] = elem

        return dataset
    
class fileAnonimizer(dsAnonimizer):
    def __init__(self, deep_anon:bool=False, remove_pvt_tags:bool=True):
        super().__init__(deep_anon, remove_pvt_tags)

    def anonimize_file(self, input:str, output:str):
        dataset = pydicom.dcmread(input, force=True)
        dataset =  self.anonimise(dataset)
        dataset.save_as(output)
 
    def run(self, input:str, output:str)->None:
        self.anonimize_file(input, output)
        

class folderAnonimizer(fileAnonimizer):
    def __init__(self, deep_anon:bool=False, remove_pvt_tags:bool=True):
        super().__init__(deep_anon, remove_pvt_tags)
 
    def run(self, input:str, output:str)->None:
        files = sorted(glob.glob(os.path.join(input+'*')))
        dcm_files = [file for file in files if check_valid_dcm(file)]

        print(f"Found {len(files)} in given folder out of which {len(dcm_files)} are DCMs")
        print("Anonimising all DCMs")
        for i, dcm in enumerate(tqdm.tqdm(dcm_files)):
            out_file_path = os.path.join(output, str(i)+'.dcm')
            self.anonimize_file(dcm, out_file_path)



    
