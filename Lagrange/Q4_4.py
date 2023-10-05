import math
import numpy as np
from numpy import *
print("问题4第四题:")

'''
print("请输入区间左右界限(空格隔开):")
a, b = map(int, input().split())
print("请输入想用拉格朗日多项式求近似值的x值:")
xbar = float(input())
'''

n = 3


# 待积函数
def fun(x):
    f = np.sqrt(x)
    return f


xkList = np.array([169., 196., 225.])


def langrange():
    y = 0.

    for k in range(0, n):
        l = 1.

        for j in range(0, n):
            if xkList[k] - xkList[j] == 0:
                continue
            l = l * (xbar - xkList[j]) / (xkList[k] - xkList[j])

        y = y + l * fun(xkList[k])

    return y


print("拉格朗日插值多项式对四个点得到的近似结果为: ")

for index in range(0, 4):
    if index == 0:
        xbar = 5
    elif index == 1:
        xbar = 50
    elif index == 2:
        xbar = 115
    elif index == 3:
        xbar = 185

    print('(' + str(xbar) + ',' + str(round(langrange(), 6)) + ')')
