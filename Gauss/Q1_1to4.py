import numpy as np

np.set_printoptions(precision = 6)


def setA(index):
    A = np.zeros(1)

    if index == 1:
        A = np.array([[0.4096, 0.1234, 0.3678, 0.2943],
                     [0.2246, 0.3872, 0.4015, 0.1129],
                     [0.3645, 0.1920, 0.3781, 0.0643],
                     [0.1784, 0.4002, 0.2786, 0.3927]])
    elif index == 2:
        A = np.array([[136.01, 90.86, 0., 0.],
                      [90.86, 98.81, -67.59, 0.],
                      [0., -67.590, 132.01, 46.26],
                      [0., 0., 46.26, 177.17]])
    elif index == 3:
        A = np.array([[1, 1/2, 1/3, 1/4],
                      [1/2, 1/3, 1/4, 1/5],
                      [1/3, 1/4, 1/5, 1/6],
                      [1/4, 1/5, 1/6, 1/7]])
    elif index == 4:
        A = np.array([[10., 7., 8., 7.],
                      [7., 5., 6., 5.],
                      [8., 6., 10., 9.],
                      [7., 5., 9., 10.]])
    return A


def setB(index):
    B = np.zeros(1)

    if index == 1:
        B = np.array([1.1951, 1.1262, 0.9989, 1.2499])
    elif index == 2:
        B = np.array([226.87, 122.08, 110.68, 223.43])
    elif index == 3:
        B = np.array([25/12, 77/60, 57/60, 319/420])
    elif index == 4:
        B = np.array([32., 23., 33., 31.])
    return B


print("问题1")
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

