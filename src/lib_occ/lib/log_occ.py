from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccLog(NCOcc):
    def __init__(self,libs:dict = cmdlib.log):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def file(self):
        " manipulate logging backend"
        cmd = self._lib['file']['command']
        return self._process([cmd])
                    
    def manage(self):
        " manage logging configuration"
        cmd = self._lib['manage']['command']
        return self._process([cmd])
                    
    def tail(self):
        " Tail the nextcloud logfile"
        cmd = self._lib['tail']['command']
        return self._process([cmd])
                    
    def watch(self):
        "Watch the nextcloud logfile"
        cmd = self._lib['watch']['command']
        return self._process([cmd])
                    
