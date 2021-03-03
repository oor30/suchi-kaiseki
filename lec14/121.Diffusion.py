#
# 拡散方程式(改良版)
#
import matplotlib
import matplotlib.pyplot as plot

def Phi(x):
    return 2*x*(1-x) # p.121

N = 6 # 空間分割数
M = 100 # 時間分割数
T = 1 # 時刻の上限
draw = [0,4,8,12,16,20] # 表示するステップ

dx = 1/N
dt = 1/M
a = dt/(dx*dx)

x = [0]*(N+1)
for j in range(N+1):
    x[j] = j*dx
    
U = [0]*(N+1)
new_U = [0]*(N+1)
for j in range(N+1):
    U[j] = Phi(j*dx)

new_U[0] = 0; new_U[N] = 0

fig = plot.figure()
graph = fig.add_subplot()
graph.set_xlim([0,1])
graph.set_ylim([0,1])
graph.set_aspect('equal')

for n in range(M):
    for j in range(1,N):
        new_U[j] = a*U[j+1] + (1-2*a)*U[j] + a*U[j-1]
    for j in range(0,N+1):
        U[j] = new_U[j]
    if n in draw:
        graph.plot(x,U)
        graph.scatter(x,U,s=30)

plot.show()