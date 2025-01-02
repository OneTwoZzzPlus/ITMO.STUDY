from sympy import *
t, x, y = symbols('t x y')

# Прямая L
X = -6+12*t
Y = 5-6*t

print('Выразим y через x')
T = solve(Eq(X, x), t)[0]
ansY = Y.subs(t, T)
print('y =', ansY)
print('Посчитаем коэффициенты')
coeX = -ansY.coeff(x)
coeY = Integer(1)
coeF = ansY.subs(x, 0)
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
print(f'{coeX}x + {coeY}y = {coeF}')
