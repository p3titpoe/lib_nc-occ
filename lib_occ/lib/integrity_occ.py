from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccIntegrity(NCOcc):
    def __init__(self,libs:dict = cmdlib.integrity):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def check_app(self)-> str:
        cmd = self._lib['check-app']['command']
        return self._process([cmd])            

    def check_core(self)-> str:
        cmd = self._lib['check-core']['command']
        return self._process([cmd])            

    def sign_app(self)-> str:
        cmd = self._lib['sign-app']['command']
        return self._process([cmd])            

    def sign_core(self)-> str:
        cmd = self._lib['sign-core']['command']
        return self._process([cmd])            
