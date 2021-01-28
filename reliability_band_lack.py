#! home/jeremy/anaconda3/bin/python

import matplotlib.pyplot as plt
import numpy as np
from sys import argv, exit
import math as m
import matplotlib.cm as cm

if len(argv) !=  2:
    exit('\n\tError: Wrong Arguments\
            \n\tExample: [program] [Star forming region] [remove(band/non)]\
            \n')

def data_process(path, name) :

    cat = open(path+'/' + name + '/{}_6D_diag_BD_GP_out_catalog.tbl'.format(name), 'r')
    new = []
    for line in cat :
        Line = line.split()
        new.append(Line)
    print("\nTotal number of objects in {} : ".format(name), len(new))

    return np.array(new)


path = '/home/jeremy/YSO_project/test_newBD/data/6D_bin1.0_sigma2_bond0_refD5'
cat = data_process(path, argv[1])
remove_LESS = []
DiagID = 271

for point in cat :
#    print(point[271])
    if point[DiagID][7:] != 'LESS3BD' :
        remove_LESS.append(point)

lack = []

for i in range(3) :
    correspond = []
    for point in remove_LESS :
        if point[DiagID][:6] == str(i+3) + 'bands' :
            correspond.append(point)
    lack.append(np.array(correspond))

lack = np.array(lack)
print(lack[0])    
