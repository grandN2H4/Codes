import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import copy

#取数据，注意相对路径是相对于当前运行路径
data = np.loadtxt('../Data/feature664.txt')

# # 取x维的数据，注意要深拷贝
# x = copy.deepcopy(data[:,:5]) 
# x = x.flatten()
# x.sort()

# # 取y维的数据，并排序，注意要深拷贝
# y = copy.deepcopy(data[:,5:10]) 
# y = y.flatten()
# y.sort()

# # 取q维的数据，并排序，注意要深拷贝
# q = copy.deepcopy(data[:,10:15]) 
# q = q.flatten()
# q.sort()

sns.distplot(data)
plt.show()

# sns.distplot(x, hist=False)
# plt.show()