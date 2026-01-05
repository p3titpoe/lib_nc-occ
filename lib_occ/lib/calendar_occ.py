from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccCalendar(NCOcc):
    def __init__(self,libs:dict = cmdlib.calendar):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def export(self)-> str:
        cmd = self._lib['export']['command']
        return self._process([cmd])            

    def import_cal(self)-> str:
        cmd = self._lib['import']['command']
        return self._process([cmd])            
