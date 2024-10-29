import os
import shutil
import text
from colorama import init as colorama_init, Fore, Back, Style
colorama_init()


state_exit = lambda: exit(0)
cls = lambda: os.system('cls' if os.name=='nt' else 'clear')


def start():
    print(f'{Fore.GREEN} {text.app_caption} {Style.RESET_ALL}')
    print(text.color_check)
    try:
        res = input(text.press_enter)
    except (EOFError, KeyboardInterrupt) as e:
        res = '0'
    if res != '':
        


def state(title: str, caption: str, commands):
    cls()
    
    x, y = shutil.get_terminal_size((80, 20))
    equ = '=' * ((x - len(title) - 2) // 2)
    print(f'{Fore.GREEN}{equ} {title} {equ}{Style.RESET_ALL}')
    
    while True:
        try:
            r = input('>>> ')
            if r in commands:
                commands[r][0]()
        except (EOFError) as e:
            pass
        except (KeyboardInterrupt) as e:
            exit(0)