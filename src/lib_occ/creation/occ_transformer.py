from pprint import pp
from dataclasses import dataclass,field
from pathlib import  Path
from lib_occ.logic import base,root


occ_file = f"{base}/creation/occ_list.txt"
occ_lib = f"{base}/creation/occ_command_lib.py"
occ_classes = f"{base}/occ_classes.py"

def get_file_content(file:str):
    with open(occ_file,"r") as f:
        file_content = f.readlines()
    return file_content

def transform_to_dict():
    """ Transforrms the textfile into a dict """
    tree = {}
    fc = get_file_content(occ_file)
    active_group =""
    for line in fc:
        expl_line = line.split("  ")
        tmp ={"command":"","desc":""}
        for i,v in enumerate(expl_line):
            if i == 0 and v != "":
                val = "".join([x for x in v if x.isalnum()])
                tree[val] = {}
                active_group= tree[val]
            elif i == 1 and v != "":
                tmp['command']=v
            elif i == len(expl_line)-1 and v !="":
                tmp['desc'] = "".join([x for x in v if x.isalnum() or x == " "])
                active_group[tmp['command']] = tmp
            else:
                pass
    return tree

def organize_tree(tree:dict):
    """ Organizes the created dict into a more fancy visual dict """
    sorted = {}
    paths = [[k.split(":"),v] for k,v in tree.items()]
    for p in paths:
        active = sorted
        fpath = p[0]
        val = p[1]
        val['path'] = fpath
        for k in fpath:
            if k !=fpath[-1]:
                if k not in active:
                    active[k]={}
                active = active[k]
        active[fpath[-1]] = val
    # pp(sorted)
    return sorted

def make_blocks(inp:dict,indent)->str|bool:
    """ Generates textblocks from a given dict """
    out = ""
    for j, l in inp.items():
        if 'path' in inp and j =="command":
            out = f"{'':>{indent}} '{l}': "
            out += f"{inp}"+ ",\n"
            break
        elif len(l) > 3 or 'command' not in l.keys():
            out += f"{'':>{indent}} '{j}':"+"{\n"
            out += make_blocks(l, indent+8)
            out += f"{'':>{indent}}" + "},\n"

        else:
            out += f"{'':>{indent}} '{j}': "
            out += f"{l},\n"
    return out

def create_occ_def(tree:dict,name:str)->str:
    """ Orchestrates the text creation from a given tree """

    out="\n"
    submod = 1
    pad = 4
    def get_ind():
        return submod*pad

    out = f"{name} = "+"{\n"
    for k,v in tree.items():
        if len(v) == 3:
            submod = 1
        else:
            submod +=1
        bl = make_blocks(v,get_ind())
        if not bl:
            submod +=1
            bl = f"{'':>{get_ind()}}"+"{},"
        out += bl
    # out += f"{'':>5}'submodules':{[x for x in tree if x !="__single__"]},\n"
    out += f"{'':>5}'occ_lib_name':'{name}'\n"
    out += "}\n"
    return out

def compose():
    """ Orchestrates the occ_command_lib.py creations

        That files is the skeleton upon which the classes files
        will be created on
     """
    if Path(occ_lib).exists():
        consent = input("occ_command_lib.py already exists!\n Are you sure want to overwite it? [y/N]")
        if consent.lower() != 'y':
            exit("Exited")
    t = transform_to_dict()
    txt = "### Definition Library\n"

    defs = []
    for k,v in t.items():
        defs.append(k)
        org_t = organize_tree(v)
        txt += create_occ_def(org_t, k)
    txt += f"members_occ_lib = {defs}"
    with open(occ_lib, "w") as ofile:
        ofile.write(txt)
# compose()