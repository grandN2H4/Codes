import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import copy
import random
import seaborn as sns
from itertools import combinations
from parameter import n

#用n-gon做特征生成，存进新文件
for I in range(1,101):
    for J in range(1,9):
        pathr = '../Data/5-gon-translation-quan/'+str(I)+'_'+str(J)+'.txt'
        data = np.loadtxt(pathr)
        features = copy.deepcopy(data)
        num = len(data)
        pathw = '../Data/feature443/'+str(I)+'_'+str(J)+'.txt'
        fw = open(pathw,'w')
        for i in range(num):
            feature = ''
            # print(features[i])
            for j in range(n*2):
                feature += '{:04b}'.format(int(features[i][j]))
            for j in range(n*2,n*3):
                feature += '{:03b}'.format(int(features[i][j]))
            # print(feature)
            # print(int(feature,2)) 
            fw.write(str(int(feature,2))+'\n')