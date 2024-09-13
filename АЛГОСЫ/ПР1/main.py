from data import *

repeat = True
print('''Программа создана, чтобы угадывать однокурсников и адаптеров K3120 и K3121!'
Вводите ответ на вопрос одним словом или символом: +/-, да/нет, true/false, 1/0 etc.
Для выхода введите exit или нажмите ctrl+C.''')

step, people_keys = -1, []
while True:
    # Запуск
    if step < 0 or step >= len(questions):
        print(f'\nНачинаем игру!')
        step = 0
        key = ''
        people_keys = sorted(people.keys())

    # Вопрос
    print(questions[step])

    # Ввод ответа
    inp = None
    while inp is None:
        try:
            # Получение строки от пользователя в нижнем регистре, опуская пробелы и точки
            raw = input('>>> ').lower().replace(' ', '').replace('.', '')
            # Поиск значения ввода
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
            print('Некорректный ввод!')
        except KeyboardInterrupt:
            exit(0)

    # Убираем из списка всех не подходящих по характеристике
    inp_v = '1' if inp else '0'
    people_keys = [x for x in people_keys if x[step] == inp_v]

    if len(people_keys) == 1:
        # Отгадали, если остался только 1
        print(f'Ваш загаданный однокурсник {people[people_keys[0]]}!')
        if repeat:
            step = -1  # Перезапуск
        else:
            input('Нажмите enter для выхода...')
            exit(0)  # Выход
    else:
        print(f'Выбираем из {len(people_keys)} человек.')
        # print(people_keys)
        # Если на следующий вопрос у всех кандидатов одинаковая характеристика - пропускаем вопрос
        while all(x[step] == people_keys[0][step] for x in people_keys):
            step += 1
