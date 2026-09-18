from sympy import *


def prod(v1, v2):
    # Векторное умножение
    x = v1[1] * v2[2] - v1[2] * v2[1]
    y = -(v1[0] * v2[2] - v1[2] * v2[0])
    z = v1[0] * v2[1] - v1[1] * v2[0]
    return x, y, z


def su(v1, v2):
    # Сумма
    return v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2]


def msc(x, v):
    # Умножение на скаляр
    return x * v[0], x * v[1], x * v[2]


# ВВОД векторов
# a = (0, 4, -4)
# b = (1, -3, -4)
# res = su(prod(a, su(msc(1, a), msc(2, b))), prod(a, msc(-4, prod(a, b))))

# a = (-4, 2, 0)
# b = (-1, -5, 2)
# res = su(prod(a, su(msc(1, a), msc(4, b))), prod(a, msc(-2, prod(a, b))))

# a = (-3, -2, -1)
# b = (1, 4, 4)
# res = su(prod(a, su(msc(3, a), msc(-2, b))), prod(a, msc(-5, prod(a, b))))

# a = (-3, 2, -4)
# b = (-1, -4, 0)
# res = su(prod(a, su(msc(-2, a), msc(-1, b))), prod(a, msc(3, prod(a, b))))

a = (-3,0,-4)
b = (-4,-4,3)
res = su(prod(a, su(msc(4, a), msc(3, b))), prod(a, msc(1, prod(a, b))))


print(res)

print(f'[{res[0]}, {res[1]}, {res[2]}]')
