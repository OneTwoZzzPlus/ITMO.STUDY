def calculate(n: str) -> list[bool]: 
    """ 
        Cтроим список коэффициентов по значениям функции 
        из таблицы истинности методом треугольника
    """
    # 
    sp = [[*n]]
    while len(sp[-1]) != 1: # построение схемы треугольником
        sp.append(list(map(lambda x: sp[-1][x] ^ sp[-1][x + 1], range(len(sp[-1]) - 1))))
    return list(map(lambda x: x[0], sp)) # возвращение коэффициентов


print(calculate([0, 0, 0, 1, 0, 1, 1, 1]))
