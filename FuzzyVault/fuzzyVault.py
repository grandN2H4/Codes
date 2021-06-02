import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import copy
import random
import seaborn as sns
from itertools import combinations
from parameter import n
from decimal import Decimal
from decimal import getcontext

work_context = getcontext()
work_context.prec = 58

#生成128位待保护的密钥
s = random.getrandbits(128)
#生成64位hash值
ss = '{:0128b}'.format(s) + '{:064b}'.format(hash(s))
#密钥和hash值连起来
c = int(ss,2)

#多项式：y=ax^2+bx+c
a = random.getrandbits(192)
b = random.getrandbits(192)

T = [1,2,3,4,5,6,7,8,9,0]
V = []
F = []
t = len(T)

#生成随机数
for i in range(20):
    alpha = random.getrandbits(80)
    beta = random.getrandbits(192)
    V.append([alpha,beta])

def encode():
    for i in range(t):
        x = T[i]
        y = a*x*x + b*x + c
        V.append([x,y])
        F.append([x,y])

encode()
print(V)

#拉格朗日插值
def p(k,targs):                 # 运用闭包返回p_k(x)
    def rtn_func(x):
        rtn = 1
        for i in targs:         # 累乘
            if i == k: 
                continue   # i!=k
            rtn *= Decimal(x) - Decimal(i[0])
            rtn /= Decimal(k[0]) - Decimal(i[0])
        rtn *= Decimal(k[1])
        return Decimal(rtn)
    return rtn_func

def L(*targs):                  # 运用闭包返回L(x)
    funcs=[p(i,targs) for i in targs]   # 获取p_k(x)
    def rtn_func(x):
        rtn = 0
        for i in funcs:
            rtn += Decimal(i(x))# 执行累加
        return Decimal(rtn)
    return rtn_func

# data=[[1,1],[2,2],[3,2],[4,6],[5,-1],[0,-1]]
func = L(*F)           # 生成插值后的多项式函数
print(Decimal(func(0)))
s_s = int(Decimal(func(0)))
print(c)
print(Decimal(func(0)))
s_b = '{:0192b}'.format(s_s)
sk = int(s_b[0:128],2)
hs = int(s_b[128:192],2)
if(hs == hash(sk)):
    print("Successful！")
else:
    print("Faild！")

# # 画出多项式图像
# x=np.arange(0,5,0.1)    # 范围[0,5)，间隔0.1
# y=[func(i) for i in x]  # 获取值
# plt.title("Lagrange Interpolation Polynomial")
# plt.plot(x,y)
# plt.show()              # 运用matplotlib显示图像