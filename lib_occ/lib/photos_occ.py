from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccPhotosAlbums(NCOcc):
    def __init__(self,libs:dict = cmdlib.photos['albums']):
        if libs is None:
            libs = {}
        super().__init__(libs)
    

    def add(self,value):
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def create(self)-> str:
        cmd = self._lib['create']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccPhotos(NCOcc):
    def __init__(self,libs:dict = cmdlib.photos):
        if libs is None:
            libs = {}
        super().__init__(libs)
    

    @property
    def albums(self)->NCOcc:
        return self._lib['albums']

    def update_1000_cities(self)-> str:
        cmd = self._lib['update-1000-cities']['command']
        return self._process([cmd])            
