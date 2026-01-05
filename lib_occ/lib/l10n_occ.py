from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccL10n(NCOcc):
    def __init__(self,libs:dict = cmdlib.l10n):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def createjs(self)-> str:
        cmd = self._lib['createjs']['command']
        return self._process([cmd])            
