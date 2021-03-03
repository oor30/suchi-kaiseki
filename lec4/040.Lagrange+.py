import matplotlib
import matplotlib.pyplot as plt

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
N = 3   # 点数
px = [0.2, 0.6, 0.8] # x座標
py = [0.3, 0.8, 0.4] # y座標

M = 10              # x方向分割数
lx = []; ly = []    # 曲線の座標

for i in range(0,M+1):
    x=i/M*N     # 注) 0 < x < 1
    y=Lagrange(N,px,py,x)
    lx += [x]; ly += [y]

Draw(0.0, 1.0, px, py, lx, ly)
    
# input("[Enter]キーを押して終了")
