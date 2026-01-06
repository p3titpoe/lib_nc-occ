from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccTablesLegacyTransfer(NCOcc):
    def __init__(self,libs:dict = cmdlib.tables['legacy']['transfer']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def rows(self):
        "Transfer table legacy rows to new schema"
        cmd = self._lib['rows']['command']
        return self._process([cmd])
                    

@dataclass(init=False)
class NcOccTablesLegacy(NCOcc):
    def __init__(self,libs:dict = cmdlib.tables['legacy']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
        to_create = {
                    'transfer' : NcOccTablesLegacyTransfer,

            }
        self._generate_subobjs(to_create)
        
    def clean(self):
        "Clean the tables legacy data"
        cmd = self._lib['clean']['command']
        return self._process([cmd])
                    
    @property
    def transfer(self)->NcOccTablesLegacyTransfer:
        "Returns corresponding object :: "
        return self._lib['transfer']


@dataclass(init=False)
class NcOccTablesContexts(NCOcc):
    def __init__(self,libs:dict = cmdlib.tables['contexts']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def lists(self):
        " Get all contexts or contexts available to a specified user"
        cmd = self._lib['list']['command']
        return self._process([cmd])
                    
    def show(self):
        " Get all contexts or contexts available to a specified user"
        cmd = self._lib['show']['command']
        return self._process([cmd])
                    

@dataclass(init=False)
class NcOccTables(NCOcc):
    def __init__(self,libs:dict = cmdlib.tables):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
        to_create = {
                    'contexts' : NcOccTablesContexts,
                    'legacy' : NcOccTablesLegacy,

            }
        self._generate_subobjs(to_create)
        
    def add(self,value) -> str:
        " Add a table"
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def clean(self):
        " Clean the tables data"
        cmd = self._lib['clean']['command']
        return self._process([cmd])
                    
    @property
    def contexts(self)->NcOccTablesContexts:
        "Returns corresponding object :: "
        return self._lib['contexts']

    @property
    def legacy(self)->NcOccTablesLegacy:
        "Returns corresponding object :: "
        return self._lib['legacy']

    def lists(self):
        "List all tables"
        cmd = self._lib['list']['command']
        return self._process([cmd])
                    
    def owner(self):
        " Set new owner for a table"
        cmd = self._lib['owner']['command']
        return self._process([cmd])
                    
    def remove(self):
        "Remove a table"
        cmd = self._lib['remove']['command']
        return self._process([cmd])
                    
    def update(self,value) -> str:
        "tablesrename Rename a table"
        cmd = self._lib['update']['command']
        return self._process([cmd,value])       

