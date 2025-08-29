"""
O(log(n))
Бинарный поиск
"""
def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


a = [1, 23, 214, 4214, 12421, 111223, 933231]
b = 5

print('Исходные:', a)
print('Результат:', binary_search(a, b))

