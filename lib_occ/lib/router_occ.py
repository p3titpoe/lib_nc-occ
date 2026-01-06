from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccRouter(NCOcc):
    def __init__(self,libs:dict = cmdlib.router):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def lists(self):
        "Find the target of a route or all routes of an app"
        cmd = self._lib['list']['command']
        return self._process([cmd])
                    
    def match(self):
        " Match a URL to the target route"
        cmd = self._lib['match']['command']
        return self._process([cmd])
                    
