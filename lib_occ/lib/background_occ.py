from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccBackground(NCOcc):
    def __init__(self,libs:dict = cmdlib.background):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def cron(self)-> str:
        cmd = self._lib['cron']['command']
        return self._process([cmd])            
