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
        "list trusted certificates"
        cmd = self._lib['certificates']['command']
        return self._process([cmd])            

    def export(self)-> str:
        " export the certificate bundle"
        cmd = self._lib['export']['command']
        return self._process([cmd])            

    def imports(self)-> str:
        " import trusted certificate in PEM format"
        cmd = self._lib['import']['command']
        return self._process([cmd])            

    def remove(self)-> str:
        " remove trusted certificate"
        cmd = self._lib['remove']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccSecurityBruteforce(NCOcc):
    def __init__(self,libs:dict = cmdlib.security['bruteforce']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        

    def attempts(self)-> str:
        " Show bruteforce attempts status for a given IP address"
        cmd = self._lib['attempts']['command']
        return self._process([cmd])            

    def reset(self)-> str:
        "resets bruteforce attempts for given IP address"
        cmd = self._lib['reset']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccSecurity(NCOcc):
    def __init__(self,libs:dict = cmdlib.security):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
        to_create = {
                    'bruteforce' : NcOccSecurityBruteforce,
                    'certificates' : NcOccSecurityCertificates,

            }
        self._generate_subobjs(to_create)
        

    @property
    def bruteforce(self)->NCOcc:
        "Returns corresponding object :: "
        return self._lib['bruteforce']

    @property
    def certificates(self)->NCOcc:
        "Returns corresponding object :: "
        return self._lib['certificates']
