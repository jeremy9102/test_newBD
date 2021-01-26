#! home/jeremy/anaconda3/bin/python

import matplotlib.pyplot as plt
import numpy as np
from sys import argv, exit
import math as m
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

if len(argv) != 5 :
    exit('\n\tError: Wrong Arguments\
            \n\tExample: [program] [input data] [type of results] [Star forming region] [remove(band/non)] \
            \n')

def calculate(point, dimen) :
    va = (np.sum(np.array([point[a]**2 for a in range(dimen)])))**0.5
    vb = dimen**0.5
    dot = np.sum(np.array(point))
    cos = dot / (va*vb)
    if 1 - cos < 10**-10:
        sin = 0
        e = va*cos / (dimen)**0.5
        vec = np.array([0*a for a in range(dimen)])
        Vec = 0
    else :
        sin = (1-cos**2)**0.5
        e = va*cos / (dimen)**0.5
        vec = np.array([point[a]-e for a in range(dimen)])
        Vec = np.sum([vec[a]**2 for a in range(dimen)])**0.5
    if Vec != 0 :
        basic = np.array([vec[a] / Vec for a in range(dimen)])
    else :
        basic = np.array([0*a for a in range(dimen)])
    H = va * cos
    R = va * sin
    '''
    print("Input : ", point)
    print("va, vb : ", va, vb)
    print("Dot : ", dot)
    print("cos, sin : ", cos, sin)
    print("e, vec, Vec : ", e, vec, Vec)
    print("R, H : ", R, H)
    print(basic)
    '''
    return R, H, basic

def order(cat) :
    for i in range(len(cat[0])) :
        for j in range(len(cat[0])) :
            if cat[0][j] > cat[0][i] :
                displace = cat[0][j] ; cat[0][j] = cat[0][i] ; cat[0][i] = displace
                displace = cat[1][j] ; cat[1][j] = cat[1][i] ; cat[1][i] = displace
                displace = cat[2][j] ; cat[2][j] = cat[2][i] ; cat[2][i] = displace
    return cat

def angle(A, B, r, dimen) :
    #print()
    #print("A, B r : ", A, B, r)
    Dot = np.sum(np.array([A[a] * B[a] for a in range(dimen)]))
    #print("Dot", Dot)
    va = np.sum(np.array([A[a]**2 for a in range(dimen)]))**0.5
    vb = np.sum(np.array([B[a]**2 for a in range(dimen)]))**0.5
    #print("va, vb : ", va, vb)
    if va == 0 or vb == 0 :
        theta = 0
        limit = 90
    #    print("theta, limit : ", theta, limit)
    else :
        if va > 1 or vb > 1 :
            va = 1 ; vb = 1
        elif va < -1 or vb < -1 :
            va = -1 ; vb = -1
        cos = Dot / va / vb
        if cos > 1 :
            cos = 1
        elif cos < -1 :
            cos = -1
        #print(cos)
        theta = m.acos(cos)/m.pi*180
        if r >= 1/2 :
            limit = m.asin(0.5 / r)/m.pi*180
        elif r <= 1/2  and cos >= 0 :
            limit = 90
        elif cos < 0 :
            limit = 0
    return round(theta, 5), round(limit, 5)

#---------------------------------------------------------------------------------------#
# Loading Data
remove = argv[4]
SEIP_upper = '../data/test_new_projection/GPV_after_smooth_6D_bin1.0_sigma2_bond0_refD5/after_smooth_lack_0_012345_6D_lower_bounds_AlDiag.npy'
SEIP_upper = '/mazu/users/jordan/YSO_Project/SEIP_GP_Bound/GPV_after_smooth_6D_bin1.0_sigma2_bond0_refD5/after_smooth_lack_0_012345_6D_lower_bounds_AlDiag.npy'
SWIRE_upper = '/mazu/users/jordan/YSO_Project/SWIRE_GP_Bound/GPV_after_smooth_6D_bin1.0_sigma2_bond0_refD5/after_smooth_lack_0_012345_6D_upper_bounds_AlDiag.npy'
orig        = np.array([4., 8.0, 7.0, 5.0, 5.0, 3.5])
bdname = 'SEIP'
bound = np.load(SEIP_upper)
#bound = np.load(SWIRE_upper)
orig  = np.array([4., 8.0, 7.0, 5.0, 5.0, 3.5])
bound = orig + 1.0 * np.array([bound[i] for i in range(len(bound))])

