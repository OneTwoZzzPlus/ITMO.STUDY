import os
import shutil
from typing import Callable
from colorama import init as colorama_init, Fore, Back, Style
colorama_init()


# Очистка терминала в зависимости от ОС
cls = lambda: os.system('cls' if os.name=='nt' else 'clear')


def init():
    """ Инициализация """
    ...
    

def check_commands_type(commands):
    if not (isinstance(commands, dict)
            and all(isinstance(k, str) and isinstance(v, tuple) for k, v in commands.items())
            and all(isinstance(v[0], Callable) and isinstance(v[1], list) and isinstance(v[2], str) 
                    for v in commands.values())
            ):
        raise TypeError('COMMANDS type not dict[str, tuple[Callable, str]]')


def draw_substate(title: str):
    """ Отрисовка временного шага TUI """
    cls()  # Очистка экрана
    x, y = shutil.get_terminal_size((80, 20))
    # Размеры линий
    equ = (x - len(title) - 3) // 2
    eqc = int(not(x % 2))
    # Линия с подписью
    print(f'{Fore.GREEN}{'=' * equ} {title} {'=' * equ}{'=' * eqc}{Style.RESET_ALL}')
    

def draw_state(title: str, 
          commands: dict[str, tuple[Callable, list, str]], 
          caption_up: str='',
          caption_down: str=''):
    """ Отрисовка TUI """
    check_commands_type(commands)
    
    cls()  # Очистка экрана
    x, y = shutil.get_terminal_size((80, 20))
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
        f'{Fore.CYAN}{key}{' ' if commands else ''}{' '.join(commands[key][1])}{Style.RESET_ALL} - {commands[key][2]} ' 
        for key in commands
    ]
    # Расчёт размера колонн
    com_len = [
        len(key) + len(commands[key][2]) + bool(commands) + len(' '.join(commands[key][1])) + 4 
        for key in commands
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


def next_state(commands: dict[str, tuple[Callable, list, str]]):
    """ Приём комманд """
    check_commands_type(commands)
    
    while True:
        try:
            r = input('>>> ').split()
            if r:
                if r[0] in commands:
                    if len(r) == 1:
                        commands[r[0]][0]()
                    else:
                        commands[r[0]][0](*r[1:])
        except (EOFError) as e:
            pass
        except (KeyboardInterrupt) as e:
            exit(0)
            
            
def input_bool() -> bool:
    """ Ввод bool """
    
    while True:
        try:
            r = input('[y/n] > ')
            if r == 'y':
                return True
            elif r == 'n':
                return False
        except (EOFError) as e:
            pass
        except (KeyboardInterrupt) as e:
            exit(0)