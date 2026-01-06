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
        " Clear values from the distributed memcache"
        cmd = self._lib['clear']['command']
        return self._process([cmd])            

    def delete(self,value):
        "Delete a value in the distributed memcache"
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def get(self,value):
        " Get a value from the distributed memcache"
        cmd = self._lib['get']['command']
        return self._process([cmd,value])       

    def set(self)-> str:
        " Set a value in the distributed memcache"
        cmd = self._lib['set']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccMemcache(NCOcc):
    def __init__(self,libs:dict = cmdlib.memcache):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
        to_create = {
                    'distributed' : NcOccMemcacheDistributed,

            }
        self._generate_subobjs(to_create)
        

    @property
    def distributed(self)->NCOcc:
        "Returns corresponding object :: "
        return self._lib['distributed']

    def redis(self)-> str:
        ""
        cmd = self._lib['redis']['command']
        return self._process([cmd])            
