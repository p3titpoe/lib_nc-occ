
import occ_command_lib as cmdlib
from logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccFilesRecommendations(NCOcc):
    def __init__(self,libs:dict = cmdlib.recommendations):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def recommend(self):
        cmd = self._lib['recommendations']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccFilesObjectMulti(NCOcc):
    def __init__(self,libs:dict = cmdlib.multi):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def rename_config(self):
        cmd = self._lib['multi']['command']
        return self._process([cmd])            

    def users(self):
        cmd = self._lib['multi']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccFilesObject(NCOcc):
    def __init__(self,libs:dict = cmdlib.object):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def delete(self,value):
        cmd = self._lib['object']['command']
        return self._process([cmd,value])       

    def get(self,value):
        cmd = self._lib['object']['command']
        return self._process([cmd,value])       

    def info(self):
        cmd = self._lib['object']['command']
        return self._process([cmd])            

    def list(self):
        cmd = self._lib['object']['command']
        return self._process([cmd])            

    def multi(self)->NCOcc:
        return self._lib['object']

    def orphans(self):
        cmd = self._lib['object']['command']
        return self._process([cmd])            

    def put(self,value):
        cmd = self._lib['object']['command']
        return self._process([cmd,value])       

@dataclass(init=False)
class NcOccFiles(NCOcc):
    def __init__(self,libs:dict = cmdlib.files):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def cleanup(self):
        cmd = self._lib['files']['command']
        return self._process([cmd])            

    def copy(self):
        cmd = self._lib['files']['command']
        return self._process([cmd])            

    def delete(self,value):
        cmd = self._lib['files']['command']
        return self._process([cmd,value])       

    def get(self,value):
        cmd = self._lib['files']['command']
        return self._process([cmd,value])       

    def move(self):
        cmd = self._lib['files']['command']
        return self._process([cmd])            

    def object(self)->NCOcc:
        return self._lib['files']

    def put(self,value):
        cmd = self._lib['files']['command']
        return self._process([cmd,value])       

    def recommendations(self)->NCOcc:
        return self._lib['files']

    def reminders(self):
        cmd = self._lib['files']['command']
        return self._process([cmd])            

    def repair_tree(self):
        cmd = self._lib['files']['command']
        return self._process([cmd])            

    def sanitize_filenames(self):
        cmd = self._lib['files']['command']
        return self._process([cmd])            

    def scan(self):
        cmd = self._lib['files']['command']
        return self._process([cmd])            

    def scan_app_data(self):
        cmd = self._lib['files']['command']
        return self._process([cmd])            

    def transfer_ownership(self,value):
        cmd = self._lib['files']['command']
        return self._process([cmd,value])       

    def windows_compatible_filenames(self):
        cmd = self._lib['files']['command']
        return self._process([cmd])            
