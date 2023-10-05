import math
import numpy as np
from numpy import *
from sympy import true

e = 10e-6
res = 0

def setA(index):
    if index == 1:
        a = 0
    if index == 2:
        a = 1
    if index == 3:
        a = 0
    if index == 4:
        a = 0
    return a


def setB(index):
    if index == 1:
        b = 1
    if index == 2:
        b = 3
    if index == 3:
        b = 1
    if index == 4:
        b = 1
    return b


def f(x, index):     # 待积分的函数
    if index == 1:
        f = (x ** 2) * (math.e ** x)
    if index == 2:
        f = math.exp(x) * math.sin(x)
    if index == 3:
        f = 4 / (1 + x ** 2)
    if index == 4:
        f = 1 / (x + 1)
    return f


def setH(index):
    h = setB(index) - setA(index)
    return h


for index in range(1, 5):
    a = setA(index)
    b = setB(index)
    h = setH(index)
    i = 1
    err = 10e-6
    T = np.zeros((6, 6))

    print("\n问题1第"+str(index)+"题答案为:")

    T[0][0] = h * (f(a, index) + f(b, index)) / 2

    while true:
        ii = 2 ** (i-1)
        T[0][i] = T[0][i-1] / 2

        for k in range(1, ii+1):
            T[0][i] += h * f(a + (k-1/2)*h, index) / 2

        for m in range(1, i+1):
            k = i - m
            T[m][k] = ((4 ** m)*T[m-1][k+1] - T[m-1][k]) / ((4 ** m) - 1)

        if abs(T[i][0] - T[i-1][0]) < err:
            res = T[i][0]

            for j in range(i + 1):
                print(T[j])
            break

        h /= 2
        i += 1

    print("由Romberg积分法得出的结果为:" + str(round(res, 8)))