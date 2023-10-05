import math
from sympy import *


# 函数
def f(t):
    f = t**2 - 2*t*(math.e**(-t)) + math.e**(-2*t)
    return f


# 函数求导数值
def df(x):
    t = symbols('t')
    f = diff(t**2 - 2*t*(math.e**(-t)) + math.e**(-2*t))
    return f.evalf(subs = {'t':x})


# alpha = math.pi / 4
# N = 10
e1 = pow(10, -6)
e2 = pow(10, -4)


print("问题2第二题")
print("请输入最大迭代次数N:")
N = int(input())

print("请输入初值x0:")
alpha = float(input())


def NewtonDie(e1, e2, N, alpha):
    n = 1
    x0 = alpha

    while n <= N:
        F = f(x0)
        DF = df(x0)
        if abs(F) < e1:
            return x0
            break

        if abs(DF) < e2:
            print("Fail!")
            return 0
            break

        x1 = x0 - F/DF
        Tol = abs(x1 - x0)

        if abs(Tol) < e1:
            return x1
            break

        n = n+1
        x0 = x1

    print("Fail!")
    return 0


res = NewtonDie(e1, e2, N, alpha)
print("牛顿迭代法求得的根为: " + str(round(res, 6)))