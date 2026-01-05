import subprocess
from pprint import pp
from dataclasses import dataclass,field

@dataclass
class NCOcc:
    name:str = None
    _lib:dict[str:str] =field(default_factory=dict)
    _output = "--output=json"
    def _set_lib(self,name:str,value:str):
        if name not in self._lib and isinstance(value,str):
            self._lib[name] = value

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
        args.append(self._output)
        ff = f"args={args}, capture_output={capture_output},text={txt}"
        # result = subprocess.run(args=args, capture_output=capture_output,text=txt)
        # return (result.stdout)
        return ff













