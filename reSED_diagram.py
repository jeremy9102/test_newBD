
import numpy as np
import matplotlib.pyplot as plt

path = '/home/jeremy/YSO_project/test_newBD/data/results/6D_bin1.0_sigma2_bond0_refD5/Compare_HL/PER_full_IY.npy'
cat = np.load(path)
band = [1.25, 3.6, 4.5, 5.8, 8.0, 24.0]
orig  = np.array([4., 8.0, 7.0, 5.0, 5.0, 3.5])
flux = [33, 96, 117, 138, 159, 180]
fig, (ax1, ax2) = plt.subplots(1, 2)
test = 'flux'



if test == 'mag' :
    ID = 275
    ylabel = 'magnitude'
    cat = np.array([orig + np.array(map(float, point[ID].split(','))) for point in cat])
    new = []
    for i in range(len(cat)) :
        print(cat[i])
        for j in range(6) :
            if float(cat[i][j]) < 0 :
                break
            if j == 5 :
                new.append(cat[i])
    cat = np.array(new)
    re_cat = np.array([[cat[i][a]/cat[i][0] for a in range(6)] for i in range(len(cat))])

elif test == 'flux' :
    ylabel = 'flux'
    #cat = np.array([list(map(float, point[ID].split(','))) for point in cat])
    cat = np.array([[float(cat[i][a]) for a in flux] for i in range(len(cat))])
    #re_cat = np.array([[cat[i][a]/cat[i][0] for a in range(6)] for i in range(len(cat))])
    re_cat = np.array([[cat[i][a]/np.sum(cat[i]) for a in range(6)] for i in range(len(cat))])
    cat = np.log10(cat)
    re_cat = np.log10(re_cat)

for i in range(len(cat)) :
    ax1.plot(band, cat[i])
    ax2.plot(band, re_cat[i])

name = 'PER'
obj = 'IY'
if obj == 'Ga' :
    objname = 'Galaxy'
else :
    objname = "IYSO"
ax1.set_xlabel('wavelength (micrometer)')
ax1.set_ylabel(ylabel+' [log]')
ax2.set_xlabel('wavelength (micrometer)')
ax2.set_ylabel(ylabel+' [log]')
ax1.set_title("{0} SED ({1})".format(objname, name))
ax2.set_title("{0} relative SED ({1})".format(objname, name))
'''
plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.45, 
                    hspace=0.35)
'''
fig.tight_layout()
plt.savefig("{0}_{1}_HL_same_SED_std_by_sum".format(name, obj))
#plt.show()

