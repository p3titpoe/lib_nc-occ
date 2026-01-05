from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccActivity(NCOcc):
    def __init__(self,libs:dict = cmdlib.activity):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def send_mails(self)-> str:
        cmd = self._lib['send-mails']['command']
        return self._process([cmd])            
