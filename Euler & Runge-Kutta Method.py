# y' = f(y, t), y(t0) = y0
# forward-difference approximation: y'i = (yi+1 – yi) / h
# h = (tn – t0) / n
# yi+1 = yi + hf(yi, ti)

# Second order Runge-Kutte Method
# dy / dt = f(y, t)
# ∫ dy = ∫ f(y, t) dt, from yi to yi+1
# yi+1 = yi + ∫ f(y, t) dt
# yi+1 = yi + (h / 2)(f(yi, ti) + f(yi+1, ti+1)) (Trapezoidal)
# yi+1 = yi + (h / 2)(f(yi, ti) + f(yi + hf(yi, ti), ti+1)) (Euler)
# yi+1 = yi + (1 / 2)(k1 + k2)
# k1 = hf(yi, ti)
# k2 = hf(yi + k1, ti+1)

# Fourth order Runge-Kutte Method
# yi+1 = yi + (1 / 6)(k1 + 2k2 + 2k3 + k4)
# k1 = hf(yi, ti)
# k2 = hf(yi + k1 / 2, ti + h / 2)
# k3 = hf(yi + k2 / 2, ti + h / 2)
# k4 = hf(yi + k3, ti + h)

def f(t, y):
    return y - t**2 + 1

def Euler(a, b, N, A):
    h = (b - a) / N
    t = a
    w = A
    print(t, w)
    for i in range(1, N + 1):
        w = w + h * f(t, w)
        t = a + i * h
        print(t, w)

Euler(0, 2, 10, 0.5)

print('----------------------------------------')

def Runge_Kutta(a, b, N, A):
    h = (b - a) / N
    t = a
    w = A
    print(t, w)
    for i in range(1, N + 1):
        K1 = h * f(t, w)
        K2 = h * f(t + h/2, w + K1/2)
        K3 = h * f(t + h/2, w + K2/2)
        K4 = h * f(t + h, w + K3)
        w = w + (K1 + 2 * K2 + 2 * K3 + K4) / 6
        t = a + i * h
        print(t, w)

Runge_Kutta(0, 2, 10, 0.5)
