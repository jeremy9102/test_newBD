#! home/jeremy/anaconda3/bin/python

import matplotlib.pyplot as plt
import numpy as np
from sys import argv, exit
import math as m
import matplotlib.cm as cm

if len(argv) != 2 :
    exit('\n\tError: Wrong Arguments\
            \n\tExample: [program] [input data] \
            \n')

#---------------------------------------------------------------------------------------#
# Loading Data
SEIP_upper = '../data/test_new_projection/GPV_after_smooth_6D_bin1.0_sigma2_bond0_refD5/after_smooth_lack_0_012345_6D_lower_bounds_AlDiag.npy'
#SEIP_upper = '/mazu/users/jordan/YSO_Project/SEIP_GP_Bound/GPV_after_smooth_6D_bin1.0_sigma2_bond0_refD5/after_smooth_lack_0_012345_6D_lower_bounds_AlDiag.npy'
orig        = np.array([4., 8.0, 7.0, 5.0, 5.0, 3.5])
#bound  = orig + 1.0 * np.array([np.load(SEIP_upper)[i] for i in range(len(np.load(SEIP_upper)))])
bound = np.load(SEIP_upper)
cat = np.load(argv[1])
bandID = [35, 98, 119, 140, 161, 182]
cat_bin = np.array([list(map(float, point[275].split(','))) for point in cat])
cat_type = [point[271] for point in cat]
cat = np.array([[float(point[i]) for i in bandID] for point in cat])
cat_bin = np.delete(cat_bin, 5, axis = 1)
bound = np.delete(bound, 5, axis = 1)
#---------------------------------------------------------------------------------------#
for i in range(len(cat_bin)) :
    probing = []
    for j in range(len(bound)) :
        non_zero = []
        classify = False
        for axis in range(len(cat_bin[i])) :
            if cat_bin[i][axis] != 0 and cat_bin[i][axis] != -999 :
                non_zero.append(axis)
        diff = np.array([cat_bin[i][a] - bound[j][a] for a in non_zero])
        for k in range(1, len(diff)) :
            if diff[0] == diff[k] and k == len(diff)-1 :
                classify = True
                probing.append(list(bound[j]))
            if diff[0] != diff[k] :
                break
    print("#" + str(i+1) + " obj position and results type: ", cat_bin[i], cat_type[i])
    print("BD on probing axis : ", probing)
    print()
                



