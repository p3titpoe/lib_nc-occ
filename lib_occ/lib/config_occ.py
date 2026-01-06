from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccConfigSystem(NCOcc):
    def __init__(self,libs:dict = cmdlib.config['system']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        

    def delete(self,value):
        " Delete a system config value"
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def get(self,value):
        "Get a system config value"
        cmd = self._lib['get']['command']
        return self._process([cmd,value])       

    def set(self)-> str:
        "Set a system config value"
        cmd = self._lib['set']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccConfigApp(NCOcc):
    def __init__(self,libs:dict = cmdlib.config['app']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        

    def delete(self,value):
        "Delete an app config value"
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def get(self,value):
        " Get an app config value"
        cmd = self._lib['get']['command']
        return self._process([cmd,value])       

    def set(self)-> str:
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
    def app(self)->NCOcc:
        "Returns corresponding object :: "
        return self._lib['app']

    def imports(self)-> str:
        "Import a list of configs"
        cmd = self._lib['import']['command']
        return self._process([cmd])            

    def list(self)-> str:
        "List all configs"
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def preset(self)-> str:
        "Select a config preset"
        cmd = self._lib['preset']['command']
        return self._process([cmd])            

    @property
    def system(self)->NCOcc:
        "Returns corresponding object :: "
        return self._lib['system']
