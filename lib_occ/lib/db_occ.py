from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccDbSchema(NCOcc):
    def __init__(self,libs:dict = cmdlib.db['schema']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def expected(self)-> str:
        cmd = self._lib['expected']['command']
        return self._process([cmd])            

    def export(self)-> str:
        cmd = self._lib['export']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccDb(NCOcc):
    def __init__(self,libs:dict = cmdlib.db):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def add_missing_columns(self)-> str:
        cmd = self._lib['add-missing-columns']['command']
        return self._process([cmd])            

    def add_missing_indices(self)-> str:
        cmd = self._lib['add-missing-indices']['command']
        return self._process([cmd])            

    def add_missing_primary_keys(self)-> str:
        cmd = self._lib['add-missing-primary-keys']['command']
        return self._process([cmd])            

    def convert_filecache_bigint(self)-> str:
        cmd = self._lib['convert-filecache-bigint']['command']
        return self._process([cmd])            

    def convert_mysql_charset(self)-> str:
        cmd = self._lib['convert-mysql-charset']['command']
        return self._process([cmd])            

    def convert_type(self)-> str:
        cmd = self._lib['convert-type']['command']
        return self._process([cmd])            

    def schema(self)->NCOcc:
        return self._lib['schema']
