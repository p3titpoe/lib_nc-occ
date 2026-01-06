from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccTheming(NCOcc):
    def __init__(self,libs:dict = cmdlib.theming):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def config(self):
        " Set theming app config values"
        cmd = self._lib['config']['command']
        return self._process([cmd])
                    
