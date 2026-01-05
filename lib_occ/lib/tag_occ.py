from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccTagFiles(NCOcc):
    def __init__(self,libs:dict = cmdlib.tag['files']):
        super().__init__(_lib=libs)

    def add(self,value):
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def delete(self,value):
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def delete_all(self)-> str:
        cmd = self._lib['delete-all']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccTag(NCOcc):

    def __init__(self,libs:dict = cmdlib.tag):
        print(libs)
        if libs is None:
            libs = {}
        super().__init__(libs)

    def add(self,value):
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def delete(self,value):
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def edit(self,value):
        cmd = self._lib['edit']['command']
        return self._process([cmd,value])       

    def files(self)->NCOcc:
        return self._lib['files']

    def list(self)-> str:
        cmd = self._lib['list']['command']
        return self._process([cmd])            
