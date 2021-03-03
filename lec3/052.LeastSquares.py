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

N = 5 # 点数
x = [1.0, 2.0, 3.0, 4.0, 5.0] # x座標
y = [0.9, 1.7, 2.1, 2.6, 3.0] # y座標

a,b = LeastSquares(N,x,y)
print('A = ',a,', B = ',b)

input("[Enter]キーを押して終了")
