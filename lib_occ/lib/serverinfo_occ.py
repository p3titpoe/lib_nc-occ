from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccServerinfo(NCOcc):
    def __init__(self,libs:dict = cmdlib.serverinfo):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def update_storage_statistics(self)-> str:
        cmd = self._lib['update-storage-statistics']['command']
        return self._process([cmd])            
