from random import randint
k, answer = 0, 0
print('Начнём игру! "Q" - выход')
while True:
    # Старт раунда
    if k == 0:
        answer = randint(1, 100)
    # Ввод
    r = input('Ваш вариант: ')
    if r == 'Q':
        break
    if not r.isdigit():
        print('Введите натуральное число!')
        continue
    d = int(r)
    if not 1 <= d <= 100:
        print('Введите число от 1 до 100 включительно!')
        continue

    # main
    if d == answer:
        print('Вы угадали =)')
        print('Сыграем ещё раз!')
        k = 0
        continue
    elif answer > d:
        print(f'Загаданное число БОЛЬШЕ')
    elif answer < d:
        print(f'Загаданное число МЕНЬШЕ')

    # Счётчик попыток
    k += 1
    if k == 10:
        print('Вы исчерпали 10 попыток =(')
        print('Сыграем ещё раз!')
        k = 0
        continue
