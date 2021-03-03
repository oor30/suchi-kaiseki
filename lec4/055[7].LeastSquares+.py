import matplotlib
import matplotlib.pyplot as plot

# Gaussの消去法
def Gauss(N, A, y):
    x = [0]*N   # 未知ベクトル

    # 前進消去
    for k in range(N-1):
        m = 0   # 最大値
        for i in range(k, N):
            if m < abs(A[i][k]):
                m = abs(A[i][k])
                l = i
            if l != k:
                for n in range(k, N):
                    A[k][n], A[l][n] = A[l][n], A[k][n]
                y[k], y[l] = y[l], y[k]

        for i in range(k+1, N):
            alpha = A[i][k]/A[k][k]
            for j in range(k+1, N):
                A[i][j] -= alpha*A[k][j]
            y[i] -= alpha*y[k]
    
    # 交代消去
    x[N-1] = y[N-1]/A[N-1][N-1]

    for i in range(N-2, -1, -1):
        s = 0   # 合計
        for k in range(i+1, N):
            s += A[i][k]*x[k]
        x[i] = (y[i] - s)/A[i][i]

    return x

# 関数
def f1(x):
    return x**2
def f2(x):
    return x
def f3(x):
    return 1

def f(x, n):
    return x**(3-n)

# 描画
def Draw(px, py, a, b):
    fig = plot.figure()         # 図
    graph = fig.add_subplot()   # グラフを配置
    xs = min(px); xe = max(px)
    graph.set_xlim(xs,xe)       # 描画範囲(X軸)
    lx = []; ly = []            # 二次曲線上の節点座標
    for i in range(M+1):
        x = (M-1)/M*xs + i/M*xe
        lx += [x]
        ly += [ABC[0]*f1(x) + ABC[1]*f2(x) + ABC[2]*f3(x)]
    graph.plot(lx, ly)                      # 線を描画
    graph.scatter(px, py, s=30, c="red")    # 点を描画
    plot.show()     # 表示

# 最小２乗法（y=Ax^2+Bx+C）
def LeastSquares(N,x,y):
    p = [[0.0]*3]*3
    for j in range(N):
        xj = x[j]
        for r in range(3):
            for c in range(3):
                print('r:', r, ', c:', c)
                p[r][c] += f(xj, r+1)*f(xj, c+1)
                p[r][c]
                print('p[r][c]:', p[r][c], ', f(xj, r+1)', f(xj, r+1), 'f(xj, c+1)', f(xj, c+1))
    
    q = [0.0]*3
    for j in range(N):
        xj = x[j]; yj = y[j]
        for k in range(3):
            q[k] += yj*f(xj, k+1)
    
    return Gauss(3, p, q)

# 実行
N = 5                           # 点数
x = [0.0, 0.5, 1.0, 1.5, 2.0]   # x座標
y = [-0.45, 0.20, 0.53, 0.28, -0.62]    # y座標

ABC = LeastSquares(N,x,y)
print('A = ', ABC[0], ', B = ', ABC[1], ', C = ', ABC[2])

M = 20
Draw(x, y, ABC, M)    # 描画

# input("[Enter]キーを押して終了")
