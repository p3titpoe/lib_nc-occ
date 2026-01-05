from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccMemcacheDistributed(NCOcc):
    def __init__(self,libs:dict = cmdlib.memcache['distributed']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def clear(self)-> str:
        cmd = self._lib['clear']['command']
        return self._process([cmd])            

    def delete(self,value):
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def get(self,value):
        cmd = self._lib['get']['command']
        return self._process([cmd,value])       

    def set(self)-> str:
        cmd = self._lib['set']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccMemcache(NCOcc):
    def __init__(self,libs:dict = cmdlib.memcache):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def distributed(self)->NCOcc:
        return self._lib['distributed']

    def redis(self)-> str:
        cmd = self._lib['redis']['command']
        return self._process([cmd])            
