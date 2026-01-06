from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass

@dataclass(init=False)
class NcOccMaintenanceUpdate(NCOcc):
    def __init__(self,libs:dict = cmdlib.maintenance['update']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        

    def htaccess(self)-> str:
        "Updates the htaccess file"
        cmd = self._lib['htaccess']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccMaintenanceTheme(NCOcc):
    def __init__(self,libs:dict = cmdlib.maintenance['theme']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        

    def update(self,value):
        " Apply custom theme changes"
        cmd = self._lib['update']['command']
        return self._process([cmd,value])       

@dataclass(init=False)
class NcOccMaintenanceMimetype(NCOcc):
    def __init__(self,libs:dict = cmdlib.maintenance['mimetype']):
        if libs is None:
            libs = {}
        super().__init__(libs)
        

    def update_db(self)-> str:
        " Update database mimetypes and update filecache"
        cmd = self._lib['update-db']['command']
        return self._process([cmd])            

    def update_js(self)-> str:
        " Update mimetypelistjs"
        cmd = self._lib['update-js']['command']
        return self._process([cmd])            

@dataclass(init=False)
class NcOccMaintenance(NCOcc):
    def __init__(self,libs:dict = cmdlib.maintenance):
        if libs is None:
            libs = {}
        super().__init__(libs)
        
        to_create = {
                    'mimetype' : NcOccMaintenanceMimetype,
                    'theme' : NcOccMaintenanceTheme,
                    'update' : NcOccMaintenanceUpdate,

            }
        self._generate_subobjs(to_create)
        

    def data_fingerprint(self)-> str:
        " update the systems datafingerprint after a backup is restored"
        cmd = self._lib['data-fingerprint']['command']
        return self._process([cmd])            

    @property
    def mimetype(self)->NCOcc:
        "Returns corresponding object :: "
        return self._lib['mimetype']

    def mode(self)-> str:
        " Show or toggle maintenance mode status"
        cmd = self._lib['mode']['command']
        return self._process([cmd])            

    def repair(self)-> str:
        " repair this installation"
        cmd = self._lib['repair']['command']
        return self._process([cmd])            

    def repair_share_owner(self)-> str:
        " repair invalid shareowner entries in the database"
        cmd = self._lib['repair-share-owner']['command']
        return self._process([cmd])            

    @property
    def theme(self)->NCOcc:
        "Returns corresponding object :: "
        return self._lib['theme']

    def update(self,value):
        ""
        cmd = self._lib['update']['command']
        return self._process([cmd,value])       
