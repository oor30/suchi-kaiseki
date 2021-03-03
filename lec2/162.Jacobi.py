# 経過表示
def Progress(k,x):
    print(k,end="")
    for val in x:
        print(' {:.8f}'.format(val), end="")
    print('')
    
# ヤコビ法
def Jacobi(N,A,y):
    x = [0]*N # 未知ベクトル
    z = [0]*N # 途中計算用
    k = 0

    Progress(0,x) # 経過表示

    while True: # 無限ループ
        k = k + 1
        sum = 0
        error = 0
        for i in range(N):
            total = 0
            for j in range(N):
                if i != j:
                    total += A[i][j]*x[j]
            z[i] = (y[i] - total)/A[i][i]
            sum = sum + abs(z[i])
            error = error + abs((z[i]-x[i]))
        if error<sum*0.001: # eps=0.001
            Progress(k,x)
            return z
        for i in range(N):
            x[i] = z[i] # 更新
        Progress(k,x) # 経過表示
    return x

N = 2 # 未知数の個数
A = [[5,4],[2,3]] # 係数行列
y = [13,8] # 右辺ベクトル
M = 41 # 反復回数
x = Jacobi(N,A,y)
input("[Enter]キーを押して終了")
