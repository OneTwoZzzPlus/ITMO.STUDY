import tui
import data
    
def state_open_base():
    state_main()
    
    
    
def state_main():
    commands = {
        'main': (state_main, [''], 'выход в главное меню'),
        'exit': (tui.state_exit, [''], 'выход из приложения'),
        'open': (state_open_base, ['[path]'], 'открыть файл')
    }
    caption = f'Путь к данным: {1}' if data.current_path != '' else ''
    tui.draw_state('Главное меню', commands, caption_down=caption)
    tui.next_state(commands)



if __name__ == "__main__":
    
    print('Программа для контроля собственных денежных средств.')
    try:
        input('Нажмите enter > ')
    except (EOFError, KeyboardInterrupt) as e:
        exit(0)
        
    tui.init()
    state_main()
