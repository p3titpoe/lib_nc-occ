#!/usr/bin/python
#from lib import nc_occ as occ
#from .lib import nc_occ as occ
from lib_occ.nc_occ import common
from pprint import pp

tt = common.NcOccCommon()
rs = tt.lists()

print(rs)


