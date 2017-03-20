# h = (a - b) / 2
# ∫ f(x) dx (from a to b) ~ (h / 3)(fa + 4fm + fb)
# h = (a - b) / n, n ∈ even
# ∫ f(x) dx ~ (h / 3)(f0 + 4f1 + 2f2 + 4f3 + … + 4fn-1 + fn)
# = (h / 3)[f(a) + 2 sum f(x2i) (from 1 to m – 1) + 4 sum f(x2i-1) (from 1 to m) + f(b)], n = 2m

import math

def f(x):
    return math.sin(x)

def Simpson(a, b):
    n = 10
    h = (b - a) / n
    sum_1 = 0
    sum_2 = 0
    for j in range(1, int((n / 2 - 1) + 1)):
        sum_1 += f(a + 2 * j * h)
    for j in range(1, int((n / 2) + 1)):
        sum_2 += f(a + (2 * j - 1) * h)
    F = (h / 3) * (f(a) + 2 * sum_1 + 4 * sum_2 + f(b))
    print(F)

Simpson(0, 3.14)