from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccCommon(NCOcc):
    def __init__(self,libs:dict = cmdlib.common):
        if libs is None:
            libs = {}
        super().__init__(libs)
    

    def check(self)-> str:
        cmd = self._lib['check']['command']
        return self._process([cmd])            

    def completion(self)-> str:
        cmd = self._lib['completion']['command']
        return self._process([cmd])            

    def help(self)-> str:
        cmd = self._lib['help']['command']
        return self._process([cmd])            

    def list(self)-> str:
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def setupchecks(self)-> str:
        cmd = self._lib['setupchecks']['command']
        return self._process([cmd])            

    def status(self)-> str:
        cmd = self._lib['status']['command']
        return self._process([cmd])            

    def upgrade(self)-> str:
        cmd = self._lib['upgrade']['command']
        return self._process([cmd])            
