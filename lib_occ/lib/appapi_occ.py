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
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def list(self)-> str:
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def remove(self)-> str:
        cmd = self._lib['remove']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccAppapiDaemon(NCOcc):
    def __init__(self,libs:dict = cmdlib.appapi['daemon']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def list(self)-> str:
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def register(self)-> str:
        cmd = self._lib['register']['command']
        return self._process([cmd])            

    def registry(self)->NCOcc:
        return self._lib['registry']

    def unregister(self)-> str:
        cmd = self._lib['unregister']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccAppapiAppConfig(NCOcc):
    def __init__(self,libs:dict = cmdlib.appapi['app']['config']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def delete(self,value):
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def get(self,value):
        cmd = self._lib['get']['command']
        return self._process([cmd,value])       

    def list(self)-> str:
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def set(self)-> str:
        cmd = self._lib['set']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccAppapiApp(NCOcc):
    def __init__(self,libs:dict = cmdlib.appapi['app']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def config(self)->NCOcc:
        return self._lib['config']

    def disable(self)-> str:
        cmd = self._lib['disable']['command']
        return self._process([cmd])            

    def enable(self)-> str:
        cmd = self._lib['enable']['command']
        return self._process([cmd])            

    def list(self)-> str:
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def register(self)-> str:
        cmd = self._lib['register']['command']
        return self._process([cmd])            

    def unregister(self)-> str:
        cmd = self._lib['unregister']['command']
        return self._process([cmd])            

    def update(self,value):
        cmd = self._lib['update']['command']
        return self._process([cmd,value])       

@dataclass(init=False)
class NcOccAppapi(NCOcc):
    def __init__(self,libs:dict = cmdlib.appapi):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def app(self)->NCOcc:
        return self._lib['app']

    def daemon(self)->NCOcc:
        return self._lib['daemon']
