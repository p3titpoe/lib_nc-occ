from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccCirclesShares(NCOcc):
    def __init__(self,libs:dict = cmdlib.circles['shares']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def files(self)-> str:
        cmd = self._lib['files']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccCirclesMigrate(NCOcc):
    def __init__(self,libs:dict = cmdlib.circles['migrate']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def customgroups(self)-> str:
        cmd = self._lib['customgroups']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccCirclesMembers(NCOcc):
    def __init__(self,libs:dict = cmdlib.circles['members']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def add(self,value):
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def details(self)-> str:
        cmd = self._lib['details']['command']
        return self._process([cmd])            

    def level(self)-> str:
        cmd = self._lib['level']['command']
        return self._process([cmd])            

    def list(self)-> str:
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def remove(self)-> str:
        cmd = self._lib['remove']['command']
        return self._process([cmd])            

    def search(self)-> str:
        cmd = self._lib['search']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccCirclesManage(NCOcc):
    def __init__(self,libs:dict = cmdlib.circles['manage']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def config(self)-> str:
        cmd = self._lib['config']['command']
        return self._process([cmd])            

    def create(self)-> str:
        cmd = self._lib['create']['command']
        return self._process([cmd])            

    def destroy(self)-> str:
        cmd = self._lib['destroy']['command']
        return self._process([cmd])            

    def details(self)-> str:
        cmd = self._lib['details']['command']
        return self._process([cmd])            

    def edit(self,value):
        cmd = self._lib['edit']['command']
        return self._process([cmd,value])       

    def join(self)-> str:
        cmd = self._lib['join']['command']
        return self._process([cmd])            

    def leave(self)-> str:
        cmd = self._lib['leave']['command']
        return self._process([cmd])            

    def list(self)-> str:
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def setting(self)-> str:
        cmd = self._lib['setting']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccCircles(NCOcc):
    def __init__(self,libs:dict = cmdlib.circles):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def check(self)-> str:
        cmd = self._lib['check']['command']
        return self._process([cmd])            

    def maintenance(self)-> str:
        cmd = self._lib['maintenance']['command']
        return self._process([cmd])            

    def manage(self)->NCOcc:
        return self._lib['manage']

    def members(self)->NCOcc:
        return self._lib['members']

    def memberships(self)-> str:
        cmd = self._lib['memberships']['command']
        return self._process([cmd])            

    def migrate(self)->NCOcc:
        return self._lib['migrate']

    def remote(self)-> str:
        cmd = self._lib['remote']['command']
        return self._process([cmd])            

    def shares(self)->NCOcc:
        return self._lib['shares']

    def sync(self)-> str:
        cmd = self._lib['sync']['command']
        return self._process([cmd])            

    def test(self)-> str:
        cmd = self._lib['test']['command']
        return self._process([cmd])            
