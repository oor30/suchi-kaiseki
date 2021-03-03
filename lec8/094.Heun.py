def Heun(T, N, Y):
    dt = T/N; x = []; y = [Y]
    for j in range(N):
        t = j*dt; x += [t]
        k1 = f(t, Y)
        k2 = f(t+dt, Y+dt*k1)
        Y += dt/2*(k1+k2); y += [Y]
    x += [T]
    return x, y

# 実行
T = 1; N = 10; Y = 1
x, y = Heun(T, N, Y); Draw(x, y)
print("{0:5d} {1:6.4f} {2:8.6f}".format(N, T/N, y[N]))  # p.97 表5-4
