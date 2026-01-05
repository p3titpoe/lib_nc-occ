from lib_occ import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccFilesRecommendations(NCOcc):
    def __init__(self,libs:dict = cmdlib.files['recommendations']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def recommend(self)-> str:
        cmd = self._lib['recommend']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccFilesObjectMulti(NCOcc):
    def __init__(self,libs:dict = cmdlib.files['object']['multi']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def rename_config(self)-> str:
        cmd = self._lib['rename-config']['command']
        return self._process([cmd])            

    def users(self)-> str:
        cmd = self._lib['users']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccFilesObject(NCOcc):
    def __init__(self,libs:dict = cmdlib.files['object']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def delete(self,value):
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def get(self,value):
        cmd = self._lib['get']['command']
        return self._process([cmd,value])       

    def info(self)-> str:
        cmd = self._lib['info']['command']
        return self._process([cmd])            

    def list(self)-> str:
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def multi(self)->NCOcc:
        return self._lib['multi']

    def orphans(self)-> str:
        cmd = self._lib['orphans']['command']
        return self._process([cmd])            

    def put(self,value):
        cmd = self._lib['put']['command']
        return self._process([cmd,value])       

@dataclass(init=False)
class NcOccFiles(NCOcc):
    def __init__(self,libs:dict = cmdlib.files):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def cleanup(self)-> str:
        cmd = self._lib['cleanup']['command']
        return self._process([cmd])            

    def copy(self)-> str:
        cmd = self._lib['copy']['command']
        return self._process([cmd])            

    def delete(self,value):
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def get(self,value):
        cmd = self._lib['get']['command']
        return self._process([cmd,value])       

    def move(self)-> str:
        cmd = self._lib['move']['command']
        return self._process([cmd])            

    def object(self)->NCOcc:
        return self._lib['object']

    def put(self,value):
        cmd = self._lib['put']['command']
        return self._process([cmd,value])       

    def recommendations(self)->NCOcc:
        return self._lib['recommendations']

    def reminders(self)-> str:
        cmd = self._lib['reminders']['command']
        return self._process([cmd])            

    def repair_tree(self)-> str:
        cmd = self._lib['repair-tree']['command']
        return self._process([cmd])            

    def sanitize_filenames(self)-> str:
        cmd = self._lib['sanitize-filenames']['command']
        return self._process([cmd])            

    def scan(self)-> str:
        cmd = self._lib['scan']['command']
        return self._process([cmd])            

    def scan_app_data(self)-> str:
        cmd = self._lib['scan-app-data']['command']
        return self._process([cmd])            

    def transfer_ownership(self,value):
        cmd = self._lib['transfer-ownership']['command']
        return self._process([cmd,value])       

    def windows_compatible_filenames(self)-> str:
        cmd = self._lib['windows-compatible-filenames']['command']
        return self._process([cmd])            
