import occ_command_lib as cmdlib
from occ_transformer import base




def sanitize_func_name(fname:str,chk_reserved=True)->str:
    if "-" in fname:
        fname = fname.replace("-", "_")
    elif fname in reserved_words:
        if chk_reserved:
            fname = reserved_words[fname]

    return fname


class ClsNameLib:
    def __init__(self):
        self.names = []
        self.paths = {}
        self.pfix = "NcOcc"

    def add(self,val:str,path:list[str]):
        self.names.append(val)
        # clsname = self.pfix+val
        if val not in self.paths:
            self.paths[val] = []
        if path is not None:
            self.paths[val].append(path)

    def update(self,clsname:str,val:str):
        self.paths[clsname].append(val)

    def make_obj_to_init(self,classname:str)->str:
        """
         makes the to_create dict  for class init
        """
        txt = """
        to_create = {
        """
        class_objs = self.paths[classname]
        if len(class_objs) == 0:
            return ""

        for k in class_objs:
            ind = 20
            if k == class_objs[0]:
                ind = 12
            # Create classnames
            txt += f"{'':>{ind}}'{k}' : {self.pfix}{classname}{k.capitalize()},\n"
        txt +="""
            }
        self._generate_subobjs(to_create)
        """
        # print(txt)
        return txt

    def make_prefixed_names(self)->list[str]:
        return  [f"{self.pfix}{k}" for k in self.names]

    def rm(self):
        self.names = []
        self.paths = {}

header = """
@dataclass(init=False)
class NcOcc{clname}(NCOcc):
    def __init__(self,libs:dict = cmdlib.{path_to}):
        if libs is None:
            libs = {}
        super().__init__(libs)
        {repl_init}
"""

func_ref_normal ="""    def {funcname}(self):
        "{description}"
        cmd = self._lib['{libname}']['command']
        return self._process([cmd])
                    
"""

func_ref_param ="""    def {funcname}(self,value) -> {returnobject}:
        "{description}"
        cmd = self._lib['{libname}']['command']
        return self._process([cmd,value])       

"""

func_ref_objs ="""    @property
    def {funcname}(self)->{returnobject}:
        "Returns corresponding object :: {description}"
        return self._lib['{libname}']

"""

py_imports = """from lib_occ.creation import occ_command_lib as cmdlib
from lib_occ.logic import NCOcc
from dataclasses import dataclass
"""

two_param = ['add','delete','edit','update','put','get','transfer-ownership']
reserved_words = {'import':'imports','list':'lists'}

cls_names = ClsNameLib()



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
    head = head.format('{}',clname = classname,libname = libname,path_to=path_to,repl_init="{**}")
    main_class += head
    cls_names.add(classname, None)
    for k,v in skel.items():
        returnobject = ""
        ref = func_ref_normal[:]
        if k == 'occ_lib_name':
            break
        if len(v) > 3 or 'command' not in v.keys():
            cls_names.update(classname, k)

            ss = str(k).capitalize()
            clsname = f"{classname}{ss}"

            subclasses.append(generate_classes(skel=v,classname=clsname,libname=ss.lower(),path_to=path_to))
            ref = func_ref_objs[:]
            returnobject = "NcOcc"+clsname
            # print(k,v)
            # continue
        if k in two_param:
            ref = func_ref_param[:]
            returnobject = "str"

        funcname = sanitize_func_name(k)
        # print(k,v)
        desc = ""
        if 'desc' in v.keys():
            desc = v['desc']
        func = ref.format(funcname=funcname,libname=k,description=desc,returnobject=returnobject)
        main_class_funcs += func

    main_class += main_class_funcs
    subs = reversed(subclasses)
    grand_out =[]
    for s in subs:
        grand_out.extend(s)
    grand_out.append(main_class)
    return grand_out

def update_init(classnames:str):
    initf = f"{base}/lib/__init__.py"
    with open(initf,"a+") as ini:
        ini.write(classnames)

def compose_classes(write_files=True, write_ini=True,verbose=True,debug_txt=False) :
    suffix='_occ'
    members = cmdlib.members_occ_lib
    # members =['files']
    import_base = ""

    for section in members:
        cls_names.rm()
        fname = f"{section}{suffix}"
        filename = f"{base}/lib/{fname}.py"
        import_base = f"from lib import {fname} as {section}"

        filetxt = ""
        filetxt += py_imports
        skel = getattr(cmdlib,section)
        class_list:list[str] = generate_classes(skel,section.capitalize(),section)
        if len(class_list) == len(cls_names.paths):
            rev = [x for x in cls_names.paths.keys()]
            rev.reverse()
            for i,c in enumerate(rev):
                repl = cls_names.make_obj_to_init(c)
                class_list[i] = class_list[i].replace("{**}", repl)
                filetxt += class_list[i]

        if debug_txt:
            print(filetxt)
        if write_files:
            with open(filename,"w") as fn:
                fn.write(filetxt)
        gen_classnames = reversed(cls_names.make_prefixed_names())
        nn = ",".join(gen_classnames)
        # import_base = import_base+" "+",".join(gen_classnames)
        # import_base = import_base+" "+nn

        # print(cls_names.make_obj_to_init())
        if verbose:
            print("Created classes",nn)

        if write_ini:
            update_init(f"{import_base}\n")
        cls_names.rm()

compose_classes(False,True,False)
