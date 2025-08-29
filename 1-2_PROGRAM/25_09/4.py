name_month = {
    'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6,
    'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12
}
len_month = {
    1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

day, month = None, None
while day is None or month is None:
    r = input('Дата: день и месяц > ')
    data = r.split(' ')
    if len(data) == 2:
        if data[1].isdigit():
            if 1 <= int(data[1]) <= 12:
                month = int(data[1])
        elif data[1] in name_month:
            month = name_month[data[1]]
        if data[0].isdigit() and month is not None:
            if 1 <= int(data[0]) <= len_month[month]:
                day = int(data[0])
                break
    month = None
    print('Неверная дата!')

count = sum(len_month[i] for i in range(month + 1, 13)) + len_month[month] - day + 1

if 10 <= count % 100 <= 19:
    y = 'дней'
elif count % 10 == 1:
    y = 'день'
elif 2 <= count % 10 <= 4:
    y = 'дня'
else:
    y = 'дней'

print(f'Новый год - 1 января 2025 года через {count} {y}!')
