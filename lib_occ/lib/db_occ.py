from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccDbSchema(NCOcc):
    def __init__(self,libs:dict = cmdlib.db['schema']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def expected(self):
        " Export the expected database schema for a fresh installation"
        cmd = self._lib['expected']['command']
        return self._process([cmd])
                    
    def export(self):
        " Export the current database schema"
        cmd = self._lib['export']['command']
        return self._process([cmd])
                    

@dataclass(init=False)
class NcOccDb(NCOcc):
    def __init__(self,libs:dict = cmdlib.db):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
        to_create = {
                    'schema' : NcOccDbSchema,

            }
        self._generate_subobjs(to_create)
        
    def add_missing_columns(self):
        " Add missing optional columns to the database tables"
        cmd = self._lib['add-missing-columns']['command']
        return self._process([cmd])
                    
    def add_missing_indices(self):
        " Add missing indices to the database tables"
        cmd = self._lib['add-missing-indices']['command']
        return self._process([cmd])
                    
    def add_missing_primary_keys(self):
        "Add missing primary keys to the database tables"
        cmd = self._lib['add-missing-primary-keys']['command']
        return self._process([cmd])
                    
    def convert_filecache_bigint(self):
        "Convert the ID columns of the filecache to BigInt"
        cmd = self._lib['convert-filecache-bigint']['command']
        return self._process([cmd])
                    
    def convert_mysql_charset(self):
        " Convert charset of MySQLMariaDB to use utf8mb4"
        cmd = self._lib['convert-mysql-charset']['command']
        return self._process([cmd])
                    
    def convert_type(self):
        "Convert the Nextcloud database to the newly configured one"
        cmd = self._lib['convert-type']['command']
        return self._process([cmd])
                    
    @property
    def schema(self)->NcOccDbSchema:
        "Returns corresponding object :: "
        return self._lib['schema']

