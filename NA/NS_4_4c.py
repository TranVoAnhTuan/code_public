import math
def fx(x):
    res = 2*x*math.cos(2*x)-(x+1)**2
    return res

def chiadoi(a, b, esp):
    res = []
    e = (b-a)/2
    k =1
    while e> esp:
        c= (a+b)/2
        k = k+1
        res.append([a,b,c,e])
        e /= 2 
        if fx(c) == 0:
            return c
        else:
            if fx(a) * fx(c) < 0:
                a = a
                b = c
            else:
                a = c
                b = b 
    res.append([a,b,(a+b)/2,e])
    return res, k

print(chiadoi(-3,-2,0.0001))
