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
same = 0
notsame = 0
for I in range(1,101):  #每个人的
    for J in range(8,9):    #第8张 
        for I1 in range(1,101): #与每个人的
            cnt=0
            flag = 0  
            if(I == I1):    #计算自己和自己比的总次数
                same += 1
            else:   #计算自己和别人比的总次数
                notsame += 1
            for J1 in range(1,8):   #第1~7张
                print(I,J,I1,J1)                
                       
                if(I >= I1):    #调整文件名称
                    pathr = '../Data/dist-5-gon-translation-quan664/'+str(I1)+'_'+str(J1)+'and'+str(I)+'_'+str(J)+'.txt'
                else:
                    pathr = '../Data/dist-5-gon-translation-quan664/'+str(I)+'_'+str(J)+'and'+str(I1)+'_'+str(J1)+'.txt'
                # pathr = 'dist-5-gon-translation-quan664/8_2and9_5.txt'
                
                dist = np.loadtxt(pathr)
                length = len(dist)
                # print(dist.min())
                for i in range(length):
                    if(dist[i] < 10):       #dist<30时认为是同一个点
                        # print(dist[i])
                        cnt += 1
            if(cnt > 3):                    #有cnt+1个相同点
                flag = 1                    #判定为同一人
            if((I1 == I) and (flag == 0)):  #FRR
                # print('frr: ',I,J,I1,J1,dist.min())
                frr += 1
            if((I1 != I) and (flag == 1)):   #FAR
                # print('far: ',I,J,I1,J1,dist.min())
                far += 1
print('FRR = ' + str(frr) + '/' + str(same) + ' = ' + str(frr/same*100) + '%')
print('FAR = ' + str(far) + '/' + str(notsame) + ' = ' + str(far/notsame*100) + '%')
# print('total: ',cc)