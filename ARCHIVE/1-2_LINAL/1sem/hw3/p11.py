from sympy import *

moduleA = 4
moduleB = 1
fi = 2 * pi / 3
c, d, e, f = -3, 4, -4, 1

# c f e d
S = ((c * moduleA) * (f * moduleB) - (e * moduleA) * (d * moduleB)) * sin(fi)

print(S)
print(f'{S.evalf(chop=True):.2f}')
