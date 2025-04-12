from sympy import *

A, B, C, D, E, F = symbols('A, B, C, D, E, F', real=True)

# ВВОД ЗНАЧЕНИЙ КОЭФФИЦИЕНТОВ Ax^2 + 2Bxy + Cy^2 + Dx + Ey + F = 0
values = [(A, 17), (B, 3 * sqrt(3)), (C, 11), (D, 0), (E, 0), (F, 4)]


tet = atan(2 * B / (A - C)) / 2
rad = expand(tet.subs(values))
print('Угол поворота =', rad)
print(rad * (180 / pi))


