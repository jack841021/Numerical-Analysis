# fixed point: x = g(x)
# Transform f(x) into x = g(x), pn = g(pn-1)
# If pn converges to p, then p = lim(pn) = lim[g(pn-1)] = g[lim(pn-1)] = g(p).
# Therefore, p is a solution to x = g(x) and a root of f(x).

def g(x):
    return 0.5 * (10 - x ** 3) ** 0.5

def fixed_point(p):
    n = 0
    p_ = 0
    while n < 1000000000 and (abs(p - p_) > 10**-9):
        p_ = p
        p = g(p)
        n = n + 1
    print(p, n)

fixed_point(1.5)