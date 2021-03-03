import matplotlib
import matplotlib.pyplot as plot
from math import *

def f(x):
    return sqrt(1-x**2)

def g(x):
    return 1/(1+x**2)

def Daikei(N, a, b, f):
    h = (b-a)/N
    T = h*(f(a) + f(b))/2
    for j in range(1, N):
        x = a+j*h
        T += h*f(x)
    return T

print('円周率の計算（1）')
print("{0:3}   {1:7}   {2:8}".format('分割数', '計算値', '誤差'))
for n in [2**n for n in range(1, 9)]:
    T = Daikei(n, 0, 1, f)*4
    print("{0:6d}   {1:.8f}   {2:.8f}".format(n, T, T-pi))

print('円周率の計算（2）')
print("{0:3}   {1:7}   {2:8}".format('分割数', '計算値', '誤差'))
for n in [2**n for n in range(1, 9)]:
    T = Daikei(n, 0, 0.5, f)*12 - 3/2*sqrt(3)
    print("{0:6d}   {1:.8f}   {2:.8f}".format(n, T, T-pi))

print('円周率の計算（3）')
print("{0:3}   {1:7}   {2:8}".format('分割数', '計算値', '誤差'))
for n in [2**n for n in range(1, 9)]:
    T = Daikei(n, 0, 1, g)*4
    print("{0:6d}   {1:.8f}   {2:.8f}".format(n, T, T-pi))
