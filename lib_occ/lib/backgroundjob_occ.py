from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccBackgroundjob(NCOcc):
    def __init__(self,libs:dict = cmdlib.backgroundjob):
        if libs is None:
            libs = {}
        super().__init__(libs)
        

    def delete(self,value):
        "Remove a background job from database"
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def execute(self)-> str:
        " Execute a single background job manually"
        cmd = self._lib['execute']['command']
        return self._process([cmd])            

    def list(self)-> str:
        "List background jobs"
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def worker(self)-> str:
        "Run a background job worker"
        cmd = self._lib['worker']['command']
        return self._process([cmd])            
