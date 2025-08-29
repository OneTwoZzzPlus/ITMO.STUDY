class RangeError(Exception):
    pass


class IntError(Exception):
    pass


def bin_s(diap, p):
    steps = 0
    ind_max = len(diap) - 1
    ind_min = 0
    while ind_min <= ind_max:
        steps += 1
        a = (ind_max + ind_min) // 2
        if diap[a] < p:
            ind_min = a + 1
        elif diap[a] > p:
            ind_max = a - 1
        else:
            return steps
    return None


try:
    start = int(input('Введите начало отсчета '))
    finish = int(input('Введите конец отсчета ')) + 1
    step = int(input('Введите шаг '))
    sp = list(range(start, finish, step))
    if step < 0:
        sp.reverse()
    if not sp:
        raise RangeError('Неверный диапазон')
    plan = int(input('Введите загаданное число из диапазона '))
    result = bin_s(sp, plan)
    if result is None:
        raise IntError('Такого числа нет в списке')
    print(f'Число шагов = {result}')
except ValueError as r:
    print("Можно вводить только числа")
except RangeError as r:
    print(r)
except IntError as r:
    print(r)

input()