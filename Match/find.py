import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import copy
import random
import seaborn as sns
from itertools import combinations
from parameter import n

same = []
notsame = []
cnt1 = 0
cnt2 = 0
for I in range(1,101):
    for J in range(1,9):
        for I1 in range(I,101):
            left = 1
            if (I1 == I):
                left = J+1
            for J1 in range(left,9):
                # cc += 1
                print(I,J,I1,J1) 
                pathr = '../Data/dist-5-gon-translation-quan443/'+str(I)+'_'+str(J)+'and'+str(I1)+'_'+str(J1)+'.txt'
                # pathr = 'dist-5-gon-translation-quan664/8_2and9_5.txt'
                dist = np.loadtxt(pathr)
                if(I == I1):
                    same.append(dist.min())
                    cnt1 += 1
                else:
                    notsame.append(dist.min())
                    cnt2 += 1
same = np.array(same)
sns.distplot(same)
plt.show()
same = np.array(same)
sns.distplot(notsame)
plt.show()