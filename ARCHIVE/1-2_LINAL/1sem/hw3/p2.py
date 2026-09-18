from sympy import *

A, B, C, D, E, F = symbols('A, B, C, D, E, F', real=True)

# ВВОД ЗНАЧЕНИЙ КОЭФФИЦИЕНТОВ Ax^2 + 2Bxy + Cy^2 + Dx + Ey + F = 0
# !!! ВВОДИТЬСЯ B, а не 2B !!!
# values = [(A, 11), (B, -25 * sqrt(3)), (C, -39), (D, -164 * sqrt(3) - 22),
#           (E, -92 + 50 * sqrt(3)), (F, -17 + 164 * sqrt(3))]
values = [(A, 3), (B, sqrt(3)), (C, 1), (D, 10 * sqrt(3) + 44),
          (E, 10 - 12 * sqrt(3)), (F, 153 - 60 * sqrt(3))]


def val(x):
    return x.subs(values).evalf(chop=True)


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

print('Повёрнутая кривая')
vprint(A1=A1, B1=B1, C1=C1, D1=D1, E1=E1)

if val(A1*C1) > 0:  #
    print('ЭЛЛИПС')
    X0 = -D1 / (2 * A1)
    Y0 = -E1 / (2 * C1)
    F1 = F - (D1 ** 2) / (4 * A1) - (E1 ** 2) / (4 * C1)
    vprint(X0=X0, Y0=Y0, F1=F1)
    a2 = abs(-F1 / A1)
    b2 = abs(-F1 / C1)
    c2 = a2 - b2
    vprint(a2=a2, b2=b2, c2=c2)
    a = sqrt(a2)
    b = sqrt(b2)
    c = sqrt(c2)
    vprint(a=a, b=b, c=c)
    E = sqrt(c2 / a2)
    P = b2 / a
    vprint(E=E, P=P)
    print('ОТВЕТ')
    print('E =', val(E))
    print('P =', val(P))
    print(f'[{val(E):.2f}, {val(P):.2f}]')
elif val(A1*C1) != 0:  # ГИПЕРБОЛА
    print('ГИПЕРБОЛА')
    X0 = -D1 / (2 * A1)
    Y0 = -E1 / (2 * C1)
    F1 = F - (D1 ** 2) / (4 * A1) - (E1 ** 2) / (4 * C1)
    vprint(X0=X0, Y0=Y0, F1=F1)
    a2 = abs(-F1/A1)
    b2 = abs(-F1/C1)
    c2 = a2 + b2
    vprint(a2=a2, b2=b2, c2=c2)
    a = sqrt(a2)
    b = sqrt(b2)
    c = sqrt(c2)
    vprint(a=a, b=b, c=c)
    E = sqrt(c2/a2)
    P = b2/a
    vprint(E=E, P=P)
    print('ОТВЕТ')
    print('E =', val(E))
    print('P =', val(P))
    print(f'[{val(E):.2f}, {val(P):.2f}]')
elif val(C1) == 0:  # ПАРАБОЛА x^2=2py
    print('ПАРАБОЛА x^2=2py')
    X0 = -D1 / (2 * A1)
    F1 = F - (D1 ** 2) / (4 * A1)
    vprint(X0=X0, F1=F1)
    p = -E1/(2*A1)
    vprint(p=p)
    print('ОТВЕТ')
    print('E =', 1)
    print('P =', val(p))
    print(f'[{1:.2f}, {val(p):.2f}]')
elif val(A1) == 0:  # ПАРАБОЛА y^2=2px
    print("ПАРАБОЛА y^2=2px")
    Y0 = -E1 / (2 * C1)
    F1 = F - (E1 ** 2) / (4 * C1)
    vprint(Y0=Y0, F1=F1)
    p = -D1 / (2 * C1)
    vprint(p=p)
    print('ОТВЕТ')
    print('E =', 1)
    print('P =', val(p))
    print(f'[{1:.2f}, {val(p):.2f}]')
else:
    print('Это кривая 1 порядка!')
    exit(2)
