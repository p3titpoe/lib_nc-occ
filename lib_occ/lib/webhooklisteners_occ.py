from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccWebhooklisteners(NCOcc):
    def __init__(self,libs:dict = cmdlib.webhooklisteners):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def lists(self):
        " Lists configured webhook listeners"
        cmd = self._lib['list']['command']
        return self._process([cmd])
                    
