from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccConfigSystem(NCOcc):
    def __init__(self,libs:dict = cmdlib.config['system']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def delete(self,value) -> str:
        " Delete a system config value"
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def get(self,value) -> str:
        "Get a system config value"
        cmd = self._lib['get']['command']
        return self._process([cmd,value])       

    def set(self):
        "Set a system config value"
        cmd = self._lib['set']['command']
        return self._process([cmd])
                    

@dataclass(init=False)
class NcOccConfigApp(NCOcc):
    def __init__(self,libs:dict = cmdlib.config['app']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def delete(self,value) -> str:
        "Delete an app config value"
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def get(self,value) -> str:
        " Get an app config value"
        cmd = self._lib['get']['command']
        return self._process([cmd,value])       

    def set(self):
        " Set an app config value"
        cmd = self._lib['set']['command']
        return self._process([cmd])
                    

@dataclass(init=False)
class NcOccConfig(NCOcc):
    def __init__(self,libs:dict = cmdlib.config):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
        to_create = {
                    'app' : NcOccConfigApp,
                    'system' : NcOccConfigSystem,

            }
        self._generate_subobjs(to_create)
        
    @property
    def app(self)->NcOccConfigApp:
        "Returns corresponding object :: "
        return self._lib['app']

    def imports(self):
        "Import a list of configs"
        cmd = self._lib['import']['command']
        return self._process([cmd])
                    
    def lists(self):
        "List all configs"
        cmd = self._lib['list']['command']
        return self._process([cmd])
                    
    def preset(self):
        "Select a config preset"
        cmd = self._lib['preset']['command']
        return self._process([cmd])
                    
    @property
    def system(self)->NcOccConfigSystem:
        "Returns corresponding object :: "
        return self._lib['system']

