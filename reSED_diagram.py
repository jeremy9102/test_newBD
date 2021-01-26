
import numpy as np
import matplotlib.pyplot as plt

path = '/home/jeremy/YSO_project/test_newBD/data/results/6D_bin1.0_sigma2_bond0_refD5/Compare_HL/PER_Ga_HL_same.npy'
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
    ylabel = 'flux (log)'
    #cat = np.array([list(map(float, point[ID].split(','))) for point in cat])
    cat = np.array([[float(cat[i][a]) for a in flux] for i in range(len(cat))])
    re_cat = np.array([[cat[i][a]/cat[i][0] for a in range(6)] for i in range(len(cat))])
    #cat = np.array([[cat[i][a]/np.sum(cat[i]) for a in range(6)] for i in range(len(cat))])
    cat = np.log(cat)
    re_cat = np.log(re_cat)

for i in range(len(cat)) :
    ax1.plot(band, cat[i])
    ax2.plot(band, re_cat[i])

ax1.set_xlabel('wavelength (micrometer)')
ax1.set_ylabel(ylabel)
ax2.set_xlabel('wavelength (micrometer)')
ax2.set_ylabel(ylabel)
ax1.set_title("IY_SED")
ax2.set_title("IY_reSED")
plt.show()

