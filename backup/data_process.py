#!home/jeremy/anaconda3/bin/python

import numpy as np
from sys import argv, exit 

if len(argv) != 2 :
    exit("Error argument : [program] [catalog position]")

#path = "/home/jeremy/test_newBD/data/test_new_projection/"
#cat = open(path+"CHA_II_6D_diag_BD_GP_out_catalog.tbl","r")

def process(path, name) :
    cat = open(path+'/' + name + '/{}_6D_diag_BD_GP_out_catalog.tbl'.format(name), 'r')
    new = []
    
    for line in cat :
        Line = line.split()
        new.append(Line)
    print("Total number of objects in {} : ".format(name), len(new))

    output1 = np.array(new)
    np.save("/home/jeremy/YSO_project/test_newBD/data/results/{0}_6D_multi_BD_GP_out_catalog.npy".format(name), output1)

    #type_pos = [241,245,249,253,257,261]
    type_pos = 235
    #obj = [[new[i][j] for j in type_pos] for i in range(len(new))]

    obj = [new[i][271]for i in range(len(new))]
    for ty in obj :
        print(ty)
    output2 = np.array(obj)
    np.save("/home/jeremy/YSO_project/test_newBD/data/results/{0}_6D_multi_BD_GP_obj_type.npy".format(name), output2)

cloud = ['CHA_II', 'LUP_I', 'LUP_III', 'LUP_IV', 'SER', 'OPH', 'PER']
for cl in cloud :
    print()
    path = argv[1]
    print("Star forming region : {}".format(cl))
    process(argv[1], cl)
    print()

