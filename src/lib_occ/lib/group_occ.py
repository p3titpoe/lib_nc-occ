from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccGroup(NCOcc):
    def __init__(self,libs:dict = cmdlib.group):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def add(self,value) -> str:
        "Add a group"
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def adduser(self):
        "add a user to a group"
        cmd = self._lib['adduser']['command']
        return self._process([cmd])
                    
    def delete(self,value) -> str:
        " Remove a group"
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def info(self):
        " Show information about a group"
        cmd = self._lib['info']['command']
        return self._process([cmd])
                    
    def lists(self):
        " list configured groups"
        cmd = self._lib['list']['command']
        return self._process([cmd])
                    
    def removeuser(self):
        " remove a user from a group"
        cmd = self._lib['removeuser']['command']
        return self._process([cmd])
                    
