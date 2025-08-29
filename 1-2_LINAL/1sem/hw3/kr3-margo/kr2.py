from sympy import *
t, x, y = symbols('t x y')

# Прямая ax+by=c
a = -12
b = 2
c = 6
# Точка
A = (4, -3)

# Прямая ax+by=c
# a = 2
# b = 13
# c = 9
# # Точка
# A = (-4, -1)

print('Выразим y через x')
k = -S(a)/b
Y = k * x + S(c)/b
print('y =', Y)

print('Ортогональная прямая через точку А')
ortY = -1 / k * (x - A[0]) + A[1]
print('y =', ortY)

print('Посчитаем коэффициенты')
coeX = -ortY.coeff(x)
coeY = Integer(1)
coeF = ortY.subs(x, 0)
if coeY < 0:
    coeX *= -1
    coeY *= -1
    coeF *= -1
print(f'{coeX}*x + {coeY}*y = {coeF}')
print('Приведём коэффициенты к целым числам')
eq = Eq(coeX*x + Integer(1)*y, coeF)
den_x = eq.lhs.as_numer_denom()[1]
den_y = eq.rhs.as_numer_denom()[1]
lcm_value = lcm(den_x, den_y)
coeX *= lcm_value
coeY *= lcm_value
coeF *= lcm_value
print(f'{coeX if coeX != 1 else ''}x + {coeY if coeY != 1 else ''}y = {coeF}')