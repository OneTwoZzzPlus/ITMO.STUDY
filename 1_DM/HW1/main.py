# 1 - Предлагает сохранить результат в файл
OPTION_SAVE_TO_FILE = 1
# 1 - Не завершается после получения результата
OPTION_LOOP_WORK = 0
# 1 - Выводит ПЖ с переменными, 0 - коэффициенты через запятую
OPTION_NICE_POLINOM = 1


import itertools
import math


def calculate(n: list[bool]) -> list[bool]: 
    """ 
        Cтроим список коэффициентов по значениям функции 
        из таблицы истинности методом треугольника
    """
    # 
    sp = [[*n]]
    while len(sp[-1]) != 1: # построение схемы треугольником
        sp.append(list(map(lambda x: sp[-1][x] ^ sp[-1][x + 1], range(len(sp[-1]) - 1))))
    return list(map(lambda x: x[0], sp)) # возвращение коэффициентов


def read_file(s: str) -> str:
    """
        Если ввод обрамлён "", читает значения ТИ из файла
    """
    if len(s) > 2:
        if s[0] == '"' and s[-1] == '"':
            with open(s.strip('"'), 'r', encoding='utf-8') as file:
                return clear(file.read())
    return s
            
            
def validate_input(s: str):
    """
    Вызывает исключения при неправильной ТИ
    
    Raises:
        InvalidInput 1: лишние символы
        InvalidInput 2: длина не степень 2
    """
    # Проверяем корректность символов в ТИ
    for x in s:
        if x not in '01':
            raise InvalidInput(
                f'Некорректный символ в таблице истинности: "{x}"!')
    # Проверяем длину последовательности
    n = len(s)
    if not (n > 0 and (n & (n-1)) == 0 and n <= 4503599627370496):
        raise InvalidInput(f'ТИ неправильной длины: {n}, '
                            'необходима натуральная степень 2 '
                            '(от 0 до 52 переменных)')


def draw_polinom(result: list[bool]) -> str:
    """
        Преобразуем коэффициенты полинома в полином с переменными
    """
    summands = []
    v = int(math.log2(len(result)))  # кол-во переменных
    vars = symbols[:v]  # буквы для переменных
    for i, a in enumerate(itertools.product([False, True], repeat=v)):
        if all(not(x) for x in a) and result[i]:
            summands.append('1')
        elif result[i]:  # если конъюнкт нужен
            # Перебираем все возможные конъюнкты
            summand = "".join([vars[i] for i in range(v) if a[i]])
            summands.append(summand)
    out = " + ".join(summands)
    if out == '':
        out = '0'
    return out
        

def save_result(polinom: str):
    """
        Предлагает сохранить полином в файл
    """
    print('\nНажмите enter, чтобы выйти, или '
            'введите путь к файлу для сохранения')
    while 1:
        s = clear(input('Сохранить: '))
        if s == '':
            break
        try:
            file = open(s.strip('"'), 'w', encoding='utf-8')
            file.write(polinom)
            file.close()
            break
        except PermissionError:
            print('Недостаточно прав для сохранения!')
        except (FileNotFoundError, FileExistsError):
            print('Такой файл нельзя создать!')


class InvalidInput(Exception):
    pass


clear = lambda x: x.replace('\t', '').replace('\r', '').replace('\n', '')
symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

msg = '''Эта программа строит полином Жегалкина булевой функции, заданной по таблице истинности.

Введите последовательность из 0 и 1 длиной, кратной степени 2.
Например > 10010110

Или путь к файлу (его название, если он лежит в той же директории) "в кавычках".
Например > "./path/to/file.txt"
Или так > "file.txt"

Введите текст после > затем нажмите enter, а случае ошибки, повторите ввод.

Для выхода введите q, для справки введите h.'''


if __name__ == '__main__':
    print(msg)
    while 1:
        try:
            # Ввод, убираем пробелы по краям, пустые символы
            print('\nВведите ТИ или путь к файлу')
            s = input(' > ').strip(' ')
            s = clear(s)
            if s == 'q':
                exit(0)
            if s == 'h':
                print(msg)  
                break
            
            # Заменяем путь к файлу на ТИ
            s = read_file(s)
                    
            # Проверяем корректность ТИ
            s = s.replace(' ', '')
            validate_input(s)
            
            # Производим рассчёт
            result = calculate(map(lambda x: bool(int(x)), s))
            
            # Преобразуем коэффициенты полинома в полином
            if OPTION_NICE_POLINOM:
                polinom = draw_polinom(result)
            else:
                polinom = ", ".join(map(lambda x: str(int(x)), result))
            
            # Вывод на экран
            print("Результат:")
            print(polinom)
            
            # Сохранение результата в файл
            if OPTION_SAVE_TO_FILE:
                save_result(polinom)
            
            if not OPTION_LOOP_WORK: 
                exit(0)
        except KeyboardInterrupt:
            print('Выход по системному прерыванию!')
            exit(0)
        except PermissionError:
            print('Недостаточно прав для работы с файлом!')
        except (FileNotFoundError, FileExistsError):
            print('Такого файла не существует!')
        except UnicodeDecodeError:
            print('Некорректный символ!')
        except InvalidInput as e:
            print(e)
        