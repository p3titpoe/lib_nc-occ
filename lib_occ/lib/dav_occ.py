from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccDavRetention(NCOcc):
    def __init__(self,libs:dict = cmdlib.dav['retention']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def clean_up(self)-> str:
        cmd = self._lib['clean-up']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccDavAbsence(NCOcc):
    def __init__(self,libs:dict = cmdlib.dav['absence']):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def get(self,value):
        cmd = self._lib['get']['command']
        return self._process([cmd,value])       

    def set(self)-> str:
        cmd = self._lib['set']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccDav(NCOcc):
    def __init__(self,libs:dict = cmdlib.dav):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def absence(self)->NCOcc:
        return self._lib['absence']

    def clear_calendar_unshares(self)-> str:
        cmd = self._lib['clear-calendar-unshares']['command']
        return self._process([cmd])            

    def clear_contacts_photo_cache(self)-> str:
        cmd = self._lib['clear-contacts-photo-cache']['command']
        return self._process([cmd])            

    def create_addressbook(self)-> str:
        cmd = self._lib['create-addressbook']['command']
        return self._process([cmd])            

    def create_calendar(self)-> str:
        cmd = self._lib['create-calendar']['command']
        return self._process([cmd])            

    def create_subscription(self)-> str:
        cmd = self._lib['create-subscription']['command']
        return self._process([cmd])            

    def delete_calendar(self)-> str:
        cmd = self._lib['delete-calendar']['command']
        return self._process([cmd])            

    def delete_subscription(self)-> str:
        cmd = self._lib['delete-subscription']['command']
        return self._process([cmd])            

    def fix_missing_caldav_changes(self)-> str:
        cmd = self._lib['fix-missing-caldav-changes']['command']
        return self._process([cmd])            

    def list_addressbooks(self)-> str:
        cmd = self._lib['list-addressbooks']['command']
        return self._process([cmd])            

    def list_calendar_shares(self)-> str:
        cmd = self._lib['list-calendar-shares']['command']
        return self._process([cmd])            

    def list_calendars(self)-> str:
        cmd = self._lib['list-calendars']['command']
        return self._process([cmd])            

    def list_subscriptions(self)-> str:
        cmd = self._lib['list-subscriptions']['command']
        return self._process([cmd])            

    def move_calendar(self)-> str:
        cmd = self._lib['move-calendar']['command']
        return self._process([cmd])            

    def remove_invalid_shares(self)-> str:
        cmd = self._lib['remove-invalid-shares']['command']
        return self._process([cmd])            

    def retention(self)->NCOcc:
        return self._lib['retention']

    def send_event_reminders(self)-> str:
        cmd = self._lib['send-event-reminders']['command']
        return self._process([cmd])            

    def sync_birthday_calendar(self)-> str:
        cmd = self._lib['sync-birthday-calendar']['command']
        return self._process([cmd])            

    def sync_system_addressbook(self)-> str:
        cmd = self._lib['sync-system-addressbook']['command']
        return self._process([cmd])            
