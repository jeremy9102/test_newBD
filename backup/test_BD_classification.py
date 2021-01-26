#! home/jeremy/anaconda3/python3

import numpy as np

def Check_Boundary_Position_Along_Axis(POS_vector, GP_Lower_Bound, GP_Upper_Bound, fixed_ax):
    '''
    This is to find the location of boundary on probing axis
    '''
    POS_vector_ax, POS_ax = np.delete(POS_vector, fixed_ax), POS_vector[fixed_ax]
    GP_Lower_Bound_ax = np.delete(GP_Lower_Bound, fixed_ax, axis=1)
    GP_Upper_Bound_ax = np.delete(GP_Upper_Bound, fixed_ax, axis=1)
    # Find bounary point on probing axis
    POS_bd_ax, indicator = [], 0
    for i in range(len(GP_Lower_Bound_ax)):
        Lbd = GP_Lower_Bound_ax[i]
        Ubd = GP_Upper_Bound_ax[i]
        # Find corresponding points in galaxy populated region -> TBD
        if np.all(POS_vector_ax == Lbd) and np.all(POS_vector_ax == Ubd):
            POS_bd_ax.append(GP_Lower_Bound[i, fixed_ax])
            POS_bd_ax.append(GP_Upper_Bound[i, fixed_ax])
            break
        indicator += 1
    # If no corresponding boundary point
    if (indicator == len(GP_Lower_Bound_ax)):
        POS_bd_ax = np.nan
    return POS_bd_ax, POS_ax


path = "/mazu/users/jordan/YSO_Project/SEIP_GP_Bound/test/GPV_after_smooth_6D_bin1.0_sigma2_bond0_refD5/"
upper = np.load(path+"after_smooth_lack_0_012345_6D_upper_bounds_AlDiag.npy")
lower = np.load(path+"after_smooth_lack_0_012345_6D_lower_bounds_AlDiag.npy")
num =0
V = []
for i in range(len(upper)) :
    if (upper[i]==lower[i]).all() : 
        num += 1 
    V.append(((upper[i][0]-lower[i][0])**2+(upper[i][1]-lower[i][1])**2+(upper[i][2]-lower[i][2])**2+(upper[i][3]-lower[i][3])**2+(upper[i][4]-lower[i][4])**2+(upper[i][5]-lower[i][5])**2)**0.5)
    #print(upper[i], lower[i])
print()
print(round((sum(V)*(1/(2)**0.5)**5),1), num, len(upper),'\n')

for i in range(6) :
    path = "/mazu/users/jordan/YSO_Project/SEIP_GP_Bound/test/GPV_after_smooth_6D_bin1.0_sigma2_bond0_refD5/"
    upper = np.load(path+"after_smooth_lack_0_012345_6D_upper_bounds_AlB"+str(i)+".npy")
    lower = np.load(path+"after_smooth_lack_0_012345_6D_lower_bounds_AlB"+str(i)+".npy")
    num =0
    V = []
    for i in range(len(upper)) :
        if (upper[i]==lower[i]).all() :
            num += 1
        V.append(((upper[i][0]-lower[i][0])**2+(upper[i][1]-lower[i][1])**2+(upper[i][2]-lower[i][2])**2+(upper[i][3]-lower[i][3])**2+(upper[i][4]-lower[i][4])**2+(upper[i][5]-lower[i][5])**2)**0.5)
    #print(upper[i], lower[i])
    print(sum(V), num, len(upper),'\n')

