# 初期化
a = float(input("a = "))
x = a

# 反復
for i in range(5):
    x = x/2 + a/(x*2)
    print("{0:2d} {1:.15f}".format(i+1,x))

# 入力待ち
input("[Enter]キーを押して終了")
