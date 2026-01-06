from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccTalkUser(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['user']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def remove(self):
        " Remove a user from all their rooms"
        cmd = self._lib['remove']['command']
        return self._process([cmd])
                    
    def transfer_ownership(self,value) -> str:
        " Adds the destinationuser with the same participant type to all not onetoone conversations of sourceuser"
        cmd = self._lib['transfer-ownership']['command']
        return self._process([cmd,value])       


@dataclass(init=False)
class NcOccTalkTurn(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['turn']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def add(self,value) -> str:
        "Add a TURN server"
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def delete(self,value) -> str:
        " Remove an existing TURN server"
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def lists(self):
        " List TURN servers"
        cmd = self._lib['list']['command']
        return self._process([cmd])
                    

@dataclass(init=False)
class NcOccTalkStun(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['stun']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def add(self,value) -> str:
        "Add a new STUN server"
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def delete(self,value) -> str:
        " Remove an existing STUN server"
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def lists(self):
        " List STUN servers"
        cmd = self._lib['list']['command']
        return self._process([cmd])
                    

@dataclass(init=False)
class NcOccTalkSignaling(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['signaling']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def add(self,value) -> str:
        " Add an external signaling server"
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def delete(self,value) -> str:
        "Remove an existing signaling server"
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def lists(self):
        "List external signaling servers"
        cmd = self._lib['list']['command']
        return self._process([cmd])
                    
    def verify_keys(self):
        " Verify if the stored public key matches the stored private key for the signaling server"
        cmd = self._lib['verify-keys']['command']
        return self._process([cmd])
                    

@dataclass(init=False)
class NcOccTalkRoom(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['room']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def add(self,value) -> str:
        "Adds users to a room"
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def create(self):
        " Create a new room"
        cmd = self._lib['create']['command']
        return self._process([cmd])
                    
    def delete(self,value) -> str:
        " Deletes a room"
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def demote(self):
        " Demotes participants of a room to regular users"
        cmd = self._lib['demote']['command']
        return self._process([cmd])
                    
    def promote(self):
        "Promotes participants of a room to moderators"
        cmd = self._lib['promote']['command']
        return self._process([cmd])
                    
    def remove(self):
        " Remove users from a room"
        cmd = self._lib['remove']['command']
        return self._process([cmd])
                    
    def update(self,value) -> str:
        " Updates a room"
        cmd = self._lib['update']['command']
        return self._process([cmd,value])       


@dataclass(init=False)
class NcOccTalkRecording(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['recording']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def consent(self):
        " List all matching consent that were given to be audio and video recorded during a call requires administrator or moderator configuration"
        cmd = self._lib['consent']['command']
        return self._process([cmd])
                    

@dataclass(init=False)
class NcOccTalkPhoneNumber(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['phone-number']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def add(self,value) -> str:
        "Add a mapping entry to map a phone number to an user"
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def find(self):
        " Find a phone number or the phone number of an user"
        cmd = self._lib['find']['command']
        return self._process([cmd])
                    
    def imports(self):
        " Import a CSV list format numberuser for SIP dialin"
        cmd = self._lib['import']['command']
        return self._process([cmd])
                    
    def remove(self):
        " Remove a mapping entry by phone number"
        cmd = self._lib['remove']['command']
        return self._process([cmd])
                    
    def remove_user(self):
        "Remove mapping entries by user"
        cmd = self._lib['remove-user']['command']
        return self._process([cmd])
                    

@dataclass(init=False)
class NcOccTalkMonitor(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['monitor']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def calls(self):
        " Prints a list with conversations that have an active call as well as their participant count"
        cmd = self._lib['calls']['command']
        return self._process([cmd])
                    
    def room(self):
        "Prints the number of attendees active sessions and participant in the call"
        cmd = self._lib['room']['command']
        return self._process([cmd])
                    

@dataclass(init=False)
class NcOccTalkBot(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['bot']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def create(self):
        "Creates a new bot on the server with response feature only"
        cmd = self._lib['create']['command']
        return self._process([cmd])
                    
    def install(self):
        " Install a new bot on the server"
        cmd = self._lib['install']['command']
        return self._process([cmd])
                    
    def lists(self):
        "List all installed bots of the server or a conversation"
        cmd = self._lib['list']['command']
        return self._process([cmd])
                    
    def remove(self):
        "Remove a bot from a conversation"
        cmd = self._lib['remove']['command']
        return self._process([cmd])
                    
    def setup(self):
        " Add a bot to a conversation"
        cmd = self._lib['setup']['command']
        return self._process([cmd])
                    
    def state(self):
        " Change the state or feature list for a bot"
        cmd = self._lib['state']['command']
        return self._process([cmd])
                    
    def uninstall(self):
        " Uninstall a bot from the server"
        cmd = self._lib['uninstall']['command']
        return self._process([cmd])
                    

@dataclass(init=False)
class NcOccTalk(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
        to_create = {
                    'bot' : NcOccTalkBot,
                    'monitor' : NcOccTalkMonitor,
                    'phone-number' : NcOccTalkPhone-number,
                    'recording' : NcOccTalkRecording,
                    'room' : NcOccTalkRoom,
                    'signaling' : NcOccTalkSignaling,
                    'stun' : NcOccTalkStun,
                    'turn' : NcOccTalkTurn,
                    'user' : NcOccTalkUser,

            }
        self._generate_subobjs(to_create)
        
    def active_calls(self):
        "Allows you to check if calls are currently in process"
        cmd = self._lib['active-calls']['command']
        return self._process([cmd])
                    
    @property
    def bot(self)->NcOccTalkBot:
        "Returns corresponding object :: "
        return self._lib['bot']

    @property
    def monitor(self)->NcOccTalkMonitor:
        "Returns corresponding object :: "
        return self._lib['monitor']

    @property
    def phone_number(self)->NcOccTalkPhoneNumber:
        "Returns corresponding object :: "
        return self._lib['phone-number']

    @property
    def recording(self)->NcOccTalkRecording:
        "Returns corresponding object :: "
        return self._lib['recording']

    @property
    def room(self)->NcOccTalkRoom:
        "Returns corresponding object :: "
        return self._lib['room']

    @property
    def signaling(self)->NcOccTalkSignaling:
        "Returns corresponding object :: "
        return self._lib['signaling']

    @property
    def stun(self)->NcOccTalkStun:
        "Returns corresponding object :: "
        return self._lib['stun']

    @property
    def turn(self)->NcOccTalkTurn:
        "Returns corresponding object :: "
        return self._lib['turn']

    @property
    def user(self)->NcOccTalkUser:
        "Returns corresponding object :: "
        return self._lib['user']

