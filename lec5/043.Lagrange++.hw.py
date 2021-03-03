import matplotlib
import matplotlib.pyplot as plot

# 描画関数
def Draw(px, py, lx, ly):
    N = len(px)     # len(px):pxの要素数
    fig = plot.figure()             # 図
    graph = fig.add_subplot()       # グラフ
    graph.set_xlim(px[0], px[N-1])  # 描画範囲

    graph.plot(lx, ly)                      # 曲線
    graph.scatter(px, py, s=30, c="red")    # 代表点

    plot.show()     # 表示

# ラグランジュ補間関数
def Lagrange(px, py, x):
    N = len(px)
    y = 0.0
    for j in range(N):
        lj = 1.0
        for i in range(N):
            if i != j:
                lj = lj*(x-px[i])/(px[j]-px[i])
        y += py[j]*lj
    return y

# 関数
def f(x):
    if x<-0.5:
        return 2*x+2.0
    elif x<0.5:
        return -2*x
    else:
        return 2*x-2.0

# [xs, xe]間をndiv分割したときにi番目となる点のx座標(0≦i≦ndiv)
def xi(i, xs, xe, ndiv):
    return xs*(ndiv-i)/ndiv + xe*i/ndiv

# 範囲[xs, xe]
xs = -1.0; xe = 1.0

# サンプル点
N = 8               # 区間数(4or8)
px = []; py = []    # 座標
for i in range(N+1):
    x = xi(i, xs, xe, N)
    y = f(x)
    px += [x]; py += [y]

# 曲線を構成する点群
M = 200             # 点数
lx = []; ly = []    # 曲線上の点

for i in range(M+1):
    x = xi(i, xs, xe, M)
    y = Lagrange(px, py, x)
    lx += [x]; ly += [y]

# 描画
Draw(px, py, lx, ly)