from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccTagFiles(NCOcc):
    def __init__(self,libs:dict = cmdlib.tag['files']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def add(self,value) -> str:
        "Add a systemtag to a file or folder"
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def delete(self,value) -> str:
        " Delete a systemtag from a file or folder"
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def delete_all(self):
        " Delete all systemtags from a file or folder"
        cmd = self._lib['delete-all']['command']
        return self._process([cmd])
                    

@dataclass(init=False)
class NcOccTag(NCOcc):
    def __init__(self,libs:dict = cmdlib.tag):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
        to_create = {
                    'files' : NcOccTagFiles,

            }
        self._generate_subobjs(to_create)
        
    def add(self,value) -> str:
        "Add new tag"
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def delete(self,value) -> str:
        " delete a tag"
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def edit(self,value) -> str:
        " edit tag attributes"
        cmd = self._lib['edit']['command']
        return self._process([cmd,value])       

    @property
    def files(self)->NcOccTagFiles:
        "Returns corresponding object :: "
        return self._lib['files']

    def lists(self):
        " list tags"
        cmd = self._lib['list']['command']
        return self._process([cmd])
                    
