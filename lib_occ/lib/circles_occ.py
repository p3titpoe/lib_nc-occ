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
        " listing shares files"
        cmd = self._lib['files']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccCirclesMigrate(NCOcc):
    def __init__(self,libs:dict = cmdlib.circles['migrate']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        

    def customgroups(self)-> str:
        " "
        cmd = self._lib['customgroups']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccCirclesMembers(NCOcc):
    def __init__(self,libs:dict = cmdlib.circles['members']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        

    def add(self,value):
        "Add a member to a Team"
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def details(self)-> str:
        "get details about a member by its ID"
        cmd = self._lib['details']['command']
        return self._process([cmd])            

    def level(self)-> str:
        "Change the level of a member from a Team"
        cmd = self._lib['level']['command']
        return self._process([cmd])            

    def list(self)-> str:
        " listing Members from a Team"
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def remove(self)-> str:
        " remove a member from a team"
        cmd = self._lib['remove']['command']
        return self._process([cmd])            

    def search(self)-> str:
        " Change the level of a member from a Team"
        cmd = self._lib['search']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccCirclesManage(NCOcc):
    def __init__(self,libs:dict = cmdlib.circles['manage']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        

    def config(self)-> str:
        "edit configtype of a Team"
        cmd = self._lib['config']['command']
        return self._process([cmd])            

    def create(self)-> str:
        "create a new team"
        cmd = self._lib['create']['command']
        return self._process([cmd])            

    def destroy(self)-> str:
        " destroy a circle by its ID"
        cmd = self._lib['destroy']['command']
        return self._process([cmd])            

    def details(self)-> str:
        " get details about a team by its ID"
        cmd = self._lib['details']['command']
        return self._process([cmd])            

    def edit(self,value):
        "Team"
        cmd = self._lib['edit']['command']
        return self._process([cmd,value])       

    def join(self)-> str:
        "emulate a user joining a Team"
        cmd = self._lib['join']['command']
        return self._process([cmd])            

    def leave(self)-> str:
        " simulate a user joining a Team"
        cmd = self._lib['leave']['command']
        return self._process([cmd])            

    def list(self)-> str:
        "listing current teams"
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def setting(self)-> str:
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
        

    def check(self)-> str:
        "Checking your configuration"
        cmd = self._lib['check']['command']
        return self._process([cmd])            

    def maintenance(self)-> str:
        "Clean stuff keeps the app running"
        cmd = self._lib['maintenance']['command']
        return self._process([cmd])            

    @property
    def manage(self)->NCOcc:
        "Returns corresponding object :: "
        return self._lib['manage']

    @property
    def members(self)->NCOcc:
        "Returns corresponding object :: "
        return self._lib['members']

    def memberships(self)-> str:
        "index and display memberships for local and federated users"
        cmd = self._lib['memberships']['command']
        return self._process([cmd])            

    @property
    def migrate(self)->NCOcc:
        "Returns corresponding object :: "
        return self._lib['migrate']

    def remote(self)-> str:
        " remote features"
        cmd = self._lib['remote']['command']
        return self._process([cmd])            

    @property
    def shares(self)->NCOcc:
        "Returns corresponding object :: "
        return self._lib['shares']

    def sync(self)-> str:
        " Sync Circles and Members"
        cmd = self._lib['sync']['command']
        return self._process([cmd])            

    def test(self)-> str:
        " testing some features"
        cmd = self._lib['test']['command']
        return self._process([cmd])            
