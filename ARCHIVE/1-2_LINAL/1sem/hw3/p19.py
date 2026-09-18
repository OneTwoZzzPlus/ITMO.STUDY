from sympy import *

# точка
A = (12*sqrt(2), 48)
# асимптоты y=±Kx
K = 4

k, x, y = K, A[0], A[1]
a = ((k**2 * x**2 - y**2) / (k**2))**0.5
b = k * a

val = lambda num: int(num) if float(num) % 1 == 0 else num
print(f'[{val(expand(a))}, {val(expand(b))}]')


