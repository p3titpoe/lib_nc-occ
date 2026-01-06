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
        " Verify if the stored public key matches the stored private key"
        cmd = self._lib['verify']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccUserAuthTokens(NCOcc):
    def __init__(self,libs:dict = cmdlib.user['auth-tokens']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        

    def add(self,value):
        " useraddapppassword Add app password for the named account"
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def delete(self,value):
        "Deletes an authentication token"
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def list(self)-> str:
        "List authentication tokens of an user"
        cmd = self._lib['list']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccUser(NCOcc):
    def __init__(self,libs:dict = cmdlib.user):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
        to_create = {
                    'auth-tokens' : NcOccUserAuth-tokens,
                    'keys' : NcOccUserKeys,

            }
        self._generate_subobjs(to_create)
        

    def add(self,value):
        " adds an account"
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    @property
    def auth_tokens(self)->NCOcc:
        "Returns corresponding object :: "
        return self._lib['auth-tokens']

    def clear_avatar_cache(self)-> str:
        "clear avatar cache"
        cmd = self._lib['clear-avatar-cache']['command']
        return self._process([cmd])            

    def delete(self,value):
        "deletes the specified user"
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def disable(self)-> str:
        " disables the specified user"
        cmd = self._lib['disable']['command']
        return self._process([cmd])            

    def enable(self)-> str:
        "enables the specified user"
        cmd = self._lib['enable']['command']
        return self._process([cmd])            

    def info(self)-> str:
        "show user info"
        cmd = self._lib['info']['command']
        return self._process([cmd])            

    @property
    def keys(self)->NCOcc:
        "Returns corresponding object :: "
        return self._lib['keys']

    def lastseen(self)-> str:
        "shows when the user was logged in last time"
        cmd = self._lib['lastseen']['command']
        return self._process([cmd])            

    def list(self)-> str:
        "list configured users"
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def profile(self)-> str:
        " Read and modify user profile properties"
        cmd = self._lib['profile']['command']
        return self._process([cmd])            

    def report(self)-> str:
        "shows how many users have access"
        cmd = self._lib['report']['command']
        return self._process([cmd])            

    def resetpassword(self)-> str:
        " Resets the password of the named user"
        cmd = self._lib['resetpassword']['command']
        return self._process([cmd])            

    def setting(self)-> str:
        " Read and modify user settings"
        cmd = self._lib['setting']['command']
        return self._process([cmd])            

    def sync_account_data(self)-> str:
        " sync user backend data to accounts table for configured users"
        cmd = self._lib['sync-account-data']['command']
        return self._process([cmd])            

    def welcome(self)-> str:
        " Sends the welcome email"
        cmd = self._lib['welcome']['command']
        return self._process([cmd])            
