from math import sqrt
from input_check import input_float


print("Введите 3 стороны треугольника")
a = input_float("Введите a:", min=0, not_min=True)
b = input_float("Введите b:", min=0, not_min=True)
c = input_float("Введите c:", min=0, not_min=True)

if (a + b > c) and (a + c > b) and (b + c > a):
    p = (a + b + c) / 2
    S = sqrt(p * (p - a) * (p - b) * (p - c))
    print(S)
else:
    print("Неверный треугольник!")
