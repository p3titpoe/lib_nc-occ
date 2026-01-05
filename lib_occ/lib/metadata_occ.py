from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccMetadata(NCOcc):
    def __init__(self,libs:dict = cmdlib.metadata):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def get(self,value):
        cmd = self._lib['get']['command']
        return self._process([cmd,value])       
