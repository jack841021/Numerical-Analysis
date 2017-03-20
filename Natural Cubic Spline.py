import math as m

x = [0, 1, 2, 3]
a = [1, m.e, m.e**2, m.e**3]

def spline(x, a):
    n = len(x) - 1
    h = []
    A = []
    l = []
    u = []
    z = []
    c = []
    b = []
    d = []
    for i in range(n + 1):
        h.append('n')
        A.append('n')
        l.append('n')
        u.append('n')
        z.append('n')
        c.append('n')
        b.append('n')
        d.append('n')

    for i in range(n):
        h[i] = x[i + 1] - x[i]
    for i in range(1, n):
        A[i] = 3/h[i]*(a[i + 1] - a[i])-3/h[i-1]*(a[i] - a[i-1])
    l[0] = 1
    u[0] = 0
    z[0] = 0
    for i in range(1, n):
        l[i] = 2*(x[i+1]-x[i-1])-h[i-1]*u[i-1]
        u[i] = h[i]/l[i]
        z[i] = (A[i] - h[i-1]*z[i-1])/l[i]
    l[n] = 1
    z[n] = 0
    c[n] = 0
    for j in range(n - 1, -1, -1):
        c[j] = z[j]-u[j]*c[j+1]
        b[j] = (a[j+1]-a[j])/h[j]-h[j]*(c[j+1]+2*c[j])/3
        d[j] = (c[j+1]-c[j])/(3*h[j])
    print(a)
    print(b)
    print(c)
    print(d)

spline(x, a)