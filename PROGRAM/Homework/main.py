import tui
import data

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
            'exit': (state_exit, [], 'выход из приложения'),
            'main': (state_main, [], 'главное меню'),
            'open': (state_open_base, ['[path]'], 'открыть файл'),
            'save': (state_save_base, ['[path]'], 'сохранить файл'),
            'list': (state_list, [], 'просмотреть коллекцию'),
            'add': (state_add, [], 'добавить продукт'),
            'remove': (substate_remove, ['<id>'], 'удалить продукт'),
            'inc': (substate_inc, [], 'по возрастанию стоимости'),
            'dec': (substate_dec, [], 'по убыванию стоимости'),
            'help': (state_main, [], 'справка')
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
    

def substate_remove(*args):
    if len(args) == 1 and args[0].isnumeric():
        res = data.remove_product(int(args[0]))
        print("Удалено" if res else "Не удалено")
    

def substate_inc():
    data.sort_cost(True)
    print("Отсортировано по возрастанию цены")
    
    
def substate_dec():
    data.sort_cost(False)
    print("Отсортировано по убыванию цены")
    

def state_list(clear: bool=True, *args):
    if len(data.data) == 0:
        print("Коллекция пуста! Добавьте туда что-нибудь")
        return state_main, False
    
    commands = {
            'main': (state_main, [], 'главное меню'),
            'list': (state_list, [], 'просмотреть всю коллекцию'),
            'date': (state_list_date, ['[ДД.ММ.ГГ]'], 'просмотреть по дате'),
            'type': (state_list_type, ['<type>'], 'просмотреть по категории')
    }
    tui.set_commands(commands)
    if clear:
        tui.draw_state('Коллекция')

        for x in data.get_list():
            print(x)


def state_list_date(*args):
    if len(args) == 0:
        date = tui.now_date()
    elif len(args) == 1:
        date = tui.validate_date(args[0])
        if date is None:
            print("Неправильная дата!")
            return state_list, False
    else:
        print("Лишние аргументы!")
        return state_list, False

    if data.empty_list_date(date):
        print("На эту дату ничего нет!")
        return state_list, False

    tui.draw_state("Коллекция")
    for x in data.get_list_date(date):
        print(x)


def state_list_type(*args):
    if len(args) != 1:
        print("Должен быть ровно один аргумент")
        return state_list, False
    
    if data.empty_list_type(args[0]):
        print("В этой категории ничего нет!")
        return state_list, False

    tui.draw_state("Коллекция")
    for x in data.get_list_type(args[0]):
        print(x)
        

def state_add(*args):
    tui.draw_substate('Добавление')
    
    print(f"Введите {Fore.GREEN}название{CR} продукта (до {Fore.CYAN}{data.PRODUCT_NAME_LEN}{CR} символов)")
    product_name = tui.input_str(data.PRODUCT_NAME_LEN)
    
    print(f"Введите {Fore.GREEN}стоимость{CR} продукта (до {Fore.CYAN}2{CR} знаков после точки)")
    product_cost = tui.input_float(data.PRODUCT_COST_MAX, 2)

    print(f"Введите {Fore.GREEN}категорию{CR} продукта (до {Fore.CYAN}{data.PRODUCT_TYPE_LEN}{CR} символов)")
    product_type = tui.input_str(data.PRODUCT_TYPE_LEN)
    
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
