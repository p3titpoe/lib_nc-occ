from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccFilesRecommendations(NCOcc):
    def __init__(self,libs:dict = cmdlib.files['recommendations']):
        if libs is None:
            libs = {}
        super().__init__(libs)

        to_create = {
                    'object' : NcOccFilesObject,
                    'object-multi' : NcOccFilesObjectMulti,
                    'recommendations' : NcOccFilesRecommendations,

            }
        
    def recommend(self)-> str:
        "Shows recommended files for an account"
        cmd = self._lib['recommend']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccFilesObjectMulti(NCOcc):
    def __init__(self,libs:dict = cmdlib.files['object']['multi']):
        if libs is None:
            libs = {}
        super().__init__(libs)

        to_create = {
                    'object' : NcOccFilesObject,
                    'object-multi' : NcOccFilesObjectMulti,

            }
        
    def rename_config(self)-> str:
        " Rename an object store configuration and move all users over to the new configuration"
        cmd = self._lib['rename-config']['command']
        return self._process([cmd])            

    def users(self)-> str:
        " Get the mapping between users and object store buckets"
        cmd = self._lib['users']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccFilesObject(NCOcc):
    def __init__(self,libs:dict = cmdlib.files['object']):
        if libs is None:
            libs = {}
        super().__init__(libs)

        to_create = {
                    'object' : NcOccFilesObject,
                    'object-multi' : NcOccFilesObjectMulti,

            }
        
    def delete(self,value):
        "Delete an object from the object store"
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def get(self,value):
        " Get the contents of an object"
        cmd = self._lib['get']['command']
        return self._process([cmd,value])       

    def info(self)-> str:
        "Get the metadata of an object"
        cmd = self._lib['info']['command']
        return self._process([cmd])            

    def list(self)-> str:
        "List all objects in the object store"
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    @property
    def multi(self)->NCOcc:
        "Returns corresponding object :: "
        return self._lib['multi']

    def orphans(self)-> str:
        " List all objects in the object store that dont have a matching entry in the database"
        cmd = self._lib['orphans']['command']
        return self._process([cmd])            

    def put(self,value):
        " Write a file to the object store"
        cmd = self._lib['put']['command']
        return self._process([cmd,value])       

@dataclass(init=False)
class NcOccFiles(NCOcc):
    def __init__(self,libs:dict = cmdlib.files):
        if libs is None:
            libs = {}
        super().__init__(libs)

        to_create = {
                    'object' : NcOccFilesObject,
                    'object-multi' : NcOccFilesObjectMulti,
                    'recommendations' : NcOccFilesRecommendations,

            }
        
    def cleanup(self)-> str:
        "Clean up orphaned filecache and mount entries"
        cmd = self._lib['cleanup']['command']
        return self._process([cmd])            

    def copy(self)-> str:
        " Copy a file or folder"
        cmd = self._lib['copy']['command']
        return self._process([cmd])            

    def delete(self,value):
        " Delete a file or folder"
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def get(self,value):
        "Get the contents of a file"
        cmd = self._lib['get']['command']
        return self._process([cmd,value])       

    def move(self)-> str:
        " Move a file or folder"
        cmd = self._lib['move']['command']
        return self._process([cmd])            

    @property
    def object(self)->NCOcc:
        "Returns corresponding object :: "
        return self._lib['object']

    def put(self,value):
        "Write contents of a file"
        cmd = self._lib['put']['command']
        return self._process([cmd,value])       

    @property
    def recommendations(self)->NCOcc:
        "Returns corresponding object :: "
        return self._lib['recommendations']

    def reminders(self)-> str:
        "List file reminders"
        cmd = self._lib['reminders']['command']
        return self._process([cmd])            

    def repair_tree(self)-> str:
        "Try and repair malformed filesystem tree structures"
        cmd = self._lib['repair-tree']['command']
        return self._process([cmd])            

    def sanitize_filenames(self)-> str:
        " Renames files to match naming constraints"
        cmd = self._lib['sanitize-filenames']['command']
        return self._process([cmd])            

    def scan(self)-> str:
        " rescan filesystem"
        cmd = self._lib['scan']['command']
        return self._process([cmd])            

    def scan_app_data(self)-> str:
        "rescan the AppData folder"
        cmd = self._lib['scan-app-data']['command']
        return self._process([cmd])            

    def transfer_ownership(self,value):
        " All files and folders are moved to another user  outgoing shares and incoming user file shares optionally are moved as well"
        cmd = self._lib['transfer-ownership']['command']
        return self._process([cmd,value])       

    def windows_compatible_filenames(self)-> str:
        " Enforce naming constraints for windows compatible filenames"
        cmd = self._lib['windows-compatible-filenames']['command']
        return self._process([cmd])            
