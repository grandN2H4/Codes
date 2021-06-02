import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import copy
import random
import seaborn as sns
from itertools import combinations
from parameter import n

far = 0
frr = 0
flag = 0
# cc = 0
for I in range(1,101):
    for J in range(1,9):
        for I1 in range(I,101):
            left = 1
            if (I1 == I):
                left = J+1
            for J1 in range(left,9):
                # cc += 1
                print(I,J,I1,J1)                
                flag = 0
                cnt=0
                pathr = '../Data/dist-5-gon-translation-quan664/'+str(I)+'_'+str(J)+'and'+str(I1)+'_'+str(J1)+'.txt'
                
                dist = np.loadtxt(pathr)
                length = len(dist)
                print(dist.min())
                for i in range(length):
                    if(dist[i] < 20):
                        # print(dist[i])
                        cnt += 1
                if(cnt > 0):
                    flag = 1                    #判定为同一人
                if((I1 == I) and (flag == 0)):  #FRR
                    # print('frr: ',I,J,I1,J1,dist.min())
                    frr += 1
                if((I1 != I) and (flag == 1)):   #FAR
                    # print('far: ',I,J,I1,J1,dist.min())
                    far += 1
print('FRR: ' + str(frr) + ' ' + str(frr/(7*8*100/2)*100) + '%')
print('FAR: ' + str(far) + ' ' + str(far/((800*799-7*8*100)/2)*100) + '%')
# print('total: ',cc)