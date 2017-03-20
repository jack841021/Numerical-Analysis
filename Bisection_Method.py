def f(x):
    return x**3 + 4*x**2 - 10

def bisection():
    a = 1000000000
    b = -1000000000
    n = 0
    while n < 1000000000 and (abs(a - b) > 10**-9):
        m = (a + b) / 2
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
        n = n + 1
    print((a + b) / 2, n)

bisection()