from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccTrashbin(NCOcc):
    def __init__(self,libs:dict = cmdlib.trashbin):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def cleanup(self)-> str:
        cmd = self._lib['cleanup']['command']
        return self._process([cmd])            

    def expire(self)-> str:
        cmd = self._lib['expire']['command']
        return self._process([cmd])            

    def restore(self)-> str:
        cmd = self._lib['restore']['command']
        return self._process([cmd])            

    def size(self)-> str:
        cmd = self._lib['size']['command']
        return self._process([cmd])            
