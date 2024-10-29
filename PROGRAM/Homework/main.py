import tui
    

def state_main():
    commands = {
        'exit': (tui.state_exit, 'выход из приложения'),
        'main': (state_main, 'выход в главное меню')
    }
    tui.state('Главное меню', '', commands)


if __name__ == "__main__":
    tui.start()
    state_main()
