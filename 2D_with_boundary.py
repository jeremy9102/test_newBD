#!/home/jeremy/anaconda3/bin/python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from sys import argv, exit
from matplotlib.lines import Line2D

if len(argv) != 3 :
    exit('\n\tError: Wrong Arguments\
            \n\tExample: [program] [total/one][input data] \
            \n')

def process_table(path) :
    output  = []
    table   = open(path, 'r').readlines()
    for line in table :
        output.append([float(line.split()[a]) for a in [35, 98, 119, 140, 161, 182]])
    output  = np.array(output)
    return output

path_lower_SWIRE    = '/mazu/users/jordan/YSO_Project/SWIRE_GP_Bound/GPV_after_smooth_6D_bin1.0_sigma2_bond0_refD5/after_smooth_lack_0_012345_6D_lower_bounds_AlDiag.npy'
path_upper_SWIRE    = '/mazu/users/jordan/YSO_Project/SWIRE_GP_Bound/GPV_after_smooth_6D_bin1.0_sigma2_bond0_refD5/after_smooth_lack_0_012345_6D_upper_bounds_AlDiag.npy'
path_upper = '/mazu/users/jordan/YSO_Project/SEIP_GP_Bound/test/GPV_after_smooth_6D_bin1.0_sigma2_bond0_refD5/after_smooth_lack_0_012345_6D_upper_bounds_AlDiag.npy'
path_lower = '/mazu/users/jordan/YSO_Project/SEIP_GP_Bound/test/GPV_after_smooth_6D_bin1.0_sigma2_bond0_refD5/after_smooth_lack_0_012345_6D_lower_bounds_AlDiag.npy'

bound_SWIRE = np.r_[np.load(path_lower_SWIRE), np.load(path_upper_SWIRE)]
bound       = np.r_[np.load(path_lower), np.load(path_upper)]
orig        = np.array([4., 8.0, 7.0, 5.0, 5.0, 3.5])
bound_SWIRE  = orig + 1.0 * np.array([bound_SWIRE[i] for i in range(len(bound_SWIRE))])
bound = orig + 1.0 * np.array([bound[i] for i in range(len(bound))])

bandID = [35, 98, 119, 140, 161, 182]

LY = np.load('/home/jeremy/test_newBD/data/LYSO_CHA_II.npy').astype(np.float64)[:3][:]
UY = np.load('/home/jeremy/test_newBD/data/UYSO_CHA_II.npy').astype(np.float64)
Ga = np.load('/home/jeremy/test_newBD/data/Ga_CHA_II.npy').astype(np.float64)
IG = np.load('/home/jeremy/test_newBD/data/IG_CHA_II.npy').astype(np.float64)
cat = np.load(argv[2])
cat = np.array([[float(point[i]) for i in bandID] for point in cat])
band = ['J', 'IR1', 'IR2', 'IR4', 'MP1', 'MP2']


if argv[1] == 'one' :
    fig, ax = plt.subplots(1, 1)
        
    b1 = 1
    b2 = 2
    SEIP = [a for a in range(15)]
    SWIRE = [a for a in range(15)]
    data = [a for a in range(15)]
    LYplot = [a for a in range(15)]
    
    data = ax.plot(bound[:, b1], bound[:, b2], 'b+', markersize = 12)
    SWIRE = ax.plot(bound_SWIRE[:, b1], bound_SWIRE[:, b2], 'go', markersize = 12, fillstyle = Line2D.fillStyles[-1], alpha = 0.8)
    plot = ax.plot(cat[:, b1], cat[:, b2], 'ro')
    ax.set_xlabel(band[b1])
    ax.set_ylabel(band[b2])
    #ax.set_xlim(6, 20)
    #ax.set_ylim(0, 20)
    
    xmajorLocator  = MultipleLocator(1) #將x主刻度標籤設定為20的倍數
    xmajorFormatter = FormatStrFormatter('%1.1f') #設定x軸標籤文字的格式
    xminorLocator  = MultipleLocator(5) #將x軸次刻度標籤設定為5的倍數
    ymajorLocator  = MultipleLocator(1) #將y軸主刻度標籤設定為0.5的倍數
    ymajorFormatter = FormatStrFormatter('%1.1f') #設定y軸標籤文字的格式
    yminorLocator  = MultipleLocator(0.1)
    
    ax.xaxis.set_major_locator(xmajorLocator)
    ax.xaxis.set_major_formatter(xmajorFormatter)
    ax.yaxis.set_major_locator(ymajorLocator)
    ax.yaxis.set_major_formatter(ymajorFormatter)
    ax.legend([data[0], SWIRE[0], plot[0]], ['SEIP', 'SWIRE', 'GY']) 
    plt.show()

if argv[1] == "total" :
    fig, axes = plt.subplots(5, 3)
    b1 = 0
    b2 = 1
    k = 0
    SEIP = [a for a in range(15)]
    SWIRE = [a for a in range(15)]
    data = [a for a in range(15)]
    plot = [a for a in range(15)]
    for i in range(3) :
        for j in range(5) :
            if b2 > 5 :
                b1 += 1
                b2 = b1 +1
    
            SWIRE[k], = axes[j, i].plot(bound_SWIRE[:, b1], bound_SWIRE[:, b2], 'go', markersize = 8, fillstyle = Line2D.fillStyles[-1], alpha = 0.8)
            #data[k], = axes[j, i].plot(bound[:, b1], bound[:, b2], 'b+', markersize = 5)
            #axes[j, i].set_xlabel(band[b1])
            #axes[j, i].set_ylabel(band[b2])
            axes[j, i].set_xlim(4, 20)
            axes[j, i].set_ylim(4, 20)
            #plt.savefig('boundary_diff_'+band[b1]+'_'+band[b2])
            #axes[j, i].legend([SEIP[k], SWIRE[k]], ['SEIP', 'SWIRE'])
            plot[k], = axes[j, i].plot(cat[:, b1], cat[:, b2], 'ro')
            axes[j, i].set(xlabel = band[b1], ylabel = band[b2])
    
            xmajorLocator  = MultipleLocator(4)
            xmajorFormatter = FormatStrFormatter('%1.0f')
            axes[j, i].xaxis.set_major_locator(xmajorLocator)
            axes[j, i].xaxis.set_major_formatter(xmajorFormatter)
            ymajorLocator  = MultipleLocator(4)
            ymajorFormatter = FormatStrFormatter('%1.0f')
            axes[j, i].yaxis.set_major_locator(ymajorLocator)
            axes[j, i].yaxis.set_major_formatter(ymajorFormatter)
            k+=1
            b2 += 1
    
    #axes[0, 0].legend([data[0], SWIRE[0], plot[0]], ['SEIP', 'SWIRE', 'GY'])
    plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.2, hspace=0.7)
    #plt.tight_layout()
    plt.show()

