import matplotlib
import matplotlib.pyplot as plt

# 関数(p.43 図3-6)
def f(x):
    return 1/(1+25*(x**2))

# 描画
def Draw(xs, xe, px, py, lx, ly):
    fig = plt.figure()          # 図
    graph = fig.add_subplot()   # グラフを配置
    graph.set_xlim(xs, xe)      # 描画範囲(x軸)

    graph.plot(lx, ly)                      # 線を描画
    graph.scatter(px, py, s=30, c="red")    # 点を描画

    plt.show()      # 表示

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
N = 11  # 点数
px = [] # x座標
py = [] # y座標

for i in range(N):
    x = 2*i/(N-1) - 1   # -1 < x < 1
    px += [x]
    py += [f(x)]

M = 1000              # x方向分割数
lx = []; ly = []    # 曲線の座標

for i in range(0,M+1):
    x = 2*i/M - 1     # 注) -1 < x < 1
    y = Lagrange(N,px,py,x)
    lx += [x]; ly += [y]

Draw(-1.0, 1.0, px, py, lx, ly)