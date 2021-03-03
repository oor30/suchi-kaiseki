from math import*

# 関数
def f(x):
    return exp(-x)-x*x

def g(x): # f'(x)に相当
    return -exp(-x)-2*x

# 初期値の設定（ステップ(1)）
x = 1           # 出発
eps = 1.0e-6    # 収束判定値
n = 0           # 反復（ステップ(2)）

# 反復（ステップ(2)）
while True:
    print("{0:2d} {1:.15f}".format(n,x)) # 途中経過
    new_x = x - f(x)/g(x)
    n = n + 1

    if abs(new_x - x) < eps*abs(new_x):
        break

    x = new_x   # 更新

# 終了（ステップ(3)）
print("{0:2d} {1:.15f}".format(n,new_x))

input("\n[Enter]キーを押して終了")
