import os
import shutil
import dtf
from typing import Callable

from colorama import init as colorama_init, Fore, Back, Style
CR = Style.RESET_ALL
colorama_init()


# Очистка терминала в зависимости от ОС
cls = lambda: os.system('cls' if os.name=='nt' else 'clear')

# Текущие доступные комманды
_comm: dict[str, tuple[Callable, list, str]] = {}


def set_commands(commands: dict[str, tuple[Callable, list, str]]):
    """ Проверяем на корректность переданные доступные команды  """
    if not (isinstance(commands, dict)
            and all(isinstance(k, str) and isinstance(v, tuple) for k, v in commands.items())
            and all(isinstance(v[0], Callable) and isinstance(v[1], list) and isinstance(v[2], str) 
                    for v in commands.values())
            ):
        raise TypeError('COMMANDS type not dict[str, tuple[Callable, str]]')
    global _comm
    _comm = commands
    


def draw_substate(title: str):
    """ Отрисовка временной страницы TUI """
    cls()  # Очистка экрана
    x, _ = shutil.get_terminal_size((80, 20))
    # Размеры линий
    equ = (x - len(title) - 3) // 2
    eqc = int(not(x % 2))
    # Линия с подписью
    print(f'{Fore.GREEN}{'=' * equ} {title} {'=' * equ}{'=' * eqc}{Style.RESET_ALL}')
    

def draw_state(title: str, 
          caption_up: str='',
          caption_down: str=''):
    global _comm
    """ Отрисовка страницы TUI """
    
    cls()  # Очистка экрана
    x, _ = shutil.get_terminal_size((80, 20))
    # Размеры линий
    equ = (x - len(title) - 3) // 2
    eqf = 2 * equ + len(title) + 2
    eqc = int(not(x % 2))
    # Линия с подписью
    print(f'{Fore.GREEN}{'=' * equ} {title} {'=' * equ}{'=' * eqc}{Style.RESET_ALL}')
    
    # Подпись сверху при наличии
    if caption_up != '':
        print(caption_up)
    
    # Список комманд
    com = [
        f'{Fore.CYAN}{key}{' ' if _comm else ''}{' '.join(_comm[key][1])}{Style.RESET_ALL} - {_comm[key][2]} ' 
        for key in _comm
    ]
    # Расчёт размера колонн
    com_len = [
        len(key) + len(_comm[key][2]) + bool(_comm) + len(' '.join(_comm[key][1])) + 4 
        for key in _comm
    ]
    count_columns = x // max(com_len)
    width_columns = x // count_columns
    # Отображение списка комманд в табличном виде
    for i in range(0, len(com), count_columns):
        out = ''
        for j in range(i, min(i + count_columns, len(com))):
            out += com[j] + (' ' * (width_columns - com_len[j]))
        print(out)
    
    # Подпись снизу при наличии
    if caption_down != '':
        print(caption_down)
    
    # Вертикальная линия
    print(f'{Fore.GREEN}{'=' * eqf}{'=' * eqc}{Style.RESET_ALL}')
    

def run(start: Callable):
    """ Приём комманд и переход в другое состояние """
    global _comm
    ret: tuple[Callable, tuple] = start, ()
    while True:
        try:
            # Если нет планируемого состояния, запросить у пользователя
            if ret is None:
                r = input('>>> ').split()
                if r:
                    if r[0] in _comm:
                        if len(r) == 1:
                            ret = (_comm[r[0]][0], ())
                        else:
                            ret = (_comm[r[0]][0], tuple(r[1:]))
                    else:
                        raise KeyError

            if ret is None:
                raise KeyError
            
            # Запустить состояние   
            raw_ret = ret[0](*ret[1])
            
            # Обработать запрос на другое состояние
            if raw_ret is None:
                ret = None
            elif isinstance(raw_ret, Callable):
                ret = (raw_ret, tuple())
            elif isinstance(raw_ret, tuple):
                if len(raw_ret) == 0 or not isinstance(raw_ret[0], Callable):
                    ret = None
                else:
                    if len(raw_ret) == 1:
                        ret = (raw_ret[0], tuple())
                    else:
                        ret = (raw_ret[0], tuple(raw_ret[1:]))
            else:
                ret = None
                
        except (EOFError, KeyError) as e:
            pass
        except (KeyboardInterrupt) as e:
            exit(0)
            
            
def input_bool() -> bool:
    """ Ввод bool """
    
    while True:
        try:
            r = input('[д/н] > ')
            if r in 'yд1+':
                return True
            elif r in 'nн0-':
                return False
        except (EOFError, ValueError, TypeError) as e:
            pass
        except (KeyboardInterrupt) as e:
            exit(0)
            
            
def input_str(max_lenght: int, s: str=" ") -> str:
    """ Ввод str """
    
    while True:
        try:
            # Считываем строку, убирая пустые символы
            r = input(f'{s} > ')
            # Проверяем длину, корректность символов и пустоту
            if not 0 < len(r) <= max_lenght:
                raise ValueError
            if any(x in '\r\n\t,;' for x in r):
                raise ValueError
            if r.isspace():
                raise ValueError
            return r
        except (EOFError, ValueError, TypeError) as e:
            pass
        except (KeyboardInterrupt) as e:
            exit(0)
            

def input_float(maximum: int, decimal_places: int, s: str=" ") -> float:
    """ Ввод float """
    
    while True:
        try:
            # Считываем строку, убирая пустые символы
            r = input(f'{s} > ').replace(' ', '')
            f = float(r)
            n = f * 10**decimal_places
            if (n % 1 != 0) or (not 0 < n <= maximum):
                raise ValueError
            
            return f
        except (EOFError, ValueError, TypeError) as e:
            pass
        except (KeyboardInterrupt) as e:
            exit(0)
            

def input_date() -> dtf.date:
    """ Ввод date """
    # Текущая дата
    
    while True:
        try:
            # Считываем строку, убирая пустые символы
            print(f"Нажмите {Fore.CYAN}enter{CR} или введите {Fore.GREEN}дату{CR}")
            r = input(f'{dtf.now().strftime('%d.%m.%y')} > ').replace(' ', '')
            if r == '':
                # Текущее время
                return dtf.now()
            else:
                # Проверяем дату
                date = dtf.validate_point_date(r)
                if date is not None:
                    return date
                
        except (EOFError, ValueError, TypeError) as e:
            print(e)
        except (KeyboardInterrupt) as e:
            exit(0)
