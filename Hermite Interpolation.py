# p: oculating approximation of f
# d^k p(xi) / dx^k = d^k f(xi) / dx^k where k = 0 ~ m and i = 0 ~ n
# When n = 0, p = Taylor at x0
# When k = 0, p = Lagrange of x0 ~ xn
# When k = 1, p = Hermite of x0 ~ xn

# z0 = x0  f(x0) = f0  f01 = f'(x0)  f012  f0123
# z1 = x0  f(x0) = f1  f12           f123
# z2 = x1  f(x1) = f2  f23 = f'(x2)
# z3 = x1  f(x1) = f3
# f0...k = (f1...k - f0...k-1) / (xk - x0)

import numpy

x = [[1.3, 1.6, 1.9],
     [0.6200860, 0.4554022, 0.2818186],
     [-0.5220232, -0.5698959, -0.5811571]]

n = len(x)

def matrix_creator(x, n):
    matrix = numpy.zeros((n * 2, 3 + 2 * n - 2))
    for j in range(n):
        for i in range(n):
            matrix[2 * i    ][j] = x[j][i]
            matrix[2 * i + 1][j] = x[j][i]
    for i in range(n - 1):
        matrix[2 * i + 1][2] = (matrix[2 * i + 2][1] - matrix[2 * i + 1][1]) / (matrix[2 * i + 2][0] - matrix[2 * i + 1][0])
    matrix[2 * n - 1][2] = 0
    return matrix

def hermite(x, n):
    matrix = matrix_creator(x, n)
    for j in range(3, 3 + n + 1):
        for i in range(3 + n + 1 - j):
            matrix[i][j] = (matrix[i + 1][j - 1] - matrix[i][j - 1]) / (matrix[i + j - 1][0] - matrix[i][0])
    return matrix

print(numpy.array(hermite(x, n)))