from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccPreview(NCOcc):
    def __init__(self,libs:dict = cmdlib.preview):
        if libs is None:
            libs = {}
        super().__init__(libs)
        

    def cleanup(self)-> str:
        "Removes existing preview files"
        cmd = self._lib['cleanup']['command']
        return self._process([cmd])            

    def generate(self)-> str:
        " generate a preview for a file"
        cmd = self._lib['generate']['command']
        return self._process([cmd])            

    def repair(self)-> str:
        " distributes the existing previews into subfolders"
        cmd = self._lib['repair']['command']
        return self._process([cmd])            

    def reset_rendered_texts(self)-> str:
        " Deletes all generated avatars and previews of text and md files"
        cmd = self._lib['reset-rendered-texts']['command']
        return self._process([cmd])            
