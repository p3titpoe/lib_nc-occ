from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccTaskprocessingTask(NCOcc):
    def __init__(self,libs:dict = cmdlib.taskprocessing['task']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def cleanup(self)-> str:
        cmd = self._lib['cleanup']['command']
        return self._process([cmd])            

    def get(self,value):
        cmd = self._lib['get']['command']
        return self._process([cmd,value])       

    def list(self)-> str:
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def stats(self)-> str:
        cmd = self._lib['stats']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccTaskprocessingTaskType(NCOcc):
    def __init__(self,libs:dict = cmdlib.taskprocessing['task-type']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def set_enabled(self)-> str:
        cmd = self._lib['set-enabled']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccTaskprocessing(NCOcc):
    def __init__(self,libs:dict = cmdlib.taskprocessing):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def task_type(self)->NCOcc:
        return self._lib['task-type']

    def task(self)->NCOcc:
        return self._lib['task']
