from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccCirclesShares(NCOcc):
    def __init__(self,libs:dict = cmdlib.circles['shares']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def files(self):
        " listing shares files"
        cmd = self._lib['files']['command']
        return self._process([cmd])
                    

@dataclass(init=False)
class NcOccCirclesMigrate(NCOcc):
    def __init__(self,libs:dict = cmdlib.circles['migrate']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def customgroups(self):
        " "
        cmd = self._lib['customgroups']['command']
        return self._process([cmd])
                    

@dataclass(init=False)
class NcOccCirclesMembers(NCOcc):
    def __init__(self,libs:dict = cmdlib.circles['members']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def add(self,value) -> str:
        "Add a member to a Team"
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def details(self):
        "get details about a member by its ID"
        cmd = self._lib['details']['command']
        return self._process([cmd])
                    
    def level(self):
        "Change the level of a member from a Team"
        cmd = self._lib['level']['command']
        return self._process([cmd])
                    
    def lists(self):
        " listing Members from a Team"
        cmd = self._lib['list']['command']
        return self._process([cmd])
                    
    def remove(self):
        " remove a member from a team"
        cmd = self._lib['remove']['command']
        return self._process([cmd])
                    
    def search(self):
        " Change the level of a member from a Team"
        cmd = self._lib['search']['command']
        return self._process([cmd])
                    

@dataclass(init=False)
class NcOccCirclesManage(NCOcc):
    def __init__(self,libs:dict = cmdlib.circles['manage']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def config(self):
        "edit configtype of a Team"
        cmd = self._lib['config']['command']
        return self._process([cmd])
                    
    def create(self):
        "create a new team"
        cmd = self._lib['create']['command']
        return self._process([cmd])
                    
    def destroy(self):
        " destroy a circle by its ID"
        cmd = self._lib['destroy']['command']
        return self._process([cmd])
                    
    def details(self):
        " get details about a team by its ID"
        cmd = self._lib['details']['command']
        return self._process([cmd])
                    
    def edit(self,value) -> str:
        "Team"
        cmd = self._lib['edit']['command']
        return self._process([cmd,value])       

    def join(self):
        "emulate a user joining a Team"
        cmd = self._lib['join']['command']
        return self._process([cmd])
                    
    def leave(self):
        " simulate a user joining a Team"
        cmd = self._lib['leave']['command']
        return self._process([cmd])
                    
    def lists(self):
        "listing current teams"
        cmd = self._lib['list']['command']
        return self._process([cmd])
                    
    def setting(self):
        " edit setting for a Team"
        cmd = self._lib['setting']['command']
        return self._process([cmd])
                    

@dataclass(init=False)
class NcOccCircles(NCOcc):
    def __init__(self,libs:dict = cmdlib.circles):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
        to_create = {
                    'manage' : NcOccCirclesManage,
                    'members' : NcOccCirclesMembers,
                    'migrate' : NcOccCirclesMigrate,
                    'shares' : NcOccCirclesShares,

            }
        self._generate_subobjs(to_create)
        
    def check(self):
        "Checking your configuration"
        cmd = self._lib['check']['command']
        return self._process([cmd])
                    
    def maintenance(self):
        "Clean stuff keeps the app running"
        cmd = self._lib['maintenance']['command']
        return self._process([cmd])
                    
    @property
    def manage(self)->NcOccCirclesManage:
        "Returns corresponding object :: "
        return self._lib['manage']

    @property
    def members(self)->NcOccCirclesMembers:
        "Returns corresponding object :: "
        return self._lib['members']

    def memberships(self):
        "index and display memberships for local and federated users"
        cmd = self._lib['memberships']['command']
        return self._process([cmd])
                    
    @property
    def migrate(self)->NcOccCirclesMigrate:
        "Returns corresponding object :: "
        return self._lib['migrate']

    def remote(self):
        " remote features"
        cmd = self._lib['remote']['command']
        return self._process([cmd])
                    
    @property
    def shares(self)->NcOccCirclesShares:
        "Returns corresponding object :: "
        return self._lib['shares']

    def sync(self):
        " Sync Circles and Members"
        cmd = self._lib['sync']['command']
        return self._process([cmd])
                    
    def test(self):
        " testing some features"
        cmd = self._lib['test']['command']
        return self._process([cmd])
                    
