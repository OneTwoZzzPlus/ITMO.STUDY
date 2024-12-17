def cleaner(data: list[float|None]) -> list[float]:
    """
    Очищает список от None значений
    :param data: список входящих значений
    :return: список значений без None
    """
    return [x for x in data if x is not None and x > 0]


def mean(data: list[float]) -> float:
    """
    Находит среднее арифметическое списка чисел
    :param data: список значений
    :return: среднее арифметическое или 0
    """
    return 0 if len(data) == 0 else round(sum(data) / len(data), 2)


def best(data: list[float]) -> list[float]:
    """
    Находит до 3 лучших значений
    :param data: список значений
    :return: список из не более трёх минимальных значений
    """
    if len(data) <= 1:
        return data  # Сортировать нечего
    elif len(data) == 2:
        return [min(data), max(data)]  # Сортируем 2 элемента
    else:
        return sorted(set(data))[:3]  # Берём 3 наименьших уникальных значения


def input_list() -> list[float|None]:
    """
    Ввод списка с None значениями
    :return: список
    """
    res = []
    while (inp := input(' > ')) != '':  # Пока ввод не пустая строка
        try:
            if inp == 'None':
                res.append(None)
            elif len(inp) > 300:  # Обработка переполнения float
                raise ValueError
            else:
                f = float(inp)
                if f <= 0:  # Положительность числа
                    raise ValueError
                res.append(f)  # Добавляем элемент
        except ValueError:
            print('Неправильное значение!')
    return res


input_data = input_list()
clear_data = cleaner(input_data)
print('Среднее значение =', mean(clear_data))
print('Лучшие значения:', *best(clear_data))
