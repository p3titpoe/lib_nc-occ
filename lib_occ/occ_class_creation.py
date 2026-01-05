import occ_command_lib as cmdlib
from occ_transformer import base

class ClsNameLib:
    def __init__(self):
        self.names = []

    def add(self,val):
        self.names.append(val)

    def rm(self):
        self.names = []

header = """
@dataclass(init=False)
class NcOcc{clname}(NCOcc):
    def __init__(self,libs:dict = cmdlib.{path_to}):
        if libs is None:
            libs = {}
        super().__init__(libs)
"""

func_ref_normal ="""
    def {funcname}(self)-> str:
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

py_imports = """from lib_occ import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass
"""

two_param = ['add','delete','edit','update','put','get','transfer-ownership']


cls_names = ClsNameLib()

def generate_classes(skel:dict,classname:str,libname:str,path_to:str=None):
    out=""
    subclasses = []
    if path_to is not None:
        path_to = f"{path_to}['{libname}']"
    else:
        path_to=libname
    # print(skel)
    cl = header.format('{}',clname = classname,libname = libname,path_to=path_to)
    out += cl
    cls_names.add(classname)
    for k,v in skel.items():
        # print(k,v)
        ref = func_ref_normal
        if k == 'occ_lib_name':
            break
        if len(v) > 3 or 'command' not in v.keys():
            ss = str(k).capitalize()
            subclasses.append(generate_classes(skel=v,classname=f"{classname}{ss}",libname=ss.lower(),path_to=path_to))
            ref = func_ref_objs
        if k in two_param:
            ref = func_ref_param
        funcname = k
        if "-" in k:
            funcname = k.replace("-","_")
        func = ref.format(funcname=funcname,libname=k)
        out += func
    subs = reversed(subclasses)
    grand_out =""
    for s in subs:
        grand_out += s
    grand_out += out
    return grand_out

def update_init(classnames:str):
    initf = f"{base}/lib/__init__.py"
    with open(initf,"a+") as ini:
        ini.write(classnames)

def compose_classes() :
    suffix='_occ'
    members = ['files']
    import_base = ""

    for section in members:
        filetxt = ""
        cls_names.rm()
        fname = f"{section}{suffix}"
        filename = f"{base}/lib/{fname}.py"
        import_base = f"from .{fname} import "
        filetxt += py_imports
        filetxt += generate_classes(cmdlib.files,section.capitalize(),section)
        with open(filename,"w") as fn:
            fn.write(filetxt)
        gen_classnames = reversed([f"NcOcc{x}" for x in cls_names.names])
        import_base = import_base+" "+",".join(gen_classnames)
        print(import_base)
        update_init(import_base)


compose_classes()
