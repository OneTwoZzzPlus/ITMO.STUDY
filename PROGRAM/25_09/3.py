def input_int(s: str) -> int:
    while True:
        r = input(s + ' > ')
        try:
            return int(r)
        except TypeError:
            pass


year = input_int('Введите год')

if year < 0:  # отрицательный год
    year = -year - 1

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('Год високосный')
else:
    print('Год не високосный')
