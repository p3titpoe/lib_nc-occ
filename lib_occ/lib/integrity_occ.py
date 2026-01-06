from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccIntegrity(NCOcc):
    def __init__(self,libs:dict = cmdlib.integrity):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def check_app(self):
        "Check integrity of an app using a signature"
        cmd = self._lib['check-app']['command']
        return self._process([cmd])
                    
    def check_core(self):
        " Check integrity of core code using a signature"
        cmd = self._lib['check-core']['command']
        return self._process([cmd])
                    
    def sign_app(self):
        " Signs an app using a private key"
        cmd = self._lib['sign-app']['command']
        return self._process([cmd])
                    
    def sign_core(self):
        "Sign core using a private key"
        cmd = self._lib['sign-core']['command']
        return self._process([cmd])
                    
