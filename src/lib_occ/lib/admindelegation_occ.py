from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccAdmindelegation(NCOcc):
    def __init__(self,libs:dict = cmdlib.admindelegation):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def add(self,value) -> str:
        " add setting delegation to a group"
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def remove(self):
        "remove settings delegation from a group"
        cmd = self._lib['remove']['command']
        return self._process([cmd])
                    
    def show(self):
        "show delegated settings"
        cmd = self._lib['show']['command']
        return self._process([cmd])
                    
