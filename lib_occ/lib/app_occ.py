from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccApp(NCOcc):
    def __init__(self,libs:dict = cmdlib.app):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def disable(self)-> str:
        cmd = self._lib['disable']['command']
        return self._process([cmd])            

    def enable(self)-> str:
        cmd = self._lib['enable']['command']
        return self._process([cmd])            

    def getpath(self)-> str:
        cmd = self._lib['getpath']['command']
        return self._process([cmd])            

    def install(self)-> str:
        cmd = self._lib['install']['command']
        return self._process([cmd])            

    def list(self)-> str:
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def remove(self)-> str:
        cmd = self._lib['remove']['command']
        return self._process([cmd])            

    def update(self,value):
        cmd = self._lib['update']['command']
        return self._process([cmd,value])       
