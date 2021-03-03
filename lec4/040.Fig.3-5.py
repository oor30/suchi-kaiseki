import matplotlib
import matplotlib.pyplot as plt

from math import sin

# 描画
def Draw(xs, xe, px, py, lx, ly):
    fig = plt.figure()
    graph = fig.add_subplot()
    graph.set_xlim(xs, xe)

    graph.plot(lx, ly)
    graph.scatter(px, py, s=30, c="red")

    plt.show()

# ラグランジュ補間関数
def Lagrange(N, px, py, x):
    y = 0.0
    for j in range(N):
        lj = 1.0
        for i in range(N):
            if i != j:
                lj = lj*(x-px[i])/(px[j]-px[i])
        y += py[j]*lj
    return y

# 実行
N = 7   # 点数
px = []; py = []    # 座標
for i in range(N):
    px += [0.5+i]
    py += [sin(0.5+i)]

M = 50              # x方向分割数
lx = []; ly = []    # 曲線の座標

for i in range(0,M+1):
    x=i/M*N     # 注) 0 < x < 1
    y=Lagrange(N,px,py,x)
    lx += [x]; ly += [y]

Draw(0.0, float(N), px, py, lx, ly)
    
#input("[Enter]キーを押して終了")
