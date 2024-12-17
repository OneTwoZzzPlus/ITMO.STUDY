"""
    Задача 2
    Дан неотсортированный список, который обязательно включает {0, 1, 2} и никаких других
    Отсортировать по возрастанию. Обосновать.
"""
import random

a = [random.randint(0, 2) for _ in range(10)]
a0, a1, a2 = [], [], []

for x in a:
    if x == 0:
        a0.append(0)
    elif x == 1:
        a1.append(1)
    else:
        a2.append(2)
        
b = a0 + a1 + a2

print(a)
print(b)