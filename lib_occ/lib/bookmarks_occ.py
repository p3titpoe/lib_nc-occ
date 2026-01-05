from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccBookmarks(NCOcc):
    def __init__(self,libs:dict = cmdlib.bookmarks):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def clear_previews(self)-> str:
        cmd = self._lib['clear-previews']['command']
        return self._process([cmd])            
