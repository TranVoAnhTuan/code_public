import math
def fx(x):
    return x-math.cos(x)
def dayCung(x0, b, eps , M, m):
    res = []
    e=10e6
    k = 0
    while e >= eps:
        k += 1
        x1 = x0 - ((b-x0)/(fx(b)-fx(x0)))*fx(x0)
        e = ((M-m)/m) * abs(x1-x0)
        res.append([k,x1,e])
        x0=x1
    return res

M = 2
m = 1
x0 = 0
b = 1
eps= 0.001
print(dayCung(x0, b, eps, M, m))


