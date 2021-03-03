from math import *

def f1(x):
    return exp(x)

def f2(x):
    return cos(x)

def Simpson(N, a, b, p, f):
    h = (b-a)/2
    T = h*(f(a) + 2*f((a+b)/2) + f(b))/2
    S = h*(f(a) + 4*f((a+b)/2) + f(b))/3
    print("{0:4d}   {1:.15f}".format(N, S))
    e = 10**(-p)
    while(True):
        N = 2*N
        h = h/2
        s = 0
        for i in range(1, N, 2):
            s = s + f(a+i*h)
        new_T = T/2 + h*s
        new_S = (4*new_T - T)/3
        print("{0:4d}   {1:.15f}".format(N, new_S))
        if abs(new_S-S) < e*abs(new_S):
            break
        T = new_T
        S = new_S
    return new_S

N = 2
a = 0
b = 1
p = 12

I = Simpson(N, a, b, p, f1)
I = Simpson(N, 0, 2, p, f2)

input("[Enter]キーを押して終了")