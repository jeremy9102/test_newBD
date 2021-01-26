#!/home/jeremy/anaconda3/bin/python

import matplotlib
import matplotlib.pyplot as plt
from sys import argv, exit
import numpy as np

if len(argv) != 3 :
    exit("\n\tError : Wrong Argument \
            \n\n\tExample : [program] [Starforming region] [total/obj_type]\
            \n")


def data_process(path, name) :

    cat = open(path+'/' + name + '/{}_6D_diag_BD_GP_out_catalog.tbl'.format(name), 'r')
    new = []
    for line in cat :
        Line = line.split()
        new.append(Line)
    print("\nTotal number of objects in {} : ".format(name), len(new))

    return np.array(new)

name = argv[1]

if argv[2] == 'total' :
    path = "/mazu/users/jordan/YSO_Project/SEIP_GP_Bound/Cloud_Classification_GPM_Diag_BD/6D_bin1.0_sigma2_bond0_refD5/"
    cat = data_process(path, name)
else :
    path = "/home/jeremy/YSO_project/test_newBD/data/results/6D_bin1.0_sigma2_bond0_refD5/Compare_HL/"
    cat = np.load(path + "{0}_{1}.npy".format(name, argv[2]))

his = [0, 0, 0, 0, 0, 0, 0]
band = np.array([a for a in range(7)])
Diag = 271

for point in cat :
    k = int(point[Diag][0])
    his[k] = his[k] + 1

plt.bar(band, his, width = 0.35, align='center' ,color = 'c' ,alpha=0.8)

for a,b in zip(band,his):
    plt.text(a, b, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)

plt.title("histogram of band number ({})".format(name + "_" + argv[2]))
plt.xlabel("Number of effective bands")
plt.ylabel("Number of objects")
#plt.savefig('histogram_of_band_number_{}'.format(name))
plt.show()

