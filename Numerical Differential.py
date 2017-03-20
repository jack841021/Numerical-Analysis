# Expand f(x) at xi: f(x) = f(xi) + (x – xi)f'(xi) + (x – xi)^2 f''(ç)​ / 2 (Taylor series)
# xi+1 = xi + h
# f(xi+1) = f(xi) + hf'(xi) + h^2 / 2f''(ç)
# f'i = (fi+1 - fi) / h (forward)
# f'i = (fi - fi-1) / h (backward)
# f'i = (fi+1 – fi-1) / 2h (central)
# f'i = (-fi+2 + 4fi+1 -3fi) / 2h (three-point forward)
# (-25fi + 48fi+1 – 36fi+2 + 16fi+3 – 3fi+4) / 12h (five-point forward)

h = 10 ** -6

def f(x):
    return x * 2.718282 ** x

def true(x):
    return (2.718282 ** x) + x * (2.718282 ** x)

def two_point(x):
    f_ = (f(x + h) - f(x))/h
    return f_, f_ - true(x)

def three_point_end(x):
    f_ = 1 / (2 * h) * ((-3) * f(x) + 4 * f(x + h) - f(x + 2 * h))
    return f_, f_ - true(x)

def three_point_mid(x):
    f_ = 1 / (2 * h) * (f(x + h) - f(x - h))
    return f_, f_ - true(x)

def five_point_end(x):
    f_ = 1 / (12 * h) * ((-25) * f(x) + 48 * f(x + h) - 36 * f(x + 2 * h) + 16 * f(x + 3 * h) - 3 * f(x + 4 * h))
    return f_, f_ - true(x)

def five_point_mid(x):
    f_ = 1 / (12 * h) * (f(x - 2 * h) - 8 * f(x - h) + 8 * f(x + h) - f(x + 2 * h))
    return f_, f_ - true(x)

print(      two_point(2))
print(three_point_end(2))
print(three_point_mid(2))
print( five_point_end(2))
print( five_point_mid(2))