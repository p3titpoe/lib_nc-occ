from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccNotification(NCOcc):
    def __init__(self,libs:dict = cmdlib.notification):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def delete(self,value) -> str:
        "Delete a generated admin notification for the given user"
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def generate(self):
        "Generate a notification for the given user"
        cmd = self._lib['generate']['command']
        return self._process([cmd])
                    
    def test_push(self):
        " Generate a notification for the given user"
        cmd = self._lib['test-push']['command']
        return self._process([cmd])
                    
