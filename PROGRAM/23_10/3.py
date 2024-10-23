from random import randint
from names_api import get_names

# 1

medium = 10  # int(input())
values = [randint(1, 20) for _ in range(20)]
forms = ["HIGH" if x > medium else "LOW" for x in values]

print('Числа', values, end='\n\n')
print('Значения', forms, end='\n\n')

# 2

names = get_names()
ak_names, other_names = [], []
for x in names:
    if 'А' <= x[0] <= 'К':
        ak_names.append(x)
    else:
        other_names.append(x)

print('Имена', names, end='\n\n')
print('Имена от А до К', ak_names, end='\n\n')
print('Остальные имена', other_names, end='\n\n')
