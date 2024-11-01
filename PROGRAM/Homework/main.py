import tui
import data

import datetime
from colorama import Fore, Back, Style
CR = Style.RESET_ALL 

  
def not_implemented(*args):
    print(f"Не реализовано =)")
    if args:
        print(f'Кстати, ваши аргументы:', args)
   
            
def substate_qsave():
    if data.available():
        print(f"Сохранить изменения в: {data.current_path}?")
        if tui.input_bool():
            data.save_file()
      
        
def state_exit(*args):
    substate_qsave()
    exit(0)
    
        
def state_open_base(*args):
    substate_qsave()
    
    if len(args) == 0:
        data.load_file()
    else:
        data.load_file(' '.join(args))
        
    if not data.available():
        print(f"Нет доступа к {data.current_path}")
    return state_main, data.available()
    
    
def state_save_base(*args):
    if len(args) == 0:
        print("Сохранено!" if data.save_file() else "Нет доступа к записи!")
        return state_main, False
    else:
        print(f"Сохранить изменения в новый файл: {' '.join(args)}?")
        if tui.input_bool():
            print("Сохранено!" if data.save_file(' '.join(args)) else "Нет доступа к записи!")
            return state_main
        
    
def state_main(clear: bool=True, *args):
    if data.available():
        caption = f'Путь к данным: {data.current_path}'
        commands = {
            'main': (state_main, [], 'главное меню'),
            'open': (state_open_base, ['[path]'], 'открыть новый файл'),
            'save': (state_save_base, ['[path]'], 'сохранить файл'),
            'exit': (state_exit, [], 'выход из приложения'),
            
            'add': (state_add, [], 'добавить продукт'),
            'list': (state_list, [], 'просмотреть коллекцию'),
            'date': (not_implemented, [''], 'просмотреть по дате'),
            'type': (not_implemented, [], 'просмотреть по категории'),
            'up': (not_implemented, [], 'сортировать по возрастанию стоимости'),
            'down': (not_implemented, [], 'сортировать по убыванию стоимости'),
            'remove': (not_implemented, [], 'удалить продукт'),
        }
    else:
        caption = "Откройте файл"
        commands = {
            'open': (state_open_base, ['[path]'], 'открыть файл'),
            'exit': (state_exit, [], 'выход из приложения')
        }
    
    tui.set_commands(commands) 
    if clear:
        tui.draw_state('Главное меню', caption_down=caption)
    


def state_list(*args):
    if len(data.data) == 0:
        print("Коллекция пуста! Добавьте туда что-нибудь")
        return state_main, False
    
    commands = {
            'main': (state_main, [], 'главное меню'),
            'exit': (state_exit, [], 'выход из приложения'),
    }
    tui.set_commands(commands)
    tui.draw_state('Коллекция')

    for x in data.get_list():
        print(x)


def state_add(*args):
    tui.draw_substate('Добавление')
    
    print(f"Введите {Fore.GREEN}название{CR} продукта (до {Fore.CYAN}{data.PRODUCT_NAME_LEN}{CR} символов)")
    product_name = tui.input_str(data.PRODUCT_NAME_LEN)
    
    print(f"Введите {Fore.GREEN}стоимость{CR} продукта (до {Fore.CYAN}2{CR} знаков после точки)")
    product_cost = tui.input_float(data.PRODUCT_COST_MAX, 2)

    print(f"Введите {Fore.GREEN}категорию{CR} продукта (до {Fore.CYAN}{data.PRODUCT_TYPE_LEN}{CR} символов)")
    product_type = tui.input_str(data.PRODUCT_TYPE_LEN)
    
    now = data.time_display_datatime(datetime.datetime.now())
    print(f"Нажмите {Fore.CYAN}enter{CR} для {Fore.CYAN}{now}{CR} или введите другую {Fore.GREEN}дату{CR}")
    product_date = tui.input_date()
    
    tui.draw_substate('Подтверждение')
    print(f"Сохранить продукт?")
    print(f"Название:\t{Fore.CYAN}{product_name}{CR}")
    print(f"Стоимость:\t{Fore.CYAN}{product_cost}{CR}")
    print(f"Категория:\t{Fore.CYAN}{product_type}{CR}")
    print(f"Дата:\t\t{Fore.CYAN}{data.time_display_datatime(product_date)}{CR}")
    
    if tui.input_bool():
        data.add_product(product_name, product_cost, product_type, product_date)
    return state_main
    

if __name__ == "__main__":
    
    # print('Программа для контроля собственных денежных средств.')
    # try:
    #     input('Нажмите enter > ')
    # except (EOFError, KeyboardInterrupt) as e:
    #     exit(0)
        
    tui.run(state_main)
