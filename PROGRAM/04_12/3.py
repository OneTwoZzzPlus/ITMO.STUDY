import math


def recursion_power(a: float, n: int) -> float:
    """
    :param a: число
    :param n: степень
    :return: число в степени
    """
    if n == 0:
        return 1  # Базовый случай
    if n < 0:
        return 1 / recursion_power(a, abs(n))  # Отрицательная степень
    return a * recursion_power(a, n - 1)  # Рекурсивный переход


def exp_power(a: float, n: float):
    """
    Берёт экспоненту от натурального логарифма O(1)
    :param a: число
    :param n: степень
    :return: число в степени
    """
    return round(math.exp(math.log(a) * n), 2)


def input_float() -> float:
    """
    :return: Введённый float
    """
    while True:
        try:
            inp = input('число > ')
            if len(inp) > 300:  # Обработка переполнения float
                raise ValueError
            return float(inp)
        except ValueError:
            print('Неправильное значение!')


def input_int() -> int:
    """
    :return: Введённый int
    """
    while True:
        try:
            inp = input('степень > ')
            if len(inp) > 300:  # Обработка переполнения int
                raise ValueError
            return int(inp)
        except ValueError:
            print('Неправильное значение!')


ad = input_float()
nd = input_int()
print('Рекурсивно:', round(recursion_power(ad, nd),  2))
print('exp * log:', exp_power(ad, nd))
