from inputter import input_natural


def prime(n: int):
    d = []
    for i in range(2, n + 1):
        if all(i % k != 0 for k in range(2, i)):
            d.append(i)
    return d


n = input_natural("Введите n: ")
lst = prime(n)
if len(lst) == 0:
    print('Нет чисел, удовлетворяющих условию')
else:
    for x in lst:
        print(x, end=' ')
    print()
