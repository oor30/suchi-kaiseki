import matplotlib
import matplotlib.pyplot as plot
from math import sin, pi

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
                    A[k][n], a[l][n] = A[l][n], A[k][n]
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

# 関数(p.55[3])
def f(x):
    return sin(x)/(1+x)

# 描画
def Draw(xmin, xmax, px, py, a, b, c, d):
    fig = plot.figure()
    graph = fig.add_subplot()
    graph.set_xlim(xmin, xmax)
    #自然スプライン
    dx = (xmax-xmin)/len(a)
    for j in range(len(a)):
        xj = xmin + j*dx    # xk = xj + dx
        qx = []; qy = []
        M = 10  # 1区間をM分割
        for i in range(M+1):
            x = xj + dx*i/M
            qx += [x]
            qy += [a[j]*(x-xj)**3 + b[j]*(x-xj)**2 + c[j]*(x-xj) + d[j]]
        graph.plot(qx, qy)
        graph.scatter(px, py, s=30, c="red")
        
    plot.show()

# 自然スプライン
def NaturalSpline(N, px, py):
    h = [0]*10
    for j in range(N):
        h[j] = px[j+1]-px[j]
    v = [0]*N
    for j in range(N):
        v[j] = 6*((py[j+1]-py[j])/h[j] - (py[j]-py[j-1])/h[j-1])
    
    # 連立方程式の作成
    A = []
    for i in range(N-1):
        A += [[0]*(N-1)]
    for i in range(N-1):
        A[i][i] = 2*(h[i]+h[i+1])   # 対角成分
    for i in range(N-2):
        A[i][i+1] = h[i+1]  # 対角周辺
        A[i+1][i] = h[i]    # 対角周辺
    y = [0]*(N-1)   # 右辺ベクトル
    for i in range(N-1):
        y[i] = v[i+1]

    x = Gauss(N-1, A, y)    # p.47 (3.32)式

    u = [0] + x + [0]       # 両端の境界条件

    b = [0]*N
    for j in range(N):
        b[j] = u[j]/2   # (3.20)式
    a = [0]*N
    for j in range(N):
        a[j] = (u[j+1]-u[j])/(6*(px[j+1]-px[j]))    # (3.22)式
    d = [0]*N
    for j in range(N):
        d[j] = py[j]    # (3.24)式
    c = [0]*N
    for j in range(N):
        c[j] = (py[j+1]-py[j])/(px[j+1]-px[j])-(px[j+1]-px[j])*(2*u[j]+u[j+1])/6    # (3.25)式

    return a, b, c, d

# 実行
N = 10
px = []; py = []
for i in range(0,N+1):
    px += [i]
    py += [f(i)]

a, b, c, d = NaturalSpline(N, px, py)

Draw(0, 3*pi, px, py, a, b, c, d)