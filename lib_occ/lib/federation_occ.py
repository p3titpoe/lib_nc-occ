from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccFederation(NCOcc):
    def __init__(self,libs:dict = cmdlib.federation):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def sync_addressbooks(self)-> str:
        cmd = self._lib['sync-addressbooks']['command']
        return self._process([cmd])            

    def sync_calendars(self)-> str:
        cmd = self._lib['sync-calendars']['command']
        return self._process([cmd])            
