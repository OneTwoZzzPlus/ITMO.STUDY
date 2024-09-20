from data import *


def input_bool() -> bool:
    inp = None
    while inp is None:
        try:
            # Получение строки от пользователя в нижнем регистре
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
            exit(0)  # Выход
    return inp


print('''Программа создана, чтобы угадывать однокурсников и адаптеров K3120 и K3121!'
Вводите ответ на вопрос одним словом или символом: +/-, да/нет, true/false, 1/0 etc.
Для выхода введите exit или нажмите ctrl+C.''')

step, people_keys = -1, []
while True:
    # Запуск
    if step < 0 or step >= len(questions):
        print(f'\nНачинаем игру!')
        step = 0
        people_keys = sorted(people.keys())

    # Вопрос
    print(questions[step])

    # Ввод ответа
    inp = '1' if input_bool() else '0'
    
    # Убираем из списка всех не подходящих по характеристике
    people_keys = [x for x in people_keys if x[step] == inp]

    if len(people_keys) == 1:
        # Отгадали, если остался только 1
        print(f'Ваш загаданный однокурсник {people[people_keys[0]]}!')
        input('Нажмите enter для выхода...')
        exit(0)  # Выход
    else:
        print(f'Выбираем из {len(people_keys)} человек.')
        # Если на следующий вопрос у всех кандидатов 
        # одинаковая хар-ка - пропускаем вопрос
        while all(x[step] == people_keys[0][step] for x in people_keys):
            step += 1

