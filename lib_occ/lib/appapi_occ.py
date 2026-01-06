from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccAppapiDaemonRegistry(NCOcc):
    def __init__(self,libs:dict = cmdlib.appapi['daemon']['registry']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        

    def add(self,value):
        "Add Deploy daemon Docker registry mapping"
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def list(self)-> str:
        " List configured Deploy daemon Docker registry mappings"
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def remove(self)-> str:
        " Remove Deploy daemon Docker registry mapping"
        cmd = self._lib['remove']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccAppapiDaemon(NCOcc):
    def __init__(self,libs:dict = cmdlib.appapi['daemon']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
        to_create = {
                    'registry' : NcOccAppapiDaemonRegistry,

            }
        self._generate_subobjs(to_create)
        

    def list(self)-> str:
        "List registered daemons"
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def register(self)-> str:
        "Register daemon config for ExApp deployment"
        cmd = self._lib['register']['command']
        return self._process([cmd])            

    @property
    def registry(self)->NCOcc:
        "Returns corresponding object :: "
        return self._lib['registry']

    def unregister(self)-> str:
        "Unregister daemon"
        cmd = self._lib['unregister']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccAppapiAppConfig(NCOcc):
    def __init__(self,libs:dict = cmdlib.appapi['app']['config']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        

    def delete(self,value):
        "Delete ExApp configs"
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def get(self,value):
        " Get ExApp config"
        cmd = self._lib['get']['command']
        return self._process([cmd,value])       

    def list(self)-> str:
        "List ExApp configs"
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def set(self)-> str:
        " Set ExApp config"
        cmd = self._lib['set']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccAppapiApp(NCOcc):
    def __init__(self,libs:dict = cmdlib.appapi['app']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
        to_create = {
                    'config' : NcOccAppapiAppConfig,

            }
        self._generate_subobjs(to_create)
        

    @property
    def config(self)->NCOcc:
        "Returns corresponding object :: "
        return self._lib['config']

    def disable(self)-> str:
        "Disable registered external app"
        cmd = self._lib['disable']['command']
        return self._process([cmd])            

    def enable(self)-> str:
        " Enable registered external app"
        cmd = self._lib['enable']['command']
        return self._process([cmd])            

    def list(self)-> str:
        " List ExApps"
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def register(self)-> str:
        " Install external App"
        cmd = self._lib['register']['command']
        return self._process([cmd])            

    def unregister(self)-> str:
        " Unregister external app"
        cmd = self._lib['unregister']['command']
        return self._process([cmd])            

    def update(self,value):
        " Update ExApp"
        cmd = self._lib['update']['command']
        return self._process([cmd,value])       

@dataclass(init=False)
class NcOccAppapi(NCOcc):
    def __init__(self,libs:dict = cmdlib.appapi):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
        to_create = {
                    'app' : NcOccAppapiApp,
                    'daemon' : NcOccAppapiDaemon,

            }
        self._generate_subobjs(to_create)
        

    @property
    def app(self)->NCOcc:
        "Returns corresponding object :: "
        return self._lib['app']

    @property
    def daemon(self)->NCOcc:
        "Returns corresponding object :: "
        return self._lib['daemon']
