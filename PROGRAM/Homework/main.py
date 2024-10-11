import os
import shutil
import data
from colorama import init as colorama_init, Fore, Back, Style
colorama_init()


def state_start():
    print(data.title_start)
    state_help()
    try:
        input('Нажмите enter...')
    except (EOFError) as e:
        pass
    state_main()


def state_help():
    print(data.title_help)


def state_exit():
    exit(0)


def cls(title: str):
    os.system('cls' if os.name=='nt' else 'clear')
    x, y = shutil.get_terminal_size((80, 20))
    cnt = (x - len(title) - 2) // 2
    equ = '=' * cnt
    print(f'{Fore.GREEN}{equ} {title} {equ}{Style.RESET_ALL}')


def state_main():
    cls('Главное меню')
    commands = {
        'exit': state_exit,
        'main': state_main,
        'help': state_help
    }
    while True:
        try:
            r = input('>>> ')
            if r in commands:
                commands[r]()
        except (EOFError) as e:
            pass


if __name__ == "__main__":
    state_start()
