# Pn(x) = a0 + a1(x – x0) + a2(x – x0)(x – x1) + ... + an(x – x0)...(x – xn–i) where a0 ~ an are constant
# a0 = Pn(x0) = f0
# f0 + a1(x - x0) = Pn(x1) = f1
# a1 = (f1 - f0) / (x1 - x0) = f01
# a2 = (f12 - f01) / (x2 - x0) = f012
# ak = (f1...k - f0...k-1) / (xk - x0) = f0...k
# Pn(x) = f0 + sigma[f0...k (x - x0) ... (x - xk-1)] from 1 to n

# x0 f0 f01 f012 f0123
# x1 f1 f12 f123
# x2 f2 f23
# x3 f3

import numpy

x = [[1.0, 1.3, 1.6, 1.9, 2.2], [0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623]]

n = len(x[0])

def matrix_creator(x, n):
    matrix = numpy.zeros((n, n + 1))
    for j in range(2):
        for i in range(n):
            matrix[i][j] = x[j][i]
    return matrix

def divided_difference(x, n):
    matrix = matrix_creator(x, n)
    for j in range(2, n + 1):
        for i in range(n + 1 - j):
            matrix[i][j] = (matrix[i + 1][j - 1] - matrix[i][j - 1]) / (matrix[i + j - 1][0] - matrix[i][0])
    return matrix

# print(numpy.array(divided_difference(x, n)))

print(0.03330556345)