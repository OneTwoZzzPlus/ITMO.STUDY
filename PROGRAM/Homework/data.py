import csv

current_path = ''
data = None

def load_file(path: str='base.txt') -> bool:
    global data, current_path
    try:
        file = open(path, 'r', encoding='utf-8')
        current_path = path
        file_reader  = csv.reader(file, delimiter = ",")
        
        # TODO проверка корректности записей
        data = [x for x in file_reader] 
        
        file.close()
    except FileNotFoundError:
        open(path, 'w', encoding='utf-8')
        return load_file(path)
    except PermissionError:
        return False
        
