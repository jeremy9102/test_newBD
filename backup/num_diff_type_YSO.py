#! home/jeremy/anaconda3/bin/python

import numpy as np
from sys import argv , exit

cat = np.load('../data/results/CHA_II_6D_multi_BD_GP_obj_type.npy')
cat = cat.tolist()
remove_LESS = []

for point in cat :
    if point[7:] != 'LESS3BD' :
        remove_LESS.append(point)
obj_type = []
YSO = 0
IYSO = 0
Galaxy = 0
Galaxyc = 0
LYSO = 0
IGalaxy = 0
UYSO = 0
other = 0
IUYSO = 0
LUYSO = 0
#print("\nNot YSO or Galaxy\n")
check = True
if check ==True:
    IY = 0 ; UY = 0 ; LY = 0 ; Ga = 0 ; IG = 0 ; oth = 0 
    for obj in remove_LESS :
        print(obj[7:])
        if obj[7:] == "Other" :
            oth += 1
        if obj[7:] == "IGalaxyc" :
            IG += 1
        if obj[7:] == "IYSOc" :
            IY += 1
        if obj[7:] == "UYSOc" :
            UY += 1
        if obj[7:] == "LYSOc" :
            LY += 1
        if obj[7:] == "Galaxyc" :
            Ga += 1
    print("[Galaxy, IGalaxy, IYSO, LYSO, UYSO, Other] = ",[Ga, IG, IY, LY, UY, oth])
    if LY >= 1 : 
        if argv[1] == 'LYSO' : 
            print("[Galaxy, IGalaxy, IYSO, LYSO, UYSO, Other] = ",[Ga, IG, IY, LY, UY, oth])
    if IY + LY + oth  == 6 and Ga + oth != 6:
        #print("[Galaxy, IGalaxy, IYSO, LYSO, UYSO, Other] = ",[Ga, IG, IY, LY, UY, oth])
        YSO += 1
    if IY + oth == 6 :
        if argv[1] == 'IYSO' :
            print("[Galaxy, IGalaxy, IYSO, LYSO, UYSO, Other] = ",[Ga, IG, IY, LY, UY, oth])
        IYSO += 1
    if IY + UY + oth == 6 :
        IUYSO += 1
    if LY + UY + oth == 6 :
        LUYSO += 1
    if LY + oth + Ga == 6 and Ga + oth != 6:
        #print("[Galaxy, IGalaxy, IYSO, LYSO, UYSO, Other] = ",[Ga, IG, IY, LY, UY, oth])
        LYSO += 1
    if UY >= 1 :
        UYSO += 1
    if Ga + IG + UY + oth == 6 :
        Galaxyc += 1
    if Ga + oth == 6 :
        Galaxy += 1
    if IG + oth == 6 :
        IGalaxy += 1
    #if IG >= 1 :
    #    print("[Ga, IG, IY, LY, UY] = ",[Ga, IG, IY, LY, UY])
    #    IGalaxy += 1
    #if [Ga, IY, LY, UY] == [0, 0, 0, 0] :
        #print(line)
print("\nTotal number :\t",len(remove_LESS))
print("YSO(L+I+G+oth):\t",YSO)
print("IYSO :\t\t",IYSO)
#print("IUYSO :\t\t",IUYSO)
#print("LUYSO :\t\t",LUYSO)
print("LYSO :\t\t",LYSO)
print("Galaxy :\t",Galaxyc)
print("UYSO :\t\t",UYSO)
print("IGalaxy : \t", IGalaxy)
print()
