from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccApp(NCOcc):
    def __init__(self,libs:dict = cmdlib.app):
        if libs is None:
            libs = {}
        super().__init__(libs)
        

    def disable(self)-> str:
        "disable an app"
        cmd = self._lib['disable']['command']
        return self._process([cmd])            

    def enable(self)-> str:
        " enable an app"
        cmd = self._lib['enable']['command']
        return self._process([cmd])            

    def getpath(self)-> str:
        "Get an absolute path to the app directory"
        cmd = self._lib['getpath']['command']
        return self._process([cmd])            

    def install(self)-> str:
        "install an app"
        cmd = self._lib['install']['command']
        return self._process([cmd])            

    def list(self)-> str:
        " List all available apps"
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def remove(self)-> str:
        " remove an app"
        cmd = self._lib['remove']['command']
        return self._process([cmd])            

    def update(self,value):
        " update an app or all apps"
        cmd = self._lib['update']['command']
        return self._process([cmd,value])       
