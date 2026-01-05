import occ_command_lib as cmdlib
from occ_transformer import base

header = """
@dataclass(init=False)
class NcOcc{clname}(NCOcc):
    def __init__(self,libs:dict = cmdlib.{libname}):
        if libs is None:
            libs = {}
        super().__init__(libs)
"""

func_ref_normal ="""
    def {funcname}(self):
        cmd = self._lib['{libname}']['command']
        return self._process([cmd])            
"""

func_ref_param ="""
    def {funcname}(self,value):
        cmd = self._lib['{libname}']['command']
        return self._process([cmd,value])       
"""

func_ref_objs ="""
    def {funcname}(self)->NCOcc:
        return self._lib['{libname}']
"""

py_imports = """
import occ_command_lib as cmdlib
from logic import NCOcc
from dataclasses import dataclass
"""

two_param = ['add','delete','edit','update','put','get','transfer-ownership']



def generate_classes(skel:dict,classname:str,libname:str):
    out=""
    subclasses = []
    cl = header.format('{}',clname = classname,libname = libname,)
    out += cl

    for k,v in skel.items():
        # print(k,v)
        ref = func_ref_normal
        if k == 'occ_lib_name':
            break
        if len(v) > 3 or 'command' not in v.keys():
            ss = str(k).capitalize()
            subclasses.append(generate_classes(v,f"{classname}{ss}",ss.lower()))
            ref = func_ref_objs
        if k in two_param:
            ref = func_ref_param
        if "-" in k:
            k = k.replace("-","_")
        func = ref.format(funcname=k,libname=libname)
        out += func
    subs = reversed(subclasses)
    grand_out =""
    for s in subs:
        grand_out += s
    grand_out += out
    return grand_out

def compose_classes() :

    members = ['files']

    for section in members:
        filetxt = ""
        filename = f"{base}/lib/{section}_occ.py"
        print(filename)
        filetxt += py_imports
        filetxt += generate_classes(cmdlib.files,section.capitalize(),section)
        with open(filename,"w") as fn:
            fn.write(filetxt)


compose_classes()
