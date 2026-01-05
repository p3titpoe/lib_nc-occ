import occ_command_lib as cmdlib
from occ_transformer import base

class ClsNameLib:
    def __init__(self):
        self.names = []
        self.pfix = "NcOcc"

    def add(self,val):
        self.names.append(val)

    def make_obj_to_init(self)->str:
        """
        Some words are separated by dash,
        They have to be rebuid
        :return:
        """
        txt = """
        to_create = {
        """
        pfix = "NcOcc"
        spl = self.names[0]
        wlist:list[str] = self.names[1:]
        # kys = [f"{prf}{v}" for v in wlist]
        for k in wlist:
            ind = 20
            if k == wlist[0]:
                ind = 12
            # Recreate the dict key
            # check for 2nd capital letter and inject a dash at that index
            keyspl = k.split(spl)[1]
            capitals = [keyspl.index(x) for x in keyspl if x.isupper()]
            capitals = capitals[1:]
            key = keyspl.lower()
            if len(capitals) > 0:
                key_seq =[x if i not in capitals else f"-{x}" for i,x in enumerate(key)]
                key = "".join(key_seq)
            # print(capitals)

            txt += f"{'':>{ind}}'{key}' : {pfix}{k},\n"

        txt +="""
            }
        """
        return txt

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
        "{description}"
        cmd = self._lib['{libname}']['command']
        return self._process([cmd])            
"""

func_ref_param ="""
    def {funcname}(self,value):
        "{description}"
        cmd = self._lib['{libname}']['command']
        return self._process([cmd,value])       
"""

func_ref_objs ="""
    @property
    def {funcname}(self)->NCOcc:
        "Returns corresponding object :: {description}"
        return self._lib['{libname}']
"""

py_imports = """from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass
"""

two_param = ['add','delete','edit','update','put','get','transfer-ownership']
reserved_words = {'import':'imports'}

cls_names = ClsNameLib()


def sanitize_func_name(fname:str)->str:
    if "-" in fname:
        fname = fname.replace("-", "_")
    elif fname in reserved_words:
        fname = reserved_words[fname]

    return fname

def generate_classes(skel:dict,classname:str,libname:str,path_to:str=None):
    main_class=""
    main_class_funcs = ""
    subclasses = []
    #Check for dashes
    if "-" in classname:
        excn = classname.split("-")
        classname = f"{excn[0]}{excn[1].capitalize()}"
        print(f"{classname} was dashed")
    #Check the path
    if path_to is not None:
        path_to = f"{path_to}['{libname}']"
    else:
        path_to=libname
    ####Start creation ####
    head = header[:]
    head = head.format('{}',clname = classname,libname = libname,path_to=path_to)
    main_class += head
    cls_names.add(classname)
    for k,v in skel.items():
        ref = func_ref_normal[:]
        if k == 'occ_lib_name':
            break
        if len(v) > 3 or 'command' not in v.keys():
            ss = str(k).capitalize()
            subclasses.append(generate_classes(skel=v,classname=f"{classname}{ss}",libname=ss.lower(),path_to=path_to))
            ref = func_ref_objs[:]
            # print(k,v)
            # continue
        if k in two_param:
            ref = func_ref_param[:]

        funcname = sanitize_func_name(k)
        print(k,v)
        desc = ""
        if 'desc' in v.keys():
            desc = v['desc']
        func = ref.format(funcname=funcname,libname=k,description=desc)
        main_class_funcs += func


    main_class += cls_names.make_obj_to_init()
    main_class += main_class_funcs
    subs = reversed(subclasses)
    grand_out =""
    for s in subs:
        grand_out += s
    grand_out += main_class
    return grand_out

def update_init(classnames:str):
    initf = f"{base}/lib/__init__.py"
    with open(initf,"a+") as ini:
        ini.write(classnames)

def compose_classes(write_files=True, write_ini=True,verbose=True,debug_txt=False) :
    suffix='_occ'
    # members = cmdlib.members_occ_lib
    members =['files']
    import_base = ""

    for section in members:
        cls_names.rm()
        fname = f"{section}{suffix}"
        filename = f"{base}/lib/{fname}.py"
        import_base = f"from lib_occ.lib.{fname} import "

        filetxt = ""
        filetxt += py_imports
        skel = getattr(cmdlib,section)
        filetxt += generate_classes(skel,section.capitalize(),section)
        if debug_txt:
            print(filetxt)
        if write_files:
            with open(filename,"w") as fn:
                fn.write(filetxt)
        gen_classnames = reversed([f"NcOcc{x}" for x in cls_names.names])
        nn = ",".join(gen_classnames)
        # import_base = import_base+" "+",".join(gen_classnames)
        import_base = import_base+" "+nn

        print(cls_names.make_obj_to_init())
        if verbose:
            print("Created classes",nn)

        if write_ini:
            update_init(f"{import_base}\n")
        cls_names.rm()


# def function_tests(classnames:list[str],modulename:str):
#
#     for c in classnames:
#         lbname = f"lib_occ.lib.{modulename}"
#         cls = ","
#         try:
#             from lib_occ.lib import


compose_classes(True,False)
