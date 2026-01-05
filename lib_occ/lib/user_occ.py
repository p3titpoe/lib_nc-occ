from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccUserKeys(NCOcc):
    def __init__(self,libs:dict = cmdlib.user['keys']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def verify(self)-> str:
        cmd = self._lib['verify']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccUserAuthTokens(NCOcc):
    def __init__(self,libs:dict = cmdlib.user['auth-tokens']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def add(self,value):
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def delete(self,value):
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def list(self)-> str:
        cmd = self._lib['list']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccUser(NCOcc):
    def __init__(self,libs:dict = cmdlib.user):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def add(self,value):
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def auth_tokens(self)->NCOcc:
        return self._lib['auth-tokens']

    def clear_avatar_cache(self)-> str:
        cmd = self._lib['clear-avatar-cache']['command']
        return self._process([cmd])            

    def delete(self,value):
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def disable(self)-> str:
        cmd = self._lib['disable']['command']
        return self._process([cmd])            

    def enable(self)-> str:
        cmd = self._lib['enable']['command']
        return self._process([cmd])            

    def info(self)-> str:
        cmd = self._lib['info']['command']
        return self._process([cmd])            

    def keys(self)->NCOcc:
        return self._lib['keys']

    def lastseen(self)-> str:
        cmd = self._lib['lastseen']['command']
        return self._process([cmd])            

    def list(self)-> str:
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def profile(self)-> str:
        cmd = self._lib['profile']['command']
        return self._process([cmd])            

    def report(self)-> str:
        cmd = self._lib['report']['command']
        return self._process([cmd])            

    def resetpassword(self)-> str:
        cmd = self._lib['resetpassword']['command']
        return self._process([cmd])            

    def setting(self)-> str:
        cmd = self._lib['setting']['command']
        return self._process([cmd])            

    def sync_account_data(self)-> str:
        cmd = self._lib['sync-account-data']['command']
        return self._process([cmd])            

    def welcome(self)-> str:
        cmd = self._lib['welcome']['command']
        return self._process([cmd])            
