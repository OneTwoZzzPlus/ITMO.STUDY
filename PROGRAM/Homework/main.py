import tui
import data

import datetime
    
    
def not_implemented(*args):
    print(f"Не реализовано =)")
    if args:
        print(f'Кстати, ваши аргументы:', args)
   
            
def substate_qsave():
    if data.available():
        print(f"Сохранить изменения в: {data.current_path}?")
        if tui.input_bool():
            data.save_file()
        
    
def state_open_base(*args):
    substate_qsave()
    
    if len(args) == 0:
        data.load_file()
    else:
        data.load_file(' '.join(args))
        
    if not data.available():
        print(f"Нет доступа к {data.current_path}")
    return state_main(data.available())
    
    
def state_save_base(*args):
    if len(args) == 0:
        print("Сохранено!" if data.save_file() else "Нет доступа к записи!")
        return state_main(False)
    else:
        print(f"Сохранить изменения в новый файл: {' '.join(args)}?")
        if tui.input_bool():
            print("Сохранено!" if data.save_file(' '.join(args)) else "Нет доступа к записи!")
            return state_main()


def state_exit(*args):
    substate_qsave()
    exit(0)
        
    
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
        
        
    if clear:
        tui.draw_state('Главное меню', commands, caption_down=caption)
    return tui.next_state(commands)


def state_list(*args):
    if len(data.data) == 0:
        print("Коллекция пуста! Добавьте туда что-нибудь")
        return state_main(False)
    
    commands = {
            'main': (state_main, [], 'главное меню'),
            'exit': (state_exit, [], 'выход из приложения'),
    }
    tui.draw_state('Коллекция', commands)

    for x in data.get_list():
        print(x)
        
    return tui.next_state(commands)


def state_add(*args):
    now = datetime.datetime(
        datetime.datetime.now().year, 
        datetime.datetime.now().month, 
        datetime.datetime.now().day
    )
    
    product_name, product_cost, product_type = 'lol', 1.0, 'lol1', now

    
    tui.draw_substate('Добавление')
    
    if tui.input_bool():
        ... # TODO tui.input_[type]
    
    tui.draw_substate('Подтверждение')
    print(f"Сохранить: {product_name} {product_cost} {product_type} {product_date}?")
    if tui.input_bool():
        data.add_product(product_name, product_cost, product_type, product_date)
    return state_main()
    

if __name__ == "__main__":
    
    print('Программа для контроля собственных денежных средств.')
    try:
        input('Нажмите enter > ')
    except (EOFError, KeyboardInterrupt) as e:
        exit(0)
        
    tui.init()
    state_main()
