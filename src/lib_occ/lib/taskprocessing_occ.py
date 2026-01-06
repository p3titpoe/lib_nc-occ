from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccTaskprocessingTask(NCOcc):
    def __init__(self,libs:dict = cmdlib.taskprocessing['task']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def cleanup(self):
        "cleanup old tasks"
        cmd = self._lib['cleanup']['command']
        return self._process([cmd])
                    
    def get(self,value) -> str:
        "Display all information for a specific task"
        cmd = self._lib['get']['command']
        return self._process([cmd,value])       

    def lists(self):
        " list tasks"
        cmd = self._lib['list']['command']
        return self._process([cmd])
                    
    def stats(self):
        "get statistics for tasks"
        cmd = self._lib['stats']['command']
        return self._process([cmd])
                    

@dataclass(init=False)
class NcOccTaskprocessingTaskType(NCOcc):
    def __init__(self,libs:dict = cmdlib.taskprocessing['task-type']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def set_enabled(self):
        " Enable or disable a task type"
        cmd = self._lib['set-enabled']['command']
        return self._process([cmd])
                    

@dataclass(init=False)
class NcOccTaskprocessing(NCOcc):
    def __init__(self,libs:dict = cmdlib.taskprocessing):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
        to_create = {
                    'task-type' : NcOccTaskprocessingTask-type,
                    'task' : NcOccTaskprocessingTask,

            }
        self._generate_subobjs(to_create)
        
    @property
    def task_type(self)->NcOccTaskprocessingTaskType:
        "Returns corresponding object :: "
        return self._lib['task-type']

    @property
    def task(self)->NcOccTaskprocessingTask:
        "Returns corresponding object :: "
        return self._lib['task']

