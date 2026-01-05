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
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def get(self,value):
        cmd = self._lib['get']['command']
        return self._process([cmd,value])       

    def set(self)-> str:
        cmd = self._lib['set']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccConfigApp(NCOcc):
    def __init__(self,libs:dict = cmdlib.config['app']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def delete(self,value):
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def get(self,value):
        cmd = self._lib['get']['command']
        return self._process([cmd,value])       

    def set(self)-> str:
        cmd = self._lib['set']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccConfig(NCOcc):
    def __init__(self,libs:dict = cmdlib.config):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def app(self)->NCOcc:
        return self._lib['app']

    def import_config(self)-> str:
        cmd = self._lib['import']['command']
        return self._process([cmd])            

    def list(self)-> str:
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def preset(self)-> str:
        cmd = self._lib['preset']['command']
        return self._process([cmd])            

    def system(self)->NCOcc:
        return self._lib['system']
