def input_int(s: str) -> int:
    while True:
        r = input(s + ' > ')
        try:
            return int(r)
        except TypeError:
            pass


a = input_int('Введите a')
b = input_int('Введите b')
c = input_int('Введите c')

D = b * b - 4 * a * c

if a == b == 0 or D < 0:
    print('Уравнение корней не имеет')
elif a == 0:
    x = -c / b
    x = int(x) if x % 1 == 0 else x
    print(f'Уравнение имеет один корень: x = {x}')
elif D == 0:
    x = -b / 2 / a
    x = int(x) if x % 1 == 0 else x
    print(f'Уравнение имеет один корень: x = {x}')
else:
    x1 = (-b - D ** 0.5) / 2 / a
    x1 = int(x1) if x1 % 1 == 0 else x1
    x2 = (-b + D ** 0.5) / 2 / a
    x2 = int(x2) if x2 % 1 == 0 else x2
    print(f'Уравнение имеет два корня: x1 = {x1} и x2 = {x2}')