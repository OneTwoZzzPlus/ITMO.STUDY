s = 0
while True:
    r = input('Введите координату: ')
    if r == 'STOP':
        break
    x, y = 0, 0
    try:
        t = r.strip().split(' ')
        if len(t) != 2:
            raise ValueError
        x, y = float(t[0]), float(t[1])
    except ValueError:
        print('Вводите 2 числа через пробел!')

    if x != 0 and y != 0:
        a = (1 if y > 0 else 4) if (x > 0) else (2 if y > 0 else 3)
        print(f'+{a}')
        s += a
    else:
        print('Без баллов')

print(f'Общий счёт: {s}')
