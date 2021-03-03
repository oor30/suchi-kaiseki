import matplotlib
import matplotlib.pyplot as plot
from math import *

def f(x):
    return sqrt(1-x**2)

# ちょっと便利な関数
def xi(i, xs, xe, ndiv):
    return xs*(ndiv-i)/ndiv + xe*i/ndiv

# 描画
def Draw(a, b, N):
    fig = plot.figure()
    graph = fig.add_subplot()
    graph.set_xlim(a, b)
    graph.set_aspect('equal')

    # f(x)
    px = []; py = []; M = 1000
    for i in range(M+1):
        x = xi(i, a, b, M)
        px += [x]
        y = f(x)
        py += [y]
    graph.plot(px, py)

    # 台形
    for i in range(N):
        px = []; py = []
        xs = xi(i, a, b, N); ys = f(xs)
        px += [xs]; py += [ys]
        xe = xi(i+1, a, b, N); ye = f(xe)
        px += [xe]; py += [ye]
        px = [xs] + px + [xe] + [xs]
        py = [0] + py + [0] + [0]
        graph.plot(px, py)
    
    plot.show()

N = 12
a = 0
b = 1

Draw(a, b, N)