from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccUpdate(NCOcc):
    def __init__(self,libs:dict = cmdlib.update):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def check(self)-> str:
        cmd = self._lib['check']['command']
        return self._process([cmd])            
