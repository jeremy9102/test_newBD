#! home/jeremy/anaconda3/bin/python

import matplotlib.pyplot as plt
import numpy as np
from sys import argv, exit
import math as m
import matplotlib.cm as cm

if len(argv) != 6 :
    exit('\n\tError: Wrong Arguments\
            \n\tExample: [program] [input data] [type of results] [Star forming region] [remove(band/non)] [cat/total/3D]\
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
    print()
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
#SEIP_upper = '../data/test_new_projection/GPV_after_smooth_6D_bin1.0_sigma2_bond0_refD5/after_smooth_lack_0_012345_6D_lower_bounds_AlDiag.npy'
SEIP_upper = '/mazu/users/jordan/YSO_Project/SEIP_GP_Bound/GPV_after_smooth_6D_bin1.0_sigma2_bond0_refD5/after_smooth_lack_0_012345_6D_lower_bounds_AlDiag.npy'
SWIRE_upper = '/mazu/users/jordan/YSO_Project/SWIRE_GP_Bound/GPV_after_smooth_6D_bin1.0_sigma2_bond0_refD5/after_smooth_lack_0_012345_6D_upper_bounds_AlDiag.npy'
orig        = np.array([4., 8.0, 7.0, 5.0, 5.0, 3.5])
bdname = 'SWIRE'
#bound = np.load(SEIP_upper)
bound = np.load(SWIRE_upper)
orig  = np.array([4., 8.0, 7.0, 5.0, 5.0, 3.5])
bound = np.array([orig + bound[i] for i in range(len(bound))])

cat = np.load(argv[1])
bandID = [35, 98, 119, 140, 161, 182]
#cat = np.array([[float(point[i]) for i in bandID] for point in cat])
cat = np.array([list(map(float, point[275].split(','))) for point in cat])
#cat = np.array([orig + cat[i] for i in range(len(cat))])

#---------------------------------------------------------------------------------------#
# Main program

Test = argv[5]
if Test == '3D':
    BD = [] ; YG = []
    b = [0, 1, 2]
    print("Position of "+argv[2]+" data in 3 dimention")
    for i in range(len(cat)) :
        if cat[i][b[0]] != -999. and cat[i][b[1]] != -999. and cat[i][b[2]] != -999. :
            print(cat[i][b[0]], cat[i][b[1]], cat[i][b[2]])
            r, H, vec = calculate([cat[i][b[0]], cat[i][b[1]], cat[i][b[2]]], 3)
            YG.append([r, H, 'non_zero', [cat[i][b[0]], cat[i][b[1]], cat[i][b[2]]], vec])
    print("Calculation of "+argv[2]+" data")
    for p in range(len(YG)) :
        print(YG[p])
        line_BD = []
        Theta = []
        for i in range(len(bound)) :
            test = [bound[i][b[0]], bound[i][b[1]], bound[i][b[2]]]
            r, H, vec = calculate(test, 3)
            BD.append([r, H, vec, test])
        
        for i in range(len(BD)) :
            theta , cri = angle(YG[p][4], BD[i][2], BD[i][0], 3)
            #print(theta, cri)
            if theta < cri :
                #print(theta, cri, BD[i][0], BD[i][1], BD[i][3])
                line_BD.append(BD[i])
                Theta.append(theta)
        #print(line_BD)
        line_BD = np.array(line_BD)
        R = np.array(line_BD[:, 0])
        H = np.array(line_BD[:, 1])
        R_YG = (YG[p][0])
        H_YG = (YG[p][1])
        plt.figure()
        cm = plt.cm.get_cmap('viridis')
        Theta = np.array(Theta)
        c = Theta
        sc = plt.scatter(R, H, c = c, cmap = cm, s = 35, vmin = 0, vmax = 10)
        plt.scatter(R_YG, H_YG, c = 'r', marker = '*', s = 70)
        plt.colorbar(sc)
        plt.savefig(argv[2]+"_RH_3D_test_"+str(p+1)+".png")
    

if Test == 'cat' :
    print("Position of "+argv[2]+" data")

    YG = [] 
    for i in range(len(cat)) :
        orig  = np.array([4., 8.0, 7.0, 5.0, 5.0, 3.5])
        if remove == 'non' :
            point = cat[i]
        else :
            point = np.delete(cat[i], int(remove))
        D = len(point)
        zero = []
        #print(point)
        for j in range(D) :
            if point[j] < -100 or point[j] == 0 :
                zero.append(j)
        print("point : ", point)
        putin = np.delete(point, np.where(point == 0))
        putin = np.delete(putin, np.where(putin == -999))
        print("putin(shift) : ", putin)
        #print(putin)
        #print(putin, D-len(zero))
        print("orig : ", orig)
        orig = np.delete(orig, zero)
        print("orig(project) : ", orig)
        putin = orig + putin
        print("putin(original) : ", putin)
        r, H, vec = calculate(putin, D-len(zero))
        YG.append([r, H, zero, putin, vec])
    for i in range(len(YG)) :
        print("R, H : ", YG[i][0], YG[i][1])
        print("Vec : ", YG[i][4])
        print("putin : ", YG[i][3])
        print()
        #print([r, H, zero, cat[i], vec])
    print()
    
    print("Calculation of "+argv[2]+" data")
    for p in range(len(YG)) :
        BD = []
        line_BD = []
        Theta = []
        for i in range(len(bound)) :
            if D == 6 :
                test = bound[i]
            else :
                test = np.delete(bound[i], int(remove))
            for i in range(len(YG[p][2])) :
                remove = YG[p][2][len(YG[p][2]) - i - 1]
                test = np.delete(test, remove)
            r, H, vec = calculate(test, D-len(YG[p][2]))
            BD.append([r, H, vec, test])
        #print("BD shape : ", np.shape(BD))
        for i in range(len(BD)) :
            theta , cri = angle(YG[p][4], BD[i][2], BD[i][0], D-len(YG[p][2]))
            #print(theta, cri)
            if theta < 1 :
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
        plt.figure()
        cm = plt.cm.get_cmap('viridis')
        Theta = np.array(Theta)
        c = Theta 
        sc = plt.scatter(R, H, c = c, cmap = cm, s = 35, vmin = 0, vmax = 10)
        plt.scatter(R_YG, H_YG, c = 'r', marker = '*', s = 70)
        #plt.colorbar(sc, label = 'Angle (degree)')
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
        plt.plot(R, H, 'o', c = 'b')
        plt.plot(R_YG, H_YG, 'o', c = 'r')
        plt.xlabel('R')
        plt.ylabel('H')
        #plt.show()
        plt.savefig("YY_RH_diagram_"+str(p+1)+".png")
        '''
if Test == "total" :
    print("Position of "+argv[2]+" data")
    print(len(cat))
    obj = []
    for i in range(len(cat)) :
        zero = []
        #print(cat[i], i)
        for j in range(6) :
            if cat[i][j] == -999 :
                zero.append(j)
        #putin = np.delete(cat[i], np.where(cat[i] == 0))
        if len(zero) == 0 :
            print(cat[i])
            r, H, vec = calculate(cat[i], 6-len(zero))
            obj.append([r, H, zero, cat[i], vec])
            print([r, H, zero, cat[i], vec])
    print()
    BD = []
    for i in range(len(bound)) :
        r, H, vec = calculate(bound[i], 6)
        BD.append([r, H, vec])
    
    BD = np.array(BD)
    obj = np.array(obj)
    plt.figure()
    plt.scatter(BD[:,0], BD[:,1], s = 35)
    plt.scatter(obj[:,0], obj[:,1], c = 'r', marker = '*', s = 70)
    n = np.arange(len(obj[:,0]))+1
    for i,txt in enumerate(n):
        plt.annotate(txt,(obj[i,0],obj[i,1]))
    plt.ylim(18, 38)
    plt.xlim(0, 11)
    plt.title("total IY (full bands)")
    plt.xlabel("R (mag)")
    plt.ylabel("H (mag)")
    plt.savefig(argv[3]+"_"+argv[2]+"_RH_diagram_tot.png")

#---------------------------------------------------------------------------------------#
#BD = np.array(BD)
#YG = np.array(YG)
#print(vec_num)
#print(len(re_RH[0]))
#print(re_RH[3])
#vecBD = np.array(re_RH[3])
#BD = np.array(BD)
#YG = np.array(YG)
#R = np.array(BD[:, 0])
#H = np.array(BD[:, 1])
#R_YG = np.array(YG[:, 0])
#H_YG = np.array(YG[:, 1])
#pos_YG = np.array(YG[:, 2])
#for line in YG :
#    print(line)
#plt.plot(R, H, 'o', c = 'b')
#plt.plot(R_YG, H_YG, 'o', c = 'r')
#plt.show()
    '''
    Rtype = [] ; Num = [] ; pos = [] ; Height = []
    for i in range(len(BD)) :
        if BD[i][0] not in Rtype :
            Rtype.append(BD[i][0])
            Num.append(1)
            Height.append([BD[i][1]])
            continue
        for j in range(len(Rtype)) :
            if Rtype[j] == BD[i][0] :
                Num[j] += 1
                Height[j].append(BD[i][1])
    '''


