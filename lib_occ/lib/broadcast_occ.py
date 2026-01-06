from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccBroadcast(NCOcc):
    def __init__(self,libs:dict = cmdlib.broadcast):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def test(self):
        " test the SSE broadcaster"
        cmd = self._lib['test']['command']
        return self._process([cmd])
                    
