#!/home/jeremy/anaconda3/bin/python

from sklearn.neighbors import KDTree
import numpy as np
import pickle
import time
from tqdm import tqdm, trange
from sys import argv , exit
import matplotlib
import matplotlib.pyplot as plt
from sys import argv, exit
import numpy as np
from matplotlib.lines import Line2D


if len(argv) != 3 :
    exit('\n\t Error Argument : \
            \n\t Example : [program] [cat1] [cat2]\
            \n ')

def KDtree(boundary, cat_arr):
    non_zero = []
    non_zero2 = []
    for i in range(len(cat_arr)) : # in order to constrain the lower-5D data
        if np.all(cat_arr[i]) != 0 :
            non_zero2.append(cat_arr[i])
    for j in range(len(boundary)) :
        if np.all(boundary[j]) != 0 :
            non_zero.append(boundary[j])
    print('\n\tCatalog 1 number\t: {}'.format(len(boundary)))
    print('\n\tCatalog 2 number\t: {}'.format(len(cat_arr)))
    print('\n\t6D Full data number(cat1)\t: {}'.format(len(non_zero)))
    print('\n\t6D Full data number(cat2)\t: {}'.format(len(non_zero2)))
    del(cat_arr, boundary)
    cat_arr = np.array(non_zero2)
    boundary = np.array(non_zero)
    if len(cat_arr) == 0 or len(boundary) == 0 :
        return np.array([]), np.array([]), np.array([])
    print('\n\tStart to construct KD tree')
    tStart = time.time()
    time.sleep(2)
    tree = KDTree(boundary, leaf_size=len(boundary)*2/3)
    s = pickle.dumps(tree)
    tree_copy = pickle.loads(s)
    tEnd = time.time()
    #print('\n\tKD tree is finish')
    print("\tIt cost %f sec" % (tEnd - tStart))

    print("\n\tStart to search data")
    tStart = time.time()
    time.sleep(2)
    dist, ind = tree_copy.query(cat_arr, k=len(boundary))
    #print('\n\tFinish to load the data')
    tEnd = time.time()
    print("\tIt cost %f sec" % (tEnd - tStart))
    print('\n\tDist : ', np.shape(dist))
    print('\tInd : ', np.shape(ind))
    return ind, dist

cat1 = np.load(argv[1])
cat2 = np.load(argv[2])
orig  = np.array([4., 8.0, 7.0, 5.0, 5.0, 3.5])
cat1 = np.array([list(map(float, point[275].split(','))) for point in cat1])
cat1 = orig + 1.0 * np.array([cat1[i] for i in range(len(cat1))])

#print('Total catalog : ')
#print()
#for line in cat :
#    print(line)

Ind, Dist = KDtree(cat1, cat2)
Dist = Dist[:, 0].flatten()

fig = plt.figure()
ax = fig.add_subplot(111)
bins = np.linspace(0, 20, num=20)
plt.xlabel('Length (magnitude)')
plt.ylabel('Number')
#plt.title("Two point interval (PER_IY and BD)")
plt.title("Closest neighbor (PER_IY and BD)")
#plt.title(name)
#plt.grid(color='gray', linestyle='--', linewidth=0.5)
ax.hist(Dist, bins=bins, linewidth=1, edgecolor='#EFB28C', color='#EED19C', histtype = 'step', label = 'IY_BD')
#ax.legend('GG')
#ax.hist(cat2, bins=bins, linewidth=1, label = 'GY', histtype = 'step', edgecolor='#4379DC', color='#9CB9EE')
#plt.legend('GY')
#fig.savefig("hist_"+name+'_interval_.png')
Ind, Dist = KDtree(cat1, cat1)
print(Dist)
#Dist = (np.delete(Dist, 0, axis = 1)).flatten()
Dist = Dist[:, 1]
ax.hist(Dist, bins=bins, linewidth=1, color='green', histtype = 'step', label = 'IY_IY')

handles, labels = ax.get_legend_handles_labels()
new_handles = [Line2D([], [], c=h.get_edgecolor()) for h in handles]
ax.legend(handles=new_handles, labels=labels)

#Ind, Dist = KDtree(cat2, cat2)
#Dist = (np.delete(Dist, 0, axis = 1)).flatten()
#ax.hist(Dist, bins=bins, linewidth=1, color='blue', histtype = 'step', label = 'BD_BD')
plt.savefig("closest_PER_IY_BD_reSED.png")
#plt.savefig("interval_PER_IY_BD_reSED.png")
plt.show()

