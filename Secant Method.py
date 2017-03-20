# Replace derivative by backward-difference approximation.
# f'(pn-1) = f(pn-1) – f(pn–2) / (pn-1 – pn–2)
# pn = pn-1 - f(pn-1) / f'(pn-1) = pn-1 - f(pn-1) * (pn-1 – pn–2) / [f(pn-1) – f(pn–2)]

import math

def f(x):
    return math.cos(x) - x

def secant(p, _p):
    n = 0
    e = 1
    while n < 10 ** 9 and e > 10 ** -9:
        p_ = p - f(p) * (p - _p) / (f(p) - f(_p))
        e = abs(p_ - p)
        p, _p = p_, p
        n = n + 1
    print(math.cos(p) - p)

secant(0.5, math.pi/4)