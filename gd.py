from numdifftools import Gradient
from numpy import arange

power = [0 for i in range(20)]
coefficient = [0 for i in range(20)]
n = int(input('Enter dimention:'))

x = [2 for i in range(n)]
e = 0.001


for i in range(n):
    coefficient[i] = float(input('Enter Coefficient: '))
    power[i] = float(input('Enter Power: '))

c = float(input('Enter c in Function: '))
print(coefficient, power, c)

def f(x):
    y = 0
    for i in range(n):
        y += coefficient[i] * ((x[i]) ** power[i])
    y += c
 
    return y

def norm(x):
    y = 0
    for i in range(len(x)):
        y += x[i] ** 2
    
    return y ** 0.5


while norm(Gradient(f)(x)) > e:
    tmp = [0 for i in range(n)]
    hlp = 1000000000
    d = []
    x_next = [0 for i in range(n)]

    for i in Gradient(f)(x):
        d.append(-1 * i)
    
    for t in arange(0, 1, 0.01):
        for i in range(len(d)):
            tmp[i] = x[i] + (t * d[i])
        if f(tmp) < hlp:
            x_next = tmp
            hlp = f(tmp)
    x = x_next

print(x, f(x))
