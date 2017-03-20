import numpy

matrix = numpy.array([[  1, -1,  2, -1, -8],
                      [  2, -2,  3, -3,-20],
                      [  1,  1,  1,  0, -2],
                      [  1, -1,  4,  3,  4]])

def Gaussian_elimination(matrix):
    i = 0
    j = 0
    l = len(matrix)
    indicator = [0, 0, 0, 0]
    while 0 in indicator:
        if matrix[i][j] != 0 and indicator[i] == 0:
            for i_ in range(l):
                if i_ != i:
                    a = matrix[i_][j] / matrix[i][j]
                    matrix[i_] = matrix[i_] - a * matrix[i]
            indicator[i] = 1
            i = (i + 1) % l
            j += 1
        else:
            i += 1
    return matrix

print(Gaussian_elimination(matrix))