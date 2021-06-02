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
cc = 0
for I in range(1,101):
    for J in range(1,9):
        #取数据，注意相对路径是相对于当前运行路径
        path1 = '../Data/5-gon-translation-quan/'+str(I)+'_'+str(J)+'.txt'
        data1 = np.loadtxt(path1)
        features1 = copy.deepcopy(data1) 
        num1 = len(features1)
        for I1 in range(I,101):
            left = 1
            if (I1 == I):
                left = J+1
            for J1 in range(left,9):
                cc += 1
                print(I,J,I1,J1)                
                flag = 0 
                path2 = '../Data/5-gon-translation-quan/'+str(I1)+'_'+str(J1)+'.txt'                
                data2 = np.loadtxt(path2)   
                features2 = copy.deepcopy(data2)
                num2 = len(features2)

                dist = np.zeros([num1,num2])
                cnt=0

                pathw = '../Data/dist-5-gon-translation-quan443/'+str(I)+'_'+str(J)+'and'+str(I1)+'_'+str(J1)+'.txt'
                fw = open(pathw,'w')
                for i in range(num1):
                    for j in range(num2):
                        dist[i][j] = np.linalg.norm(features1[i]-features2[j])
                        fw.write(str(dist[i][j]) + '\n')                       
                        if(dist[i][j]<4):
                            cnt += 1
                
                fw.close()
                if(cnt > 2):
                    flag = 1                    #判定为同一人
                if((I1 == I) and (flag == 0)):  #FRR
                    frr += 1
                if((I1 != I) and (flag == 1)):   #FAR
                    # print('far: ',dist.min())
                    far += 1
print('FRR: ' + str(frr) + ' ' + str(frr/(7*8*100/2)*100) + '%')
print('FAR: ' + str(far) + ' ' + str(far/((800*799-7*8*100)/2)*100) + '%')
print('total: ',cc)