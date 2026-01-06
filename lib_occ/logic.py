import subprocess
from pprint import pp
from pathlib import Path
from dataclasses import dataclass,field

base = Path(__file__).parent
root = base.parent



@dataclass
class NCOcc:
    _lib:dict[str:str]
    name:str = None
    _output = "--output=json"

    def _set_lib(self,name:str,value:str):
        if name not in self._lib and isinstance(value,str):
            self._lib[name] = value

    def _generate_subobjs(self, kyval: dict[str, str]):
        for k, v in kyval.items():
            obj = v()
            self._lib[k] = obj

    def update_lib(self,what:str|dict,value:str=None)->bool:
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

    def _process(self,args:str|list,capture_output:bool=True,txt:bool=True):
        arg = ['sudo','-u ','www-data php','/var/www/nextcloud/occ']
        args.append(self._output)
        arg.extend(args)
        proc:list = [f"{str(base)}/./process.sh"]
        proc.extend(args)
        result = subprocess.run(args=proc, capture_output=capture_output,text=True)
        print(result)
        return (result.stdout)
        # return ff













