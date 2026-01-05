from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccTalkUser(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['user']):
        if libs is None:
            libs = {}
        super().__init__(libs)

        to_create = {
                    'bot' : NcOccTalkBot,
                    'monitor' : NcOccTalkMonitor,
                    'phone-number' : NcOccTalkPhoneNumber,
                    'recording' : NcOccTalkRecording,
                    'room' : NcOccTalkRoom,
                    'signaling' : NcOccTalkSignaling,
                    'stun' : NcOccTalkStun,
                    'turn' : NcOccTalkTurn,
                    'user' : NcOccTalkUser,

            }
        
    def remove(self)-> str:
        " Remove a user from all their rooms"
        cmd = self._lib['remove']['command']
        return self._process([cmd])            

    def transfer_ownership(self,value):
        " Adds the destinationuser with the same participant type to all not onetoone conversations of sourceuser"
        cmd = self._lib['transfer-ownership']['command']
        return self._process([cmd,value])       

@dataclass(init=False)
class NcOccTalkTurn(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['turn']):
        if libs is None:
            libs = {}
        super().__init__(libs)

        to_create = {
                    'bot' : NcOccTalkBot,
                    'monitor' : NcOccTalkMonitor,
                    'phone-number' : NcOccTalkPhoneNumber,
                    'recording' : NcOccTalkRecording,
                    'room' : NcOccTalkRoom,
                    'signaling' : NcOccTalkSignaling,
                    'stun' : NcOccTalkStun,
                    'turn' : NcOccTalkTurn,

            }
        
    def add(self,value):
        "Add a TURN server"
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def delete(self,value):
        " Remove an existing TURN server"
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def list(self)-> str:
        " List TURN servers"
        cmd = self._lib['list']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccTalkStun(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['stun']):
        if libs is None:
            libs = {}
        super().__init__(libs)

        to_create = {
                    'bot' : NcOccTalkBot,
                    'monitor' : NcOccTalkMonitor,
                    'phone-number' : NcOccTalkPhoneNumber,
                    'recording' : NcOccTalkRecording,
                    'room' : NcOccTalkRoom,
                    'signaling' : NcOccTalkSignaling,
                    'stun' : NcOccTalkStun,

            }
        
    def add(self,value):
        "Add a new STUN server"
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def delete(self,value):
        " Remove an existing STUN server"
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def list(self)-> str:
        " List STUN servers"
        cmd = self._lib['list']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccTalkSignaling(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['signaling']):
        if libs is None:
            libs = {}
        super().__init__(libs)

        to_create = {
                    'bot' : NcOccTalkBot,
                    'monitor' : NcOccTalkMonitor,
                    'phone-number' : NcOccTalkPhoneNumber,
                    'recording' : NcOccTalkRecording,
                    'room' : NcOccTalkRoom,
                    'signaling' : NcOccTalkSignaling,

            }
        
    def add(self,value):
        " Add an external signaling server"
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def delete(self,value):
        "Remove an existing signaling server"
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def list(self)-> str:
        "List external signaling servers"
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def verify_keys(self)-> str:
        " Verify if the stored public key matches the stored private key for the signaling server"
        cmd = self._lib['verify-keys']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccTalkRoom(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['room']):
        if libs is None:
            libs = {}
        super().__init__(libs)

        to_create = {
                    'bot' : NcOccTalkBot,
                    'monitor' : NcOccTalkMonitor,
                    'phone-number' : NcOccTalkPhoneNumber,
                    'recording' : NcOccTalkRecording,
                    'room' : NcOccTalkRoom,

            }
        
    def add(self,value):
        "Adds users to a room"
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def create(self)-> str:
        " Create a new room"
        cmd = self._lib['create']['command']
        return self._process([cmd])            

    def delete(self,value):
        " Deletes a room"
        cmd = self._lib['delete']['command']
        return self._process([cmd,value])       

    def demote(self)-> str:
        " Demotes participants of a room to regular users"
        cmd = self._lib['demote']['command']
        return self._process([cmd])            

    def promote(self)-> str:
        "Promotes participants of a room to moderators"
        cmd = self._lib['promote']['command']
        return self._process([cmd])            

    def remove(self)-> str:
        " Remove users from a room"
        cmd = self._lib['remove']['command']
        return self._process([cmd])            

    def update(self,value):
        " Updates a room"
        cmd = self._lib['update']['command']
        return self._process([cmd,value])       

