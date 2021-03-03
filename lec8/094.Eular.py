import matplotlib.pyplot as plot
from math import *

def Draw(x, y):
    fig = plot.figure()
    graph = fig.add_subplot()
    plot.plot()
    plot.show()

def f(t, Y):
    return sin(t)

def Eular(T, N, Y):
    dt = T/N; x = []; y = [Y]
    for j in range(N):
        t = j*dt; x += [t]
        Y += dt*f(t, Y); y += [Y]
    x += [T]
    return x, y

# 実行
T = 1; N = 10; Y = 1
x, y = Eular(T, N, Y); Draw(x, y)
print("{0:5d} {1:6.4f} {2:8.6f}".format(N, T/N, y[N]))  #p.97 表5-4