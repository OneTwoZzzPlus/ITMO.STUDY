from sympy import *
x, y = symbols('x y')

# # Прямая L1
# eq = Eq(6*x + 1*y, -3)
# # Прямая L2
# r = (-13, -3)
# s = (9, 13)

# Прямая L1
eq = Eq(13*x + 14*y, -14)
# Прямая L2
r = (4, -2)
s = (-3, -11)

yq = solve(eq, y)[0]
X = solve(Eq(s[0]*(yq-r[1]), s[1]*(x-r[0])), x)[0]
Y = yq.subs(x, X)
print(X, Y)

print(f"[{expand(X)}, {expand(Y)}]")
