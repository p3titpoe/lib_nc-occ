from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccTwofactorauth(NCOcc):
    def __init__(self,libs:dict = cmdlib.twofactorauth):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def cleanup(self)-> str:
        cmd = self._lib['cleanup']['command']
        return self._process([cmd])            

    def disable(self)-> str:
        cmd = self._lib['disable']['command']
        return self._process([cmd])            

    def enable(self)-> str:
        cmd = self._lib['enable']['command']
        return self._process([cmd])            

    def enforce(self)-> str:
        cmd = self._lib['enforce']['command']
        return self._process([cmd])            

    def state(self)-> str:
        cmd = self._lib['state']['command']
        return self._process([cmd])            
