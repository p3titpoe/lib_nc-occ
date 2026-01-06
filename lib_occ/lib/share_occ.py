from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccShare(NCOcc):
    def __init__(self,libs:dict = cmdlib.share):
        if libs is None:
            libs = {}
        super().__init__(libs)
        

    def list(self)-> str:
        " List available shares"
        cmd = self._lib['list']['command']
        return self._process([cmd])            
