""""""
''' Задание 1
Для диапазона условие:
    если параметр больше 5 и меньше или равен 30, то (a - 5) * 1.2
    если параметр больше 30, то (a - 30) * 1.5'''

a = 40 # тестовое значение
y = (5 < a <= 30) * (a - 5) * 1.2 + (a > 30) * (a - 30) * 1.5
print(y) # 15.0


''' Задание 2
Реализовать смену флага без if'''
n = 10
flag = False

flag = not(n%2)

print(flag)

