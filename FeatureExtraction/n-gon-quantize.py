import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import copy
import random
import seaborn as sns
from itertools import combinations
from parameter import n

#取数据，注意相对路径是相对于当前运行路径
data = np.loadtxt('../Data/5-gon-translation.txt')

# 取x维的数据，注意要深拷贝
x = copy.deepcopy(data[:,:n]) 
# x = copy.deepcopy(data[:,[0,3,6,9,12]])
x = x.flatten()
x.sort()
sns.distplot(x)
plt.show()
# 取y维的数据，并排序，注意要深拷贝
y = copy.deepcopy(data[:,n:n*2]) 
# y = copy.deepcopy(data[:,[1,4,7,10,13]]) 
y = y.flatten()
y.sort()
sns.distplot(y)
plt.show()
# 取q维的数据，并排序，注意要深拷贝
q = copy.deepcopy(data[:,n*2:n*3]) 
# q = copy.deepcopy(data[:,[2,5,8,11,14]]) 
q = q.flatten()
q.sort()
sns.distplot(q)
plt.show()
length = len(x)

#bin的数量
bin1 = 2**4 #分成bin份
bin2 = 2**4 
bin3 = 2**3
num1 = length // bin1 + 1 #每份有num个
num2 = length // bin2 + 1
num3 = length // bin3 + 1
# print(num1,num2)

def quan(feature,tag):
    if(tag == 0):            
        for j in range(bin1):
            if((j == bin1-1) or (feature < x[(j+1)*num1])):
                return j
    elif(tag == 1):
        for j in range(bin2):
            if((j == bin2-1) or (feature < y[(j+1)*num2])):
                return j        
    elif(tag == 2):
        for j in range(bin3):
            if((j == bin3-1) or (feature < q[(j+1)*num3])):
                return j

for I in range(1,101):
    for J in range(1,9):
        print(I,J)
        pathr = '../Data/5-gon-translation/'+str(I)+'_'+str(J)+'.txt'
        pathw = '../Data/5-gon-translation-quan/'+str(I)+'_'+str(J)+'.txt'
        fw = open(pathw,'w')
        data = np.loadtxt(pathr)
        features = copy.deepcopy(data)
        num = len(features)
        for i in range(num):
            sstr = ''
            for j in range(n*3):
                features[i][j] = quan(features[i][j], j//n)
                # features[i][j] = quan(features[i][j], j%3)
                sstr += str(features[i][j])+' '
            fw.write(sstr + '\n')
        fw.close()
        
            
       

                
                