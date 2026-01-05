from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccGroup(NCOcc):
    def __init__(self,libs:dict = cmdlib.group):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def add(self,value):
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def adduser(self)-> str:
        cmd = self._lib['adduser']['command']
        return self._process([cmd])            

    def delete(self,value):
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def info(self)-> str:
        cmd = self._lib['info']['command']
        return self._process([cmd])            

    def list(self)-> str:
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def removeuser(self)-> str:
        cmd = self._lib['removeuser']['command']
        return self._process([cmd])            
