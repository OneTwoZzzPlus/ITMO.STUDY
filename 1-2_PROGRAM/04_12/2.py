import bisect

neg, pos = [], []


def partition(x: float) -> tuple[list[float]]:
    """
    Разбиение значений на отрицательные и неотрицательные
    :param x: новое значение
    :return: Кортеж из двух отсортированных списков
    """
    global neg, pos
    if x >= 0:
        # Вставка на место в отсортированный массив неотрицательных значений
        bisect.insort(pos, x)
    else:
        # Вставка на место в отсортированный массив отрицательных значений
        bisect.insort(neg, x)
    return list(reversed(neg)), pos


def main():
    """
    Цикл программы
    """
    while (inp := input(' > ')) != '':  # Пока ввод не пустая строка
        try:
            if len(inp) > 300:  # Обработка переполнения float
                raise ValueError
            print(partition(float(inp)))  # Вывод результата
        except ValueError:
            print('Неправильное значение!')


main()
print((list(reversed(neg)), pos))
