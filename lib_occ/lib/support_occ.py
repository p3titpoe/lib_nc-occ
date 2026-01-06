from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccSupport(NCOcc):
    def __init__(self,libs:dict = cmdlib.support):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def report(self):
        " Generate a system report"
        cmd = self._lib['report']['command']
        return self._process([cmd])
                    
