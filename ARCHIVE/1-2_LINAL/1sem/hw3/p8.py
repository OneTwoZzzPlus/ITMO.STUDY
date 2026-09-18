from sympy import *
t, X = symbols('t X')

# Прямая L1
x1 = -15-13*t
y1 = -1-t
# Прямая L2
x2 = 3-9*t
y2 = -14-4*t

T1 = solve(Eq(x1, X), t)[0]
T2 = solve(Eq(x2, X), t)[0]

y1 = y1.subs(t, T1)
y2 = y2.subs(t, T2)

ansX = solve(Eq(y1, y2), X)[0]
ansY = y1.subs(X, ansX)
print(ansX, ansY)

print(f"[{expand(ansX)}, {expand(ansY)}]")
