from sympy import *
x, y = symbols('x y')

# # Прямая L1
# eq = Eq(6*x + 1*y, -3)
# # Прямая L2
# r = (-13, -3)
# s = (9, 13)

# # Прямая L1
# eq = Eq(-12*x + -5*y, -5)
# # Прямая L2
# r = (-7, 12)
# s = (1, -6)

# # Прямая L1
# eq = Eq(-6*x - y, -13)
# # Прямая L2
# r = (-8, 0)
# s = (6, -3)

# # Прямая L1
# eq = Eq(11*x + 10*y, 4)
# # Прямая L2
# r = (0, -5)
# s = (-4, -4)

# Прямая L1
eq = Eq(-2*x - 14*y, -15)
# Прямая L2
r = (3, -5)
s = (14, 7)

yq = solve(eq, y)[0]
X = solve(Eq(s[0]*(yq-r[1]), s[1]*(x-r[0])), x)[0]
Y = yq.subs(x, X)
print(X, Y)

print(f"[{expand(X)}, {expand(Y)}]")
