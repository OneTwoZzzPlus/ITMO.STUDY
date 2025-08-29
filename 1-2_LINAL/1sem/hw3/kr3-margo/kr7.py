from sympy import *
A, B, C = symbols('A B C')

# Ax^2+By^2=C
# values = [(A, S(7)), (B, S(16)), (C, S(112))]
# values = [(A, S(15)), (B, S(16)), (C, S(240))]
values = [(A, S(3)), (B, S(4)), (C, S(12))]

val = lambda x: x.subs(values).evalf(chop=True)

a = (C/A)**0.5
b = (C/B)**0.5
c = (a**2 - b**2)**0.5

R = 2 * c
E = c / a

print(val(a), val(b), val(R), val(E))

print(f'[{val(a)}, {val(b)}, {val(R)}, {val(E)}]')