from math import *

def f1(x):
    return exp(x)

def f2(x):
    return cos(x)

def Daikei(N, a, b, f):
    h = (b-a)/N
    T = h*(f(a) + f(b))/2
    for j in range(1, N):
        x = a+j*h
        T += h*f(x)
    return T

def loop(N, a, b, p, f):
    T = Daikei(N, a, b, f)
    print("{0:4d}   {1:.8f}".format(N, T))
    e = 10**(-p)
    while(True):
        N = 2*N
        new_T = Daikei(N, a, b, f)
        print("{0:4d}   {1:.8f}".format(N, new_T))
        if abs(new_T-T) < e*abs(new_T):
            break
        T = new_T
    return new_T

N = 1
a = 0
b = 1
p = 7

I = loop(N, a, b, p, f1)
I = loop(N, 0, 2, p, f2)

input("[Enter]キーを押して終了")