cat = np.load(argv[1])
bandID = [35, 98, 119, 140, 161, 182]
#cat = np.array([[float(point[i]) for i in bandID] for point in cat])
cat = np.array([list(map(float, point[275].split(','))) for point in cat])
cat = orig + 1.0 * np.array([cat[i] for i in range(len(cat))])
#---------------------------------------------------------------------------------------#
Test = 'cat'
if Test == 'cat' :
    print("Position of "+argv[2]+" data")

    YG = []
    for i in range(len(cat)) :
        if remove == 'non' :
            point = cat[i]
        else :
            point = np.delete(cat[i], float(remove))
        D = len(point)
        zero = []
        print(point)
        for j in range(D) :
            if point[j] == -999 or point[j] == 0 :
                zero.append(j)
        putin = np.delete(point, np.where(point == 0))
        putin = np.delete(putin, np.where(putin == -999))
        #print(putin)
        print(putin, D-len(zero))
        r, H, vec = calculate(putin, D-len(zero))
        YG.append([r, H, zero, putin, vec])
        #print([r, H, zero, cat[i], vec])
    print()

    print("Calculation of "+argv[2]+" data")
    for p in range(len(YG[0])) :
        BD = []
        line_BD = []
        Theta = []
        for i in range(len(bound)) :
            if D == 6 :
                test = bound[i]
            else :
                test = np.delete(bound[i], float(remove))
            for i in range(len(YG[p][2])) :
                remove = YG[p][2][len(YG[p][2]) - i - 1]
                test = np.delete(test, remove)
            r, H, vec = calculate(test, D-len(YG[p][2]))
            BD.append([r, H, vec, test])
        #print("BD shape : ", np.shape(BD))
        for i in range(len(BD)) :
            theta , cri = angle(YG[p][4], BD[i][2], BD[i][0], D-len(YG[p][2]))
            #print(theta, cri)
            # if theta  :
            #print(theta, cri, BD[i][0], BD[i][1], BD[i][3])
            line_BD.append(BD[i])
            Theta.append(theta)
        line_BD = np.array(line_BD)
        if len(line_BD) == 0 :
            R = []
            H = []
        else :
            R = np.array(line_BD[:, 0])
            H = np.array(line_BD[:, 1])
        R_YG = (YG[p][0])
        H_YG = (YG[p][1])
        #cm = plt.cm.get_cmap('viridis')
        Theta = np.array(Theta)
        x = R
        y = R#*np.cos(Theta/180*m.pi)
        z = H
#print(H)
#x, y = np.meshgrid(x, y)
for i in range(len(x)) :
    x[i], y[i], z[i] = (float(x[i]), float(y[i]),float(z[i]))
    print(x[i], y[i], z[i])
ax = plt.figure().add_subplot(111, projection = '3d')
ax.scatter(x[:5], y[:5], z[:5])
plt.show()

'''
        c = Theta
        sc = plt.scatter(R, H, c = c, cmap = cm, s = 35, vmin = 0, vmax = 10)
        plt.scatter(R_YG, H_YG, c = 'r', marker = '*', s = 70)
        plt.colorbar(sc, label = 'Angle (degree)')
        plt.title("{0}_{1}_{3}bands_#{2}".format(argv[3], argv[2], str(p+1), len(YG[p][3])))
        plt.xlabel("R (mag)")
        plt.ylabel("H (mag)")
        plt.ylim(18, 38)
        plt.xlim(0, 11)
        if D == 6 :
            plt.savefig(argv[3]+"_"+argv[2]+"_"+bdname+"_RH_diagram_"+str(p+1)+".png")
        else :
            plt.savefig(argv[3]+"_"+argv[2]+"_"+bdname+"_RH_diagram_deleB{}_".format(argv[4])+str(p+1)+".png")
'''





