from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccSharing(NCOcc):
    def __init__(self,libs:dict = cmdlib.sharing):
        if libs is None:
            libs = {}
        super().__init__(libs)
        

    def cleanup_remote_storages(self)-> str:
        "Cleanup shared storage entries that have no matching entry in the sharesexternal table"
        cmd = self._lib['cleanup-remote-storages']['command']
        return self._process([cmd])            

    def delete_orphan_shares(self)-> str:
        " Delete shares where the owner no longer has access to the file"
        cmd = self._lib['delete-orphan-shares']['command']
        return self._process([cmd])            

    def expiration_notification(self)-> str:
        "Notify share initiators when a share will expire the next day"
        cmd = self._lib['expiration-notification']['command']
        return self._process([cmd])            

    def fix_share_owners(self)-> str:
        " Fix owner of broken shares after transfer ownership on old versions"
        cmd = self._lib['fix-share-owners']['command']
        return self._process([cmd])            
