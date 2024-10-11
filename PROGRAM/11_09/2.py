from input_check import input_int

seconds = input_int("Введите количество секунд: ")

minute, seconds = seconds // 60, seconds % 60
hour, minute = minute // 60, minute % 60
day, hour = hour // 24, hour % 24

result = f'{day}:{hour:02}:{minute:02}:{seconds:02}'
print(result)
