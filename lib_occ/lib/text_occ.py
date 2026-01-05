from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccText(NCOcc):
    def __init__(self,libs:dict = cmdlib.text):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def reset(self)-> str:
        cmd = self._lib['reset']['command']
        return self._process([cmd])            
