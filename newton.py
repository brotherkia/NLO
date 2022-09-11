import numpy as np
from numdifftools import Gradient
from torch import tensor
from torch.autograd.functional import hessian

x = np.array([1., 2.])
e = 0.00001

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

    inp = tensor(x)
    hes = hessian(f, inp)
    
    hes_inv = np.linalg.inv(hes)
    hes_inv = np.array(hes_inv)
    print(f'hes = {hes_inv}')

    grd = Gradient(f)(x)
    grd = np.array(grd)
    print(f'grd = {grd}')

    d = np.dot(hes_inv, grd)
    d = np.multiply(d, -1)
    x = np.add(x, d)
    print(f'multiply = {d}')
    print()

print(f'point: {x}, min: {f(x)}')
