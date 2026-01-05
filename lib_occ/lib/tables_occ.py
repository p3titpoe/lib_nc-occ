from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccTablesLegacyTransfer(NCOcc):
    def __init__(self,libs:dict = cmdlib.tables['legacy']['transfer']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def rows(self)-> str:
        cmd = self._lib['rows']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccTablesLegacy(NCOcc):
    def __init__(self,libs:dict = cmdlib.tables['legacy']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def clean(self)-> str:
        cmd = self._lib['clean']['command']
        return self._process([cmd])            

    def transfer(self)->NCOcc:
        return self._lib['transfer']

@dataclass(init=False)
class NcOccTablesContexts(NCOcc):
    def __init__(self,libs:dict = cmdlib.tables['contexts']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def list(self)-> str:
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def show(self)-> str:
        cmd = self._lib['show']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccTables(NCOcc):
    def __init__(self,libs:dict = cmdlib.tables):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def add(self,value):
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def clean(self)-> str:
        cmd = self._lib['clean']['command']
        return self._process([cmd])            

    def contexts(self)->NCOcc:
        return self._lib['contexts']

    def legacy(self)->NCOcc:
        return self._lib['legacy']

    def list(self)-> str:
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def owner(self)-> str:
        cmd = self._lib['owner']['command']
        return self._process([cmd])            

    def remove(self)-> str:
        cmd = self._lib['remove']['command']
        return self._process([cmd])            

    def update(self,value):
        cmd = self._lib['update']['command']
        return self._process([cmd,value])       
