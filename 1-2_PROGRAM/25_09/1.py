# Input
gender = None
while gender is None:
    r = input('Пол > ')
    if r == 'м':
        gender = True
    elif r == 'ж':
        gender = False

name = input('Имя > ')

age = None
while age is None:
    r = input('Возраст > ')
    if r.isdigit():
        age = int(r)

if 10 <= age % 100 <= 19:
    y = 'лет'
elif age % 10 == 1:
    y = 'год'
elif 2 <= age % 10 <= 4:
    y = 'года'
else:
    y = 'лет'


s = f"{'Его' if gender else 'Её'} зовут {name}. {'Ему' if gender else 'Ей'} {age} {y}."

print(s)
