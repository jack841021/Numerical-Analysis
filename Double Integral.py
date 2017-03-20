print(0.03330556345)




import math

def f(x, y):
    return math.exp(y/x)

def c(x):
    return x**3

def d(x):
    return x**2

def inte(a, b, m, n):
    h = (b - a) / n
    j1 = 0
    j2 = 0
    j3 = 0
    for i in range(n+1):
        x = a + i * h
        HX = (d(x) - c(x)) / m
        k1 = f(x, c(x)) + f(x, d(x))
        k2 = 0
        k3 = 0
        for j in range(m):
            y = c(x) + j * HX
            Q = f(x, y)
            if j % 2 == 0:
                k2 = k2 + Q
            else:
                k3 = k3 + Q
        L = (k1 + 2*k2 + 4*k3) * HX / 3
        if i == 0 or i == n:
            j1 = j1 + L
        elif i % 2 == 0:
            j2 = j2 + L
        else:
            j3 = j3 + L
    j = h*(j1 +2*j2+4*j3)/3
    return j

inte(0.1, 0.5, 10, 10)