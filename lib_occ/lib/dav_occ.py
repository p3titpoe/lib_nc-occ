from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccDavRetention(NCOcc):
    def __init__(self,libs:dict = cmdlib.dav['retention']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def clean_up(self):
        " "
        cmd = self._lib['clean-up']['command']
        return self._process([cmd])
                    

@dataclass(init=False)
class NcOccDavAbsence(NCOcc):
    def __init__(self,libs:dict = cmdlib.dav['absence']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def get(self,value) -> str:
        ""
        cmd = self._lib['get']['command']
        return self._process([cmd,value])       

    def set(self):
        ""
        cmd = self._lib['set']['command']
        return self._process([cmd])
                    

@dataclass(init=False)
class NcOccDav(NCOcc):
    def __init__(self,libs:dict = cmdlib.dav):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
        to_create = {
                    'absence' : NcOccDavAbsence,
                    'retention' : NcOccDavRetention,

            }
        self._generate_subobjs(to_create)
        
    @property
    def absence(self)->NcOccDavAbsence:
        "Returns corresponding object :: "
        return self._lib['absence']

    def clear_calendar_unshares(self):
        "Clear calendar unshares for a user"
        cmd = self._lib['clear-calendar-unshares']['command']
        return self._process([cmd])
                    
    def clear_contacts_photo_cache(self):
        " Clear cached contact photos"
        cmd = self._lib['clear-contacts-photo-cache']['command']
        return self._process([cmd])
                    
    def create_addressbook(self):
        " Create a dav addressbook"
        cmd = self._lib['create-addressbook']['command']
        return self._process([cmd])
                    
    def create_calendar(self):
        "Create a dav calendar"
        cmd = self._lib['create-calendar']['command']
        return self._process([cmd])
                    
    def create_subscription(self):
        "Create a dav subscription"
        cmd = self._lib['create-subscription']['command']
        return self._process([cmd])
                    
    def delete_calendar(self):
        "Delete a dav calendar"
        cmd = self._lib['delete-calendar']['command']
        return self._process([cmd])
                    
    def delete_subscription(self):
        "Delete a calendar subscription for a user"
        cmd = self._lib['delete-subscription']['command']
        return self._process([cmd])
                    
    def fix_missing_caldav_changes(self):
        " Insert missing calendarchanges rows for existing events"
        cmd = self._lib['fix-missing-caldav-changes']['command']
        return self._process([cmd])
                    
    def list_addressbooks(self):
        "List all addressbooks of a user"
        cmd = self._lib['list-addressbooks']['command']
        return self._process([cmd])
                    
    def list_calendar_shares(self):
        " List all calendar shares for a user"
        cmd = self._lib['list-calendar-shares']['command']
        return self._process([cmd])
                    
    def list_calendars(self):
        " List all calendars of a user"
        cmd = self._lib['list-calendars']['command']
        return self._process([cmd])
                    
    def list_subscriptions(self):
        " List all calendar subscriptions for a user"
        cmd = self._lib['list-subscriptions']['command']
        return self._process([cmd])
                    
    def move_calendar(self):
        "Move a calendar from an user to another"
        cmd = self._lib['move-calendar']['command']
        return self._process([cmd])
                    
    def remove_invalid_shares(self):
        "Remove invalid dav shares"
        cmd = self._lib['remove-invalid-shares']['command']
        return self._process([cmd])
                    
    @property
    def retention(self)->NcOccDavRetention:
        "Returns corresponding object :: "
        return self._lib['retention']

    def send_event_reminders(self):
        " Sends event reminders"
        cmd = self._lib['send-event-reminders']['command']
        return self._process([cmd])
                    
    def sync_birthday_calendar(self):
        " Synchronizes the birthday calendar"
        cmd = self._lib['sync-birthday-calendar']['command']
        return self._process([cmd])
                    
    def sync_system_addressbook(self):
        "Synchronizes users to the system addressbook"
        cmd = self._lib['sync-system-addressbook']['command']
        return self._process([cmd])
                    
