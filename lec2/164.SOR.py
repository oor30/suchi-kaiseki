# 経過表示
def Progress(k,x):
    print(k,end="")
    for val in x:
        print(' {:.8f}'.format(val), end="")
    print('')
    
# SOR法
def SOR(N,A,y,omega):
    x = [0]*N # 未知ベクトル
    k = 0
    Progress(0,x) # 経過表示
    
    while True: # 反復ループ
        sum = 0
        error = 0
        k = k + 1
        for i in range(N):
            total = 0
            for j in range(N):
                if i != j:
                    total += A[i][j]*x[j]
                    new_x = omega*(y[i] - total)/A[i][i] + (1 - omega)*x[i]
                    sum = sum + abs(new_x)
                    error = error + abs((new_x - x[i]))
            x[i] = new_x
            
        if error < sum * 0.001: # eps=0.001
            Progress(k,x)
            return x
        Progress(k,x) # 経過表示
    return x


N = 2 # 未知数の個数
A = [[5,4],[2,3]] # 係数行列
y = [13,8] # 右辺ベクトル
omega = 1.2 # 加速係数
x = SOR(N,A,y,omega)
input("[Enter]キーを押して終了")
