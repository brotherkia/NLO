from numdifftools import Gradient
from numpy import arange

x = [-2, -5]
e = 0.01

def f(x):
    # y = (2 * (x[0] ** 3)) + (3 * (x[1] ** 2)) + (3 * ((x[0] ** 2) * x[1])) - (24 * (x[1]))
    y = x[0] ** 2 + x[1] ** 2
    return y

def norm(x):
    y = 0
    for i in range(len(x)):
        y += x[i] ** 2
    
    return y ** 0.5


while norm(Gradient(f)(x)) > e:
    tmp = [0 for i in range(len(x))]
    hlp = 1000000000
    d = []
    x_next = [0 for i in range(len(x))]
    
    for i in Gradient(f)(x):
        d.append(-1 * i)

    print(f'{x}:{d}')
    for t in arange(0, 1, 0.17):
        for i in range(len(d)):
            tmp[i] = x[i] + (t * d[i])
        if f(tmp) < hlp:
            x_next = tmp
            hlp = f(tmp)
    x = x_next

print(f'point: {x}, min: {f(x)}')
