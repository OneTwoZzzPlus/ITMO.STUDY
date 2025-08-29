"""
O(n*log(n))
Быстрая сортировка
"""
def quick_sort(arr: list[int]):
    if len(arr) < 2:
        # Базовый случай из 0 или 1 элемента
        return arr
    else:
        # Берём любой элемент
        pivot = arr[0]
        # Разбиваем список на меньший и больший
        less = [x for x in arr[1:] if x <= pivot]
        great = [x for x in arr[1:] if x > pivot]
        # Слияние в рекурсии
        return quick_sort(less) + [pivot] + quick_sort(great)


# Список случайных чисел
a = [__import__('random').randint(0, 1000) for _ in range(100)]
# a = map(int, input().split())
print('Исходный:', a, '\n')
print('Сортированный:', quick_sort(a))

