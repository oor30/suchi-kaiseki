import matplotlib
import matplotlib.pyplot as plot

# 描画
def Draw(px, py, a, b):
    fig = plot.figure()         # 図
    graph = fig.add_subplot()   # グラフを配置
    xs = min(px); xe = max(px)
    graph.set_xlim(xs,xe)       # 描画範囲(X軸)
    lx = [xs, xe]               # 始点、終点(X座標)
    ly = [a*xs+b, a*xe+b]       # 始点、終点(Y座標)
    graph.plot(lx, ly)                      # 線を描画
    graph.scatter(px, py, s=30, c="red")    # 点を描画
    plot.show()     # 表示

# 最小２乗法（y=Ax+B）
def LeastSquares(N,x,y):
    sumX = 0.0; sumY = 0.0; sumX2 = 0.0; sumXY = 0.0
    for i in range(N):
        sumX += x[i]
        sumY += y[i]
        sumX2 += x[i]*x[i]
        sumXY += x[i]*y[i]
    
    bunbo = N*sumX2 - sumX*sumX
    a = (N*sumXY - sumX*sumY)/bunbo
    b = (sumX2*sumY - sumX*sumXY)/bunbo
    
    return a,b

# 実行
N = 5                           # 点数
x = [1.0, 2.0, 3.0, 4.0, 5.0]   # x座標
y = [0.9, 1.7, 2.1, 2.6, 3.0]   # y座標

a,b = LeastSquares(N,x,y)
print('A = ',a,', B = ',b)

Draw(x, y, a, b)    # 描画

# input("[Enter]キーを押して終了")
