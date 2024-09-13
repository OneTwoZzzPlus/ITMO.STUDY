from data import *

print('Программа создана, чтобы угадывать однокурсников "инфокома", которых вы загадали!')
print('Вводите ответ на вопрос одним словом или символом: +/-, да/нет, true/false, 1/0 etc.')
step = -1
while True:
    # Запуск
    if step < 0:
        print('\nНачинаем игру!')
        step = 0
        key = ''
        people_keys = sorted(people.keys())
    # Дополнительный вопрос
    elif step >= len(questions):
        print('УНИКАЛЬНЫЙ ВОПРОС')

    # Вопрос
    print(questions[step])
    # Ввод ответа
    inp = None
    while inp is None:
        try:
            # Получение строки от пользователя в нижнем регистре, опуская пробелы и точки
            raw = input('>>> ').lower().replace(' ', '').replace('.', '')
            # Поиск значения
            if raw == 'exit':
                exit(0)
            elif raw in true_answers:
                inp = True
            elif raw in false_answers:
                inp = False
            else:
                raise ValueError
        except (EOFError, ValueError):
            # Ошибка при вводе
            print("Некорректный ввод!")
        except KeyboardInterrupt:
            exit(0)
    # Обработка шага
    inp_v = '1' if inp else '0'
    # Убираем из списка всех не подходящих по характеристике
    people_keys = [x for x in people_keys if x[step] == inp_v]

    if len(people_keys) == 1:
        # Отгадали, если остался только 1
        print(f'Ваш загаданный однокурсник {people[people_keys[0]]}!')
        step = -1
        # exit(0)
    else:
        print(f'Выбираем из {len(people_keys)} человек.')
        print(f'{bcolors.WARNING}{people_keys}{bcolors.ENDC}')
        # Если на следующий вопрос у всех кандидатов одинаковая характеристика - пропускаем вопрос
        while all(x[step] == people_keys[0][step] for x in people_keys):
            step += 1

