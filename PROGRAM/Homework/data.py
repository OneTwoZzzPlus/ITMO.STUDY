import csv

current_path = ''
data = None
available = lambda: data is not None

def load_file(path: str='base.txt') -> bool:
    global data, current_path
    try:
        file = open(path, 'r', encoding='utf-8')
        current_path = path
        file_reader  = csv.reader(file, delimiter = ",", lineterminator="\r")
        
        # TODO проверка корректности записей
        data = [x for x in file_reader] 
        
        file.close()
        return True
    except FileNotFoundError:
        open(path, 'w', encoding='utf-8')
        return load_file(path)
    except PermissionError:
        return False
        

def save_file(path: str=None) -> bool:
    global data, current_path
    if path is None:
        path = current_path
    try:
        if available():
            file = open(path, 'w', encoding='utf-8')
            current_path = path
            file_writer = csv.writer(file, delimiter = ",", lineterminator="\r")
            file_writer.writerows(data)
            file.close()
            return True
    except PermissionError:
        return False
    