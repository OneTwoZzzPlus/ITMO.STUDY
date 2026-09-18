from sympy import *

C, D, E, F = symbols('C, D, E, F', real=True)

# ВВОД ЗНАЧЕНИЙ КОЭФФИЦИЕНТОВ Cy^2 + Dx + Ey + F = 0

values = [(C, -1), (D, 2), (E, 10), (F, 5)]


def val(x):
    return x.subs(values).evalf(chop=True)


def vprint(*args, **kwargs):
    for ar in args:
        print(expand(ar.subs(values)))
    for key, value in kwargs.items():
        print(key, '=', expand(value.subs(values)))


print('Парабола x=ay^2+by+c')
a = -C / D
b = -E / D
c = -F / D
vprint(a=a, b=b, c=c)
print('Вершина параболы')
y0 = -b / (2 * a)
x0 = a*(y0**2) + b*y0 + c
vprint(x0=x0, y0=y0)

print('Сдвиг параболы')
Y0 = -E / (2 * C)
F1 = F - (E ** 2) / (4 * C)
vprint(Y0=Y0, F1=F1)
print('Фокальный параметр')
p = -D / (2 * C)
vprint(p=p)

print('Решение')
print(f'[{expand(x0)}, {expand(y0)}, {expand(p)}]')

print('ОТВЕТ')
print(f'[{val(x0):.2f}, {val(y0):.2f}, {val(p):.2f}]')


