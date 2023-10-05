import numpy as np

np.set_printoptions(precision = 6)


def setA(index):
    A = np.zeros(1)

    if index == 1:
        A = np.array([[197, 305, -206, -804],
                      [46.8, 71.3, -47.4, 52.],
                      [88.6, 76.4, -10.8, 802],
                      [1.45, 5.9, 6.13, 36.5]])
    elif index == 2:
        A = np.array([[0.5398, 0.7161, -0.5554, -0.2982],
                      [0.5257, 0.6924, 0.3565, -0.6255],
                      [0.6465, -0.8187, -0.1872, 0.1291],
                      [0.5814, 0.9400, -0.7779, -0.4042]])
    elif index == 3:
        A = np.array([[10., 1., 2.],
                      [1., 10., 2.],
                      [1., 1., 5.]])
    elif index == 4:
        A = np.array([[4., -2., -4.],
                      [-2., 17., 10.],
                      [-4., 10., 9.]])
    return A


def setB(index):
    B = np.zeros(1)

    if index == 1:
        B = np.array([136., 11.7, 25.1, 6.6])
    elif index == 2:
        B = np.array([0.2058, -0.0503, 0.1070, 0.1859])
    elif index == 3:
        B = np.array([13., 13., 7.])
    elif index == 4:
        B = np.array([-2., 25., 15.])
    return B


print("问题2")
for index in range(1, 5):
    print("第"+str(index)+"小题的答案为:")

    a = setA(index)
    b = setB(index)
    n = len(a)
    is_strange = False
    m = np.zeros((n, n))
    x = np.zeros(n)

    for k in range(0, n-1):
        _max = 0
        for j in range(k, n):
            _max = max(_max, abs(a[j][k]))

        for p in range(k, n):
            if abs(a[p][k]) == _max:
                break

        if a[p][k] == 0:
            is_strange = True
            break

        elif p != k:
            row_p = a[p].copy()
            row_k = a[k].copy()
            a[p], a[k] = row_k, row_p
            b[p], b[k] = b[k], b[p]

        for i in range(k+1, n):
            if a[k][k] != 0:
                m[i][k] = a[i][k] / a[k][k]
            else:
                is_strange = True
                break

            for j in range(k+1, n):
                a[i][j] -= a[k][j]*m[i][k]

            b[i] -= b[k]*m[i][k]

        if a[n-1][n-1] == 0:
            is_strange = True
            break

    if is_strange:
        print("该线性方程组是奇异的!")

    else:
        x[n-1] = b[n-1] / a[n-1][n-1]

        for k in range(n-2, -1, -1):
            _sum = 0
            for j in range(k+1, n):
                _sum += a[k][j] * x[j]

            x[k] = round((b[k]-_sum) / a[k][k], 6)

        print("方程组的解为:" + str(x))
