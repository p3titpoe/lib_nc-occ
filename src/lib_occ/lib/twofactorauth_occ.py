from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccTwofactorauth(NCOcc):
    def __init__(self,libs:dict = cmdlib.twofactorauth):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def cleanup(self):
        "Clean up the twofactor userprovider association of an uninstalledremoved provider"
        cmd = self._lib['cleanup']['command']
        return self._process([cmd])
                    
    def disable(self):
        "Disable twofactor authentication for a user"
        cmd = self._lib['disable']['command']
        return self._process([cmd])
                    
    def enable(self):
        " Enable twofactor authentication for a user"
        cmd = self._lib['enable']['command']
        return self._process([cmd])
                    
    def enforce(self):
        "Enableddisable enforced twofactor authentication"
        cmd = self._lib['enforce']['command']
        return self._process([cmd])
                    
    def state(self):
        "Get the twofactor authentication 2FA state of a user"
        cmd = self._lib['state']['command']
        return self._process([cmd])
                    
