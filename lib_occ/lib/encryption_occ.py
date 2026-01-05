from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccEncryption(NCOcc):
    def __init__(self,libs:dict = cmdlib.encryption):
        if libs is None:
            libs = {}
        super().__init__(libs)

    def change_key_storage_root(self)-> str:
        cmd = self._lib['change-key-storage-root']['command']
        return self._process([cmd])            

    def decrypt_all(self)-> str:
        cmd = self._lib['decrypt-all']['command']
        return self._process([cmd])            

    def disable(self)-> str:
        cmd = self._lib['disable']['command']
        return self._process([cmd])            

    def enable(self)-> str:
        cmd = self._lib['enable']['command']
        return self._process([cmd])            

    def encrypt_all(self)-> str:
        cmd = self._lib['encrypt-all']['command']
        return self._process([cmd])            

    def list_modules(self)-> str:
        cmd = self._lib['list-modules']['command']
        return self._process([cmd])            

    def migrate_key_storage_format(self)-> str:
        cmd = self._lib['migrate-key-storage-format']['command']
        return self._process([cmd])            

    def set_default_module(self)-> str:
        cmd = self._lib['set-default-module']['command']
        return self._process([cmd])            

    def show_key_storage_root(self)-> str:
        cmd = self._lib['show-key-storage-root']['command']
        return self._process([cmd])            

    def status(self)-> str:
        cmd = self._lib['status']['command']
        return self._process([cmd])            
