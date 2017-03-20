# x0   x1   x2
# p0   p1   p2
# p01  p12
# p012

# p01 = [(a - x1)p0 - (a - x0)p1] / (x0 - x1)

x = [1.0, 1.3, 1.6, 1.9, 2.2]
y = [0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623]

def neville(x, y, a):
    n = len(x)
    p = y
    for i in range(1, n):
        for j in range(n - i):
            p[j] = ((a - x[j+i]) * p[j] - (a - x[j]) * p[j+1]) / (x[j] - x[j+i])
    print(p[0])

neville(x, y, 1.5)