@dataclass(init=False)
class NcOccTalkRecording(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['recording']):
        if libs is None:
            libs = {}
        super().__init__(libs)

        to_create = {
                    'bot' : NcOccTalkBot,
                    'monitor' : NcOccTalkMonitor,
                    'phone-number' : NcOccTalkPhoneNumber,
                    'recording' : NcOccTalkRecording,

            }
        
    def consent(self)-> str:
        " List all matching consent that were given to be audio and video recorded during a call requires administrator or moderator configuration"
        cmd = self._lib['consent']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccTalkPhoneNumber(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['phone-number']):
        if libs is None:
            libs = {}
        super().__init__(libs)

        to_create = {
                    'bot' : NcOccTalkBot,
                    'monitor' : NcOccTalkMonitor,
                    'phone-number' : NcOccTalkPhoneNumber,

            }
        
    def add(self,value):
        "Add a mapping entry to map a phone number to an user"
        cmd = self._lib['add']['command']
        return self._process([cmd,value])       

    def find(self)-> str:
        " Find a phone number or the phone number of an user"
        cmd = self._lib['find']['command']
        return self._process([cmd])            

    def imports(self)-> str:
        " Import a CSV list format numberuser for SIP dialin"
        cmd = self._lib['import']['command']
        return self._process([cmd])            

    def remove(self)-> str:
        " Remove a mapping entry by phone number"
        cmd = self._lib['remove']['command']
        return self._process([cmd])            

    def remove_user(self)-> str:
        "Remove mapping entries by user"
        cmd = self._lib['remove-user']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccTalkMonitor(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['monitor']):
        if libs is None:
            libs = {}
        super().__init__(libs)

        to_create = {
                    'bot' : NcOccTalkBot,
                    'monitor' : NcOccTalkMonitor,

            }
        
    def calls(self)-> str:
        " Prints a list with conversations that have an active call as well as their participant count"
        cmd = self._lib['calls']['command']
        return self._process([cmd])            

    def room(self)-> str:
        "Prints the number of attendees active sessions and participant in the call"
        cmd = self._lib['room']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccTalkBot(NCOcc):
    def __init__(self,libs:dict = cmdlib.talk['bot']):
        if libs is None:
            libs = {}
        super().__init__(libs)

        to_create = {
                    'bot' : NcOccTalkBot,

            }
        
    def create(self)-> str:
        "Creates a new bot on the server with response feature only"
        cmd = self._lib['create']['command']
        return self._process([cmd])            

    def install(self)-> str:
        " Install a new bot on the server"
        cmd = self._lib['install']['command']
        return self._process([cmd])            

    def list(self)-> str:
        "List all installed bots of the server or a conversation"
        cmd = self._lib['list']['command']
        return self._process([cmd])            

    def remove(self)-> str:
        "Remove a bot from a conversation"
        cmd = self._lib['remove']['command']
        return self._process([cmd])            

    def setup(self)-> str:
        " Add a bot to a conversation"
        cmd = self._lib['setup']['command']
        return self._process([cmd])            

    def state(self)-> str:
        " Change the state or feature list for a bot"
        cmd = self._lib['state']['command']
        return self._process([cmd])            

    def uninstall(self)-> str:
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
                    'phone-number' : NcOccTalkPhoneNumber,
                    'recording' : NcOccTalkRecording,
                    'room' : NcOccTalkRoom,
                    'signaling' : NcOccTalkSignaling,
                    'stun' : NcOccTalkStun,
                    'turn' : NcOccTalkTurn,
                    'user' : NcOccTalkUser,

            }
        
    def active_calls(self)-> str:
        "Allows you to check if calls are currently in process"
        cmd = self._lib['active-calls']['command']
        return self._process([cmd])            
