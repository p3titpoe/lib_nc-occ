from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccInfoFile(NCOcc):
    def __init__(self,libs:dict = cmdlib.info['file']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        

    def file(self)-> str:
        "get information for a file"
        cmd = self._lib['file']['command']
        return self._process([cmd])            

    def space(self)-> str:
        "Summarize space usage of specified folder"
        cmd = self._lib['space']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccInfo(NCOcc):
    def __init__(self,libs:dict = cmdlib.info):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
        to_create = {
                    'file' : NcOccInfoFile,

            }
        self._generate_subobjs(to_create)
        

    @property
    def file(self)->NCOcc:
        "Returns corresponding object :: "
        return self._lib['file']

    def storage(self)-> str:
        " Get information a single storage"
        cmd = self._lib['storage']['command']
        return self._process([cmd])            

    def storages(self)-> str:
        "List storages ordered by the number of files"
        cmd = self._lib['storages']['command']
        return self._process([cmd])            
