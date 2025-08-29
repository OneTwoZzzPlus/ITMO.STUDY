""" Программа "Статистика" """

su, minimum, min_i, maximum, max_i = 0, float('inf'), None, 0, None
a = []

while True:
    try:
        s = input(" > ")
        if s == 'Q':
            break
        if len(s) > 300:
            raise ValueError
        f = float(s)
        a.append(f)
        su += f
        if f >= maximum:
            max_i, maximum = len(a) - 1, f
        if f < minimum:
            min_i, minimum = len(a) - 1, f
    except ValueError:
        pass

print("Количество элементов:\t", len(a))
print("Среднее арифметическое:\t", su / len(a) if len(a) != 0 else "не определено")
print("Сумма элементов:\t\t", len(a))

print("Минимальное:\t\t\t", minimum if min_i is not None else "не определено")
print("Индекс минимального:\t", min_i if min_i is not None else "не определено")
print("Максимальное:\t\t\t", maximum if max_i is not None else "не определено")
print("Индекс максимального:\t", max_i if max_i is not None else "не определено")

if min_i is None or max_i is None or abs(max_i - min_i) <= 1:
    print("Произведение:\t\t\t не определено")
else:
    s, f = (min_i, max_i) if (min_i < max_i) else (max_i, min_i)
    p = 1
    for x in a[s + 1:f]:
        p = p * x
    print("Произведение:\t\t\t", p)
