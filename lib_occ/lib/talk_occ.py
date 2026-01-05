from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccTalkUser(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['user']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def remove(self)-> str:
        cmd = self._lib['remove']['command']
        return self._process([cmd])            

    def transfer_ownership(self,value):
        cmd = self._lib['transfer-ownership']['command']
        return self._process([cmd,value])       

@dataclass(init=False)
class NcOccTalkTurn(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['turn']):
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
class NcOccTalkStun(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['stun']):
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
class NcOccTalkSignaling(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['signaling']):
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

    def verify_keys(self)-> str:
        cmd = self._lib['verify-keys']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccTalkRoom(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['room']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def add(self,value):
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def create(self)-> str:
        cmd = self._lib['create']['command']
        return self._process([cmd])            

    def delete(self,value):
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def demote(self)-> str:
        cmd = self._lib['demote']['command']
        return self._process([cmd])            

    def promote(self)-> str:
        cmd = self._lib['promote']['command']
        return self._process([cmd])            

    def remove(self)-> str:
        cmd = self._lib['remove']['command']
        return self._process([cmd])            

    def update(self,value):
        cmd = self._lib['update']['command']
        return self._process([cmd,value])       

@dataclass(init=False)
class NcOccTalkRecording(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['recording']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def consent(self)-> str:
        cmd = self._lib['consent']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccTalkPhoneNumber(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['phone-number']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def add(self,value):
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def find(self)-> str:
        cmd = self._lib['find']['command']
        return self._process([cmd])            

    def import_nr(self)-> str:
        cmd = self._lib['import']['command']
        return self._process([cmd])            

    def remove(self)-> str:
        cmd = self._lib['remove']['command']
        return self._process([cmd])            

    def remove_user(self)-> str:
        cmd = self._lib['remove-user']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccTalkMonitor(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['monitor']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def calls(self)-> str:
        cmd = self._lib['calls']['command']
        return self._process([cmd])            

    def room(self)-> str:
        cmd = self._lib['room']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccTalkBot(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['bot']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def create(self)-> str:
        cmd = self._lib['create']['command']
        return self._process([cmd])            

    def install(self)-> str:
        cmd = self._lib['install']['command']
        return self._process([cmd])            

    def list(self)-> str:
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def remove(self)-> str:
        cmd = self._lib['remove']['command']
        return self._process([cmd])            

    def setup(self)-> str:
        cmd = self._lib['setup']['command']
        return self._process([cmd])            

    def state(self)-> str:
        cmd = self._lib['state']['command']
        return self._process([cmd])            

    def uninstall(self)-> str:
        cmd = self._lib['uninstall']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccTalk(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def active_calls(self)-> str:
        cmd = self._lib['active-calls']['command']
        return self._process([cmd])            

    def bot(self)->NCOcc:
        return self._lib['bot']

    def monitor(self)->NCOcc:
        return self._lib['monitor']

    def phone_number(self)->NCOcc:
        return self._lib['phone-number']

    def recording(self)->NCOcc:
        return self._lib['recording']

    def room(self)->NCOcc:
        return self._lib['room']

    def signaling(self)->NCOcc:
        return self._lib['signaling']

    def stun(self)->NCOcc:
        return self._lib['stun']

    def turn(self)->NCOcc:
        return self._lib['turn']

    def user(self)->NCOcc:
        return self._lib['user']
