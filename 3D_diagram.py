#!/home/jeremy/anaconda3/bin/python

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sys import argv, exit

if len(argv) != 3: 
    exit('\n\tError: Wrong Arguments\
            \n\tExample: [program] [input data] [band(3)]\
            \n')

SWIRE_lower = '/mazu/users/jordan/YSO_Project/SWIRE_GP_Bound/GPV_after_smooth_6D_bin1.0_sigma2_bond0_refD5/after_smooth_lack_0_012345_6D_lower_bounds_AlDiag.npy'
SWIRE_upper = '/mazu/users/jordan/YSO_Project/SWIRE_GP_Bound/GPV_after_smooth_6D_bin1.0_sigma2_bond0_refD5/after_smooth_lack_0_012345_6D_upper_bounds_AlDiag.npy'
SEIP_lower = '/mazu/users/jordan/YSO_Project/SEIP_GP_Bound/GPV_after_smooth_6D_bin1.0_sigma2_bond0_refD5/after_smooth_lack_0_012345_6D_upper_bounds_AlDiag.npy'
SEIP_upper = '/mazu/users/jordan/YSO_Project/SEIP_GP_Bound/GPV_after_smooth_6D_bin1.0_sigma2_bond0_refD5/after_smooth_lack_0_012345_6D_lower_bounds_AlDiag.npy'

bound_SWIRE = np.r_[np.load(SWIRE_lower), np.load(SWIRE_upper)]
bound_SEIP  = np.r_[np.load(SEIP_lower), np.load(SEIP_upper)]
orig        = np.array([4., 8.0, 7.0, 5.0, 5.0, 3.5])
bound_SWIRE = orig + 1.0 * np.array([bound_SWIRE[i] for i in range(len(bound_SWIRE))])
bound_SEIP  = orig + 1.0 * np.array([bound_SEIP[i] for i in range(len(bound_SEIP))])

bandID = [35, 98, 119, 140, 161, 182]

cat = np.load(argv[1])
#cat = np.array([[float(point[i]) for i in bandID] for point in cat])
cat = np.array([list(map(float, point[275].split(','))) for point in cat])
band = ['J', 'IR1', 'IR2', 'IR4', 'MP1', 'MP2']

fig = plt.figure()
axis = fig.gca(projection='3d')

b1 = int(argv[2][0])
b2 = int(argv[2][1])
b3 = int(argv[2][2])

p = 0
print(cat[p])
cat_new = []
for i in range(len(cat)) :
    if cat[i][b1] != -999. and cat[i][b2] != -999. and cat[i][b3] != -999. :
        print(cat[i])
        cat_new.append(cat[i])
cat = np.array(cat_new)

#axis.scatter(bound_SEIP[:, b1], bound_SEIP[:, b2], bound_SEIP[:, b3],label = 'galaxy region' , c = 'b' ,marker = '+', s = 100)
#axis.scatter(bound_SWIRE[:, b1], bound_SWIRE[:, b2], bound_SWIRE[:, b3], label = 'galaxy_YSO', marker = 'o', s = 100, facecolors=(0,0,0,0), edgecolors='r')
Diag = np.array([[a, a, a, a, a, a] for a in range(9, 18)])
axis.scatter(bound_SEIP[:, b1], bound_SEIP[:, b2], bound_SEIP[:, b3],label = 'galaxy region' , c = 'r' ,marker = 'o', s = 30)
axis.plot(Diag[:, b1], Diag[:, b2], Diag[:, b3],label = 'Diagonal' , c = 'b')

axis.scatter(cat[:, b1], cat[:, b2], cat[:, b3], label = 'IY_SER', c = 'g', marker = 'o', s = 40)


axis.legend()
axis.set_zlabel(band[b3], fontsize=16)
axis.set_xlabel(band[b1], fontsize=16)
axis.set_ylabel(band[b2], fontsize=16)


plt.show()


