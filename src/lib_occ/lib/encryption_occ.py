from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccEncryption(NCOcc):
    def __init__(self,libs:dict = cmdlib.encryption):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
    def change_key_storage_root(self):
        " Change key storage root"
        cmd = self._lib['change-key-storage-root']['command']
        return self._process([cmd])
                    
    def decrypt_all(self):
        " Disable serverside encryption and decrypt all files"
        cmd = self._lib['decrypt-all']['command']
        return self._process([cmd])
                    
    def disable(self):
        " Disable encryption"
        cmd = self._lib['disable']['command']
        return self._process([cmd])
                    
    def enable(self):
        "Enable encryption"
        cmd = self._lib['enable']['command']
        return self._process([cmd])
                    
    def encrypt_all(self):
        " Encrypt all files for all users"
        cmd = self._lib['encrypt-all']['command']
        return self._process([cmd])
                    
    def list_modules(self):
        "List all available encryption modules"
        cmd = self._lib['list-modules']['command']
        return self._process([cmd])
                    
    def migrate_key_storage_format(self):
        "Migrate the format of the keystorage to a newer format"
        cmd = self._lib['migrate-key-storage-format']['command']
        return self._process([cmd])
                    
    def set_default_module(self):
        "Set the encryption default module"
        cmd = self._lib['set-default-module']['command']
        return self._process([cmd])
                    
    def show_key_storage_root(self):
        " Show current key storage root"
        cmd = self._lib['show-key-storage-root']['command']
        return self._process([cmd])
                    
    def status(self):
        "Lists the current status of encryption"
        cmd = self._lib['status']['command']
        return self._process([cmd])
                    
