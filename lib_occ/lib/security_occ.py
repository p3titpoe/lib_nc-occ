from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccSecurityCertificates(NCOcc):
    def __init__(self,libs:dict = cmdlib.security['certificates']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def certificates(self)-> str:
        cmd = self._lib['certificates']['command']
        return self._process([cmd])            

    def export(self)-> str:
        cmd = self._lib['export']['command']
        return self._process([cmd])            

    def import_sec(self)-> str:
        cmd = self._lib['import']['command']
        return self._process([cmd])            

    def remove(self)-> str:
        cmd = self._lib['remove']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccSecurityBruteforce(NCOcc):
    def __init__(self,libs:dict = cmdlib.security['bruteforce']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def attempts(self)-> str:
        cmd = self._lib['attempts']['command']
        return self._process([cmd])            

    def reset(self)-> str:
        cmd = self._lib['reset']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccSecurity(NCOcc):
    def __init__(self,libs:dict = cmdlib.security):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def bruteforce(self)->NCOcc:
        return self._lib['bruteforce']

    def certificates(self)->NCOcc:
        return self._lib['certificates']
