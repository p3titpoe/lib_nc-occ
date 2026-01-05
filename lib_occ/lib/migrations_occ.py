from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccMigrations(NCOcc):
    def __init__(self,libs:dict = cmdlib.migrations):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def preview(self)-> str:
        cmd = self._lib['preview']['command']
        return self._process([cmd])            
