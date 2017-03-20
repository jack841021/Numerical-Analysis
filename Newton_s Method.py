# p_ is a root of f(x). Let p be an approximation to p_ and f'(p) != 0.
# Expand f(x) at p: f(x) = f(p) + (x – p)f'(p) + (x – p)^2 f''(ç) / 2​ (Taylor series)
# f(p_) = 0 ~ f(p) + (p_ – p)f'(p) [(p_ – p)^2 is ignored.]
# p_ ~ p - f(p) / f'(p)
# pn = pn-1 - f(pn-1) / f'(pn-1)

import math

def f(x):
    return math.cos(x) - x

def f_(p):
    return - math.sin(x) - 1

def newton(p):
    n, e = 0, 1 # e: error
    while n < 10 ** 9 and e > 10**-9:
        p_ = p - f(p) / f_(p)
        e = abs(p_ - p)
        p = p_
        n = n + 1
    print(p, n)

newton(0.5)