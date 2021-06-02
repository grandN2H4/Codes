import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import copy
import random
import seaborn as sns
from itertools import combinations
from parameter import n

for I in range(1,101):
    for J in range(1,9):
        #取数据，注意相对路径是相对于当前运行路径
        pathr = '../Data/cleanFeatures/'+str(I)+'_'+str(J)+'.txt'
        data = np.loadtxt(pathr)
        num = len(data[:,0])

        #取每个细节点数据记作p[i]
        p = np.zeros([num,3]) 
        for i in range(num):
            p[i]=data[i,:]

        #实验过程中发现有p[i]是重复的，做个去重
        p = np.unique(p, axis=0)
        num = len(p)

        #计算每个点到其它点的欧氏距离（L2范数），并记录在二维矩阵dist[][]中
        dist = np.zeros([num,num])
        for i in range(num-1):
            for j in range(i+1,num):
                dist[i][j] = dist[j][i] = np.linalg.norm(p[i]-p[j])

        #对于每个点，查找并记录离它最近的k个点，由于到本身的距离为0，所以+1
        k = 4+1                                
        index_k = np.zeros([num,k])             #得到距离p[i]最小k个数的索引
        for i in range(num):
            Lst = list(dist[i])                        
            for j in range(k):
                index_j = Lst.index(min(Lst))    #得到列表的最小值，并得到该最小值的索引
                index_k[i][j]=index_j          #记录最小值索引
                Lst[index_j] = float('inf')      #将遍历过的列表最小值改为无穷大，下次不再选择 

        #给index_k去重，减小后面找组合的工作量
        index_k.sort(axis=1)
        index_k = np.unique(index_k, axis=0)
        num = len(index_k)

        #从k+1个点中选择n个点，作为n-gon
        size = 10000
        n_gons = np.zeros([size,n])
        cnt = 0
        for i in range(num):
            test_data = index_k[i]
            for j in combinations(test_data, n):
                t = np.array(j)
                t.sort()                #每个元素都排个序方便等下去重
                n_gons[cnt] = t
                cnt += 1

        #给n-gons去重
        n_gons = np.unique(n_gons, axis=0)
        n_gons = np.delete(n_gons, 0, 0) #删除第一行全零的
        num = len(n_gons)

        #坐标平移
        features = np.zeros([num,3*n])
        for i in range(num):    #对每个n-gon
            n_gon = n_gons[i]
            point = np.zeros([n,3])  #n-gon特征集合
            for t in range(n):    #对n-gon里的每一个点
                point[t] = p[int(n_gon[t])]
                point[t][0:2] -= p[int(n_gon[0])][0:2]
                point[t][1] += 250

                #xxyy……qq
                features[i][t] = point[t][0]
                features[i][n+t] = point[t][1]
                features[i][n*2+t] = point[t][2]

        #生成平移后特征，存进新文件
        pathw = '../Data/5-gon-translation/'+str(I)+'_'+str(J)+'.txt'
        fw = open(pathw,'w')
        for i in range(num): 
            t = str(int(features[i][0]))
            for j in range(1,n*3):
                t += (' ' + str(int(features[i][j])))
            fw.write(t + '\n')