#! home/jeremy/anaconda3/bin/python

import numpy as np
from sys import argv , exit

if len(argv) != 3 :
    exit("Error argument : [program] [path of results] [Starforming region]")

def data_process(path, name) :
    
    cat = open(path+'/' + name + '/{}_6D_diag_BD_GP_out_catalog.tbl'.format(name), 'r')
    new = []
    for line in cat :
        Line = line.split()
        new.append(Line)
    print("\nTotal number of objects in {} : ".format(name), len(new))

    return np.array(new)

def HL_compare_obj(objtype, cat) :

    same = [] ; diff = []
    for point in objtype :
        ra = list(cat[:, 0])
        dec = list(cat[:, 1])
        if float(point[0]) in ra and float(point[2]) in dec :
            same.append(point)
        else :
            diff.append(point)
    
    return same, diff

#----------------------------------------------------------------------------------------#
name = argv[2]
cat = data_process(argv[1], name)
remove_LESS = []
DiagID = 271
for point in cat :
#    print(point[271])
    if point[DiagID][7:] != 'LESS3BD' :
        #print(point[DiagID][7:])
        remove_LESS.append(point)

UY = [] ; LY = [] ; IG = [] ; IY = [] ; AGB = [] ; Ga = []
FUY = [] ; FLY = [] ; FIG = [] ; FIY = [] ; FAGB = [] ; FGa = []
other = []
sixband = [0, 0, 0, 0, 0, 0]
for point in remove_LESS :
    if point[DiagID][7:] == 'UYSOc' :
        UY.append(point)
        if point[DiagID][0] == '6' :
            FUY.append(point)
    elif point[DiagID][7:] == 'LYSOc' :
        LY.append(point)
        if point[DiagID][0] == '6' :
            FLY.append(point)
    elif point[DiagID][7:] == 'IGalaxyc' :
        IG.append(point)
        if point[DiagID][0] == '6' :
            FIG.append(point)
    elif point[DiagID][7:] == 'Galaxyc' :
        Ga.append(point)
        if point[DiagID][0] == '6' :
            FGa.append(point)
    elif point[DiagID][7:] == 'AGB' :
        AGB.append(point)
        if point[DiagID][0] == '6' :
            FAGB.append(point)
    elif point[DiagID][7:] == 'IYSOc' :
        IY.append(point)
        if point[DiagID][0] == '6' :
            FIY.append(point)
    else : 
        other.append(point)
        print(point[DiagID][7:])
print()
print("Classification\n")
print('[Ga, IG, \033[93mIY\033[0m, \033[95mLY\033[0m, UY, AGB, other] = [{0}, {1}, \033[93m{2}\033[0m, \033[95m{3}\033[0m, {4}, {5}, {6}]'\
        .format(len(Ga), len(IG), len(IY), len(LY), len(UY), len(AGB), len(other)), '\n')

print('Full six bands data : \t[Ga, IG, IY, LY, UY, AGB] =',[len(FGa), len(FIG), len(FIY), len(FLY), len(FUY), len(FAGB)], '\n')
np.save('/home/jeremy/YSO_project/test_newBD/data/results/6D_bin1.0_sigma2_bond0_refD5/Compare_HL/{}_full_IY.npy'.format(name), FIY)
band = [35, 98, 119, 140, 161, 182]
#print([LY[0][i] for i in band])
#np.save('LYSO_CHA_II.npy', [[line[i] for i in band] for line in LY])
#np.save('UYSO_CHA_II.npy', [[line[i] for i in band] for line in UY])
#np.save('Ga_CHA_II.npy', [[line[i] for i in band] for line in Ga])
#np.save('IG_CHA_II.npy', [[line[i] for i in band] for line in IG])
total = [np.array(Ga), np.array(IG), np.array(IY), np.array(LY), np.array(UY), np.array(AGB)]

HL_path = '/mazu/users/jordan/YSO_Project/YSO_Hunters_Table/All_Table_To_Compare/Table_From_Hsieh/HL_YSOs_2013/'
filename = 'HL_YSOs_{}_coord.dat'.format(name)

HL = np.loadtxt(HL_path+filename).astype(np.float64)

BD_HL, BD_HL_diff = HL_compare_obj(remove_LESS, HL)
LY_HL, LY_HL_diff = HL_compare_obj(LY, HL)
UY_HL_diff , UY_HL = HL_compare_obj(UY, HL)
Ga_HL_diff , Ga_HL = HL_compare_obj(Ga, HL)
IY_HL, IY_HL_diff = HL_compare_obj(IY, HL)
IG_HL_diff, IG_HL = HL_compare_obj(IG, HL)

print("Compare to Stanley\n")

print("[tot_HL,BD_HL,\033[95mLY_HL\033[0m,UY_HL,Ga_HL,\033[93mIY_HL\033[0m,IG_HL] = [{0}, {1},\033[95m {2}\033[0m, {3}, {4}, \033[93m{5}\033[0m, {6}]"\
        .format(len(HL),len(BD_HL),len(LY_HL),len(UY_HL),len(Ga_HL),len(IY_HL),len(IG_HL)), '\n')
print("[tot_HL,BD_HL_diff,\033[95mLY_HL_diff\033[0m,UY_HL_diff,Ga_HL_diff,\033[93mIY_HL_diff\033[0m,IG_HL_diff] = [{0}, {1},\033[95m {2}\033[0m, {3}, {4}, \033[93m{5}\033[0m, {6}]"\
        .format(len(HL),len(BD_HL_diff),len(LY_HL_diff),len(UY_HL_diff),len(Ga_HL_diff),len(IY_HL_diff),len(IG_HL_diff)), '\n')
print("{}\t|YSO\t|Galaxy\t".format(name))
print("--------|-------|-------")
print("YSO\t|{0}\t|{1}".format(len(LY_HL)+len(IY_HL), len(UY_HL_diff)+len(IG_HL_diff)+len(Ga_HL_diff)))
print("NotYSO\t|{0}\t|{1}".format(len(LY_HL_diff)+len(IY_HL_diff), len(UY_HL)+len(IG_HL)+len(Ga_HL)))
print()
np.save('/home/jeremy/YSO_project/test_newBD/data/results/6D_bin1.0_sigma2_bond0_refD5/Compare_HL/{}_IY_HL_diff.npy'.format(name), IY_HL_diff)
np.save('/home/jeremy/YSO_project/test_newBD/data/results/6D_bin1.0_sigma2_bond0_refD5/Compare_HL/{}_LY_HL_diff.npy'.format(name), LY_HL_diff)
np.save('/home/jeremy/YSO_project/test_newBD/data/results/6D_bin1.0_sigma2_bond0_refD5/Compare_HL/{}_LY_HL_same.npy'.format(name), LY_HL)
np.save('/home/jeremy/YSO_project/test_newBD/data/results/6D_bin1.0_sigma2_bond0_refD5/Compare_HL/{}_Ga_HL_same.npy'.format(name), Ga_HL)
np.save('/home/jeremy/YSO_project/test_newBD/data/results/6D_bin1.0_sigma2_bond0_refD5/Compare_HL/{}_IY_HL_same.npy'.format(name), IY_HL)
for point in LY_HL_diff :
    print(point[DiagID][7:])
