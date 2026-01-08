import subprocess
from pathlib import Path
from dataclasses import dataclass,field
from json import loads


base = Path(__file__).parent
root = base.parent

class OccCaller:
    _user:str = ""

    def __repr__(self):
        out = f"User : {self._user}"
        return out

    @property
    def user(self)->str:
        return self._user

    def set_user(self,user:str):
        self._user = user

    def make_call(self)->list:
        www:list = ['php','/var/www/nextcloud/occ']
        out:list = ['sudo','-u ','www-data php','/var/www/nextcloud/occ']
        if self._user == "www-data":
            out = www
        return out

    def display(self):
        print(self._user)
        return self._user

UserReg:OccCaller = OccCaller()



@dataclass(init=False)
class OccResponse:
    """
    Handles subprocess.CompletedProcess as to have
    an unified response.
    json.loads the data if successful.
    rtype holds the type of the response
    """
    response:str = ""
    response_str:str = ""
    cmd:str = ""
    rtype:str = ""

    def __init__(self,resp:subprocess.CompletedProcess):
        rsp = resp.stderr if resp.stdout == "" else resp.stdout
        self.response = loads(rsp)
        self.response_str = rsp
        self.cmd = resp.args[1]
        self.rtype = type(self.response)

@dataclass
class NCOcc:
    """
    Base class of every class in the library.

    """
    _lib:dict[str:str]
    name:str = None
    _output = "--output=json"

    def __post_init__(self):
        self.name = self.__class__.__name__.replace("NcOcc","")

    def _set_lib(self,name:str,value:str):
        if name not in self._lib and isinstance(value,str):
            self._lib[name] = value

    def _generate_subobjs(self, kyval: dict[str, str]):
        for k, v in kyval.items():
            obj = v()
            self._lib[k] = obj

    def update_lib(self,what:str|dict,value:str=None)->bool:
        """
        Updates elements in the lib
        :param what:
        :param value:
        :return:
        """
        out = False
        if isinstance(what,dict):
            self._lib = {}
            for k,v in what.items():
                self._set_lib(k,v)
                out = True
        elif isinstance(what,str):
            self._set_lib(what,value)
            out = True
        return out

    def _process(self,args:str|list,capture_output:bool=True,txt:bool=True)->OccResponse:
        arg = UserReg.make_call()
        args.append(self._output)
        arg.extend(args)
        # proc:list = [f"{str(base)}/./process.sh"]
        # proc.extend(args)
        result = subprocess.run(args=args, capture_output=capture_output,text=True)
        res = OccResponse(result)
        return (res)

    @property
    def section_func_list(self, inlist:dict = None):
        """
        Prints all function to the screen
        :param inlist:
        :return:
        """
        wdict:dict = self._lib
        if inlist is not  None:
            wdict = inlist
        max = sorted([len(x) for x in wdict.keys()],reverse=True)[0]

        ll = {k:v['desc'] if isinstance(v,dict) else f"Link to Object"  for k,v in wdict.items()}
        print(f"### METHODS for Object {self.name} ###")
        for k, v in ll.items():
            if "occ_lib" not in k:
                ind = max-len(k)
                print(f"-- {k} {'':<{ind}}: {v}")
        print()

















