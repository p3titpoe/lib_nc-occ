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
        "Add specified photo to album"
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def create(self)-> str:
        " Create a new album for a user"
        cmd = self._lib['create']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccPhotos(NCOcc):
    def __init__(self,libs:dict = cmdlib.photos):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
        to_create = {
                    'albums' : NcOccPhotosAlbums,

            }
        self._generate_subobjs(to_create)
        

    @property
    def albums(self)->NCOcc:
        "Returns corresponding object :: "
        return self._lib['albums']

    def update_1000_cities(self)-> str:
        "Update the list of 1000 and more inhabitant cities"
        cmd = self._lib['update-1000-cities']['command']
        return self._process([cmd])            
