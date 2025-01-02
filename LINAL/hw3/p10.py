from sympy import *

A, B, C, D, E, F = symbols('A, B, C, D, E, F', real=True)

# ВВОД ЗНАЧЕНИЙ КОЭФФИЦИЕНТОВ Ax^2 + 2Bxy + Cy^2 + Dx + Ey + F = 0
values = [(A, 1), (B, 0), (C, 4), (D, -6), (E, 0), (F, -7)]


def val(x):
    return expand(x.subs(values))


def vprint(*args, **kwargs):
    for ar in args:
        print(expand(ar.subs(values)))
    for key, value in kwargs.items():
        print(key, '=', expand(value.subs(values)))


print('Угол поворота')
tet = atan(2 * B / (A - C)) / 2
vprint(Teta=tet)

A1 = A * cos(tet) ** 2 + 2 * B * cos(tet) * sin(tet) + C * sin(tet) ** 2
B1 = 2 * B * cos(2 * tet) + (C - A) * sin(2 * tet)
C1 = A * sin(tet) ** 2 - 2 * B * cos(tet) * sin(tet) + C * cos(tet) ** 2
D1 = D * cos(tet) + E * sin(tet)
E1 = E * cos(tet) - D * sin(tet)

if val(B1) != 0:
    print('ОШИБКА ПРИ ПОВОРОТЕ')
    exit(1)

print('Повёрнут вдоль осей')
vprint(A1=A1, B1=B1, C1=C1, D1=D1, E1=E1, F=F)

print('Сдвиг к канонической СК')
X0 = -D1 / (2 * A1)
Y0 = -E1 / (2 * C1)
F1 = F - (D1 ** 2) / (4 * A1) - (E1 ** 2) / (4 * C1)
vprint(X0=X0, Y0=Y0, F1=F1)
print('Полуоси ^2')
a2 = abs(-F1 / A1)
b2 = abs(-F1 / C1)
vprint(a2=a2, b2=b2)
print('Полуоси')
a = sqrt(a2)
b = sqrt(b2)
vprint(a=a, b=b)

print('Ответ')
print(f"[{val(a)}, {val(b)}]")
print('Если что, поменяйте местами')
