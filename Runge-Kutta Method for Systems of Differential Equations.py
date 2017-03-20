# du1 / dt = f(t, u1, u2, ... , um)
# du2 / dt = f(t, u1, u2, ... , um)
# ...
# dum / dt = f(t, u1, u2, ... , um) 
# for a <= t <= b with u1 = A1, u2 = A2, ... , um = Am
# Use wij to denote an approximation of ui(tj).
# initial conditon, wi0 = ui(0) = Ai
# k1 = hfi(tj, w1j, w2j, ... , wmj)
# k2 = hfi(tj + h / 2, w1j + k11 / 2, w2j + k12 / 2, ... , wmj + k1m / 2)
# k3 = hfi(tj + h / 2, w1j + k21 / 2, w2j + k22 / 2, ... , wmj + k2m / 2)
# k4 = hfi(tj + h, w1j + k31, w2j + k32, ... , wmj + k3m)
# wij+1 = wij + (k1i + 2k2i + 2k3i + k4i), i = 1, 2, ... , m

# w10  w11  ... 
# w20  w21 
# ... 
# wm0  wm1

def f(j, t, w):
    if j == 0:
        return (-4 * float(w[0]) + 3 * float(w[1]) + 6)
    elif j == 1:
        return (-2.4 * float(w[0]) + 1.6 * float(w[1]) + 3.6)

def Runge_Kutta_for_system(a, b, m, N, A):
    h = (b - a) / N
    t = a
    w = A.copy()
    print(t, w)
    K1 = [0, 0]
    K2 = [0, 0]
    K3 = [0, 0]
    K4 = [0, 0]
    for i in range(1, N + 1):
        for j in range(m):
            K1[j] = h * f(j, t, w)

        w_ = w.copy()
        for l in range(m):
            w_[l] = w_[l] + 0.5 * K1[l]
        for j in range(m):
            K2[j] = h * f(j, t + h / 2, w_)

        w_ = w.copy()
        for l in range(m):
            w_[l] = w_[l] + 0.5 * K2[l]
        for j in range(m):
            K3[j] = h * f(j, t + h / 2, w_)

        w_ = w.copy()
        for l in range(m):
            w_[l] = w_[l] + K3[l]
        for j in range(m):
            K4[j] = h * f(j, t + h, w_)

        for j in range(m):
            w[j] = w[j] + (K1[j] + 2 * K2[j] + 2 * K3[j] + K4[j]) / 6
        t = a + i * h
        print(t, w)

Runge_Kutta_for_system(0, 0.5, 2, 5, [0, 0])