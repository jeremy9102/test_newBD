#! home/jeremy/anaconda3/bin/python

import matplotlib.pyplot as plt
import numpy as np
from sys import argv, exit
import math as m
import matplotlib.cm as cm

if len(argv) != 3 :
    exit('\n\tError: Wrong Arguments\
            \n\tExample: [program] [StarForming region/bound] [Results type/tot]\
            \n')

path = '/home/jeremy/YSO_project/test_newBD/data/results/6D_bin1.0_sigma2_bond0_refD5/Compare_HL/'
orig  = np.array([4., 8.0, 7.0, 5.0, 5.0, 3.5])

if argv[1] == 'bound' and argv[2] == 'tot' :
    SEIP_upper = '/mazu/users/jordan/YSO_Project/SEIP_GP_Bound/GPV_after_smooth_6D_bin1.0_sigma2_bond0_refD5/after_smooth_lack_0_012345_6D_lower_bounds_AlDiag.npy'
    bound = np.load(SEIP_upper)
    bound = orig + 1.0 * np.array([bound[i] for i in range(len(bound))])
    cat = bound

else : 
    cat = np.load(path + '{0}_{1}.npy'.format(argv[1], argv[2]))
    cat = np.array([list(map(float, point[275].split(','))) for point in cat])
    cat = orig + 1.0 * np.array([cat[i] for i in range(len(cat))])

for i in range(len(cat)) :
    Sum = np.sum(cat[i])
    new = []
    for band in cat[i] :
        new.append(band/Sum)
    cat[i] = np.array(new)
np.save(path + 'reSED_mag_{0}_{1}.npy'.format(argv[1], argv[2]), cat)
'''
elif argv[3] == 'translate' :
    for i in range(len(cat)) :
        diff = np.array([cat[i][0]-cat[i][a] for a in range(len(cat[i]))])
        cat[i] = cat[i] + diff
        print(cat[i])
    np.save(path + 'reSED_trans_{0}_{1}.npy'.format(argv[1], argv[2]), cat)
'''


