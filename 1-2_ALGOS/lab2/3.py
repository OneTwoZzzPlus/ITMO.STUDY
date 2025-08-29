"""
O(n!)
Рекурсивное нахождение всех перестановок
"""
def permutations(arr: list[int], border = None, res = [], ret = []):
    # Контроль глубины рекурсии
    border = len(arr) - 1 if border is None else border - 1

    if border == 0:
        # Базовый случай
        res = res + [arr[0]]
        ret.append(res)
        return ret
    else:
        for i in range(len(arr)):
            ret = permutations(arr[:i] + arr[i+1:], border, res + [arr[i]], ret)
    return ret


# Список случайных чисел
a = [__import__('random').randint(0, 1000) for _ in range(5)]
# a = map(int, input().split())
print('Исходный:', a, '\n')
for x in permutations(a):
    print(x)

