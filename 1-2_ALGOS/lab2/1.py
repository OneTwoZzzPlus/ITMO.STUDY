"""
O(n)
Нахождение длины самой большой возрастающей 
подпоследовательности в массиве
"""
def find_up(arr: list[int]):
    length, max_length = 1, 1
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            length += 1
            max_length = max(max_length, length)
        else:
            length = 1
    return max_length


# Список случайных чисел
a = [__import__('random').randint(0, 1000) for _ in range(100)]
# a = map(int, input().split())
print('Исходный:', a, '\n')
print('Максимальная длина последовательности:', find_up(a))

