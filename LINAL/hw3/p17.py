from sympy import *
x, y = symbols('x y')

# Прямая L1: ax + by = c
a = 3
b = 10
c = -6

# Прямая L2: (x - x_r)/x_s = (y - y_r)/y_s
# r = (x_r, y_r)
r = (8, -6)
# s = (x_s, x_s)
s = (-7, 9)

ans = solve([Eq(a*x+b*y, c), Eq(s[1]*x-s[0]*y, expand(r[0]*s[1]-r[1]*s[0]))], (x, y))
print(ans)

print(f'[{ans[x]}, {ans[y]}]')