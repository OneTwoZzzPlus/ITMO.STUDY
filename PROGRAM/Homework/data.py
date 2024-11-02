import csv
import datetime

# Данные
current_path = ''
data: list[tuple[int, str, float, str, int]] = None
index_eq: list[int] = []
DELIMITER = ','
LINETERMINATOR = '\r'

# Индексы
index_cost: dict[float, list[int]] = {}
index_type: dict[str, list[int]] = {}
index_date: dict[int, list[int]] = {}

# Доступность
available = lambda: data is not None

# Размеры данных в коллекции
PRODUCT_NAME_LEN = 40
PRODUCT_TYPE_LEN = 40
PRODUCT_COST_MAX = 4_294_967_296 # COST.00 x100
PRODUCT_DATE_MAX = 32503669200

# Работа с датами
time_display_utc = lambda x: time_utc_to_datetime(x).strftime('%d.%m.%y')
time_display_datatime = lambda x: x.strftime('%d.%m.%y')

def time_utc_to_datetime(x: datetime.datetime):
    y = datetime.datetime.fromtimestamp(x)
    return datetime.datetime(y.year, y.month, y.day)

def time_datetime_to_utc(x: datetime.datetime):
    y = datetime.datetime(x.year, x.month, x.day)
    return int(x.timestamp())

time_utc = lambda x: time_datetime_to_utc(time_utc_to_datetime(x))

# Преобразование записи в строку
display_row = lambda x: (str(x[0]), x[1], str(x[2]), x[3], time_display_utc(x[4]))

def _encode_row(index: int, row: list[str]):
    """ Преобразуем строку из файла в запись о продукте """
    try:
        product_name = str(row[0])
        if len(product_name) >= PRODUCT_NAME_LEN:
            raise ValueError
        product_cost = int(row[1])
        if product_cost <= 0 or product_cost >= PRODUCT_COST_MAX:
            raise ValueError
        product_cost = product_cost / 100
        product_type = str(row[2])
        if len(product_type) >= PRODUCT_TYPE_LEN:
            raise ValueError
        product_date = time_utc(int(row[3]))
        if product_date <= 0 or product_date >= PRODUCT_DATE_MAX:
            raise ValueError
        
        return (index, product_name, product_cost, product_type, product_date)
    except (IndexError, TypeError, ValueError) as e:
        print(e)
        return None


def _decode_row(row: tuple[int, str, int, str, datetime.datetime]):
    """ Преобразуем запись о продукте в строку из файла """
    try:
        return [
            row[1],
            str(int(row[2] * 100)),
            row[3],
            str(row[4])
        ]        
    except (IndexError, TypeError, ValueError) as e:
        print(e)
        return None
      

def _add_product(x: list[str] ):
    """ Добавление продукта из строки """
    global data
    index_id = len(data)
    xv = _encode_row(index_id, x)
    if xv is not None:
        data.append(xv)
        # Индексируем
        index_eq.append(index_id)
        index_cost.setdefault(xv[2], []).append(index_id)
        index_type.setdefault(xv[3], []).append(index_id)
        index_date.setdefault(xv[4], []).append(index_id)
    else:
        print("Некорректная запись проигнорирована:", x)
    

def load_file(path: str='base.txt') -> bool:
    """ Загрузить коллекцию из файла """
    global data, current_path, index_cost, index_type, index_date, index_eq
    try:
        file = open(path, 'r', encoding='utf-8')
        file_reader  = csv.reader(file, delimiter=DELIMITER, lineterminator=LINETERMINATOR)
        current_path = path
        data = []
        index_eq = []
        index_cost, index_type, index_date = {}, {}, {}
        
        for x in file_reader:
            _add_product(x)
            
        file.close()
        return True
    except FileNotFoundError:
        open(path, 'w', encoding='utf-8')
        return load_file(path)
    except PermissionError:
        return False
        

def save_file(path: str=None) -> bool:
    """ Сохранить коллекцию в файл """
    global data, current_path
    if path is None:
        path = current_path
    try:
        if available():
            file = open(path, 'w', encoding='utf-8')
            current_path = path
            file_writer = csv.writer(file, delimiter=DELIMITER, lineterminator=LINETERMINATOR)
            for x in data:
                if x is None:
                    continue
                xv = _decode_row(x)
                if xv is not None:
                    file_writer.writerow(xv)
                else:
                    print("Ошибка сохранения:", x)
            file.close()
            return True
    except PermissionError:
        return False
    

def add_product(product_name: str, product_cost: float, product_type: str, product_date: datetime.datetime):
    """ Добавление продукта """
    _add_product([
        product_name, str(int(product_cost * 100)), product_type,
        time_datetime_to_utc(product_date)
    ])


def remove_product(index: int) -> bool:
    global data, index_cost, index_date, index_type, index_eq
    if not 0 <= index < len(data):
        return False
    if data[index_eq[index]] is None:
        return False
    i, pname, pcost, ptype, pdate = data[index_eq[index]]
    data[i] = None
    try:
        index_cost[pcost].remove(index)
        if not index_cost[pcost]:
            del index_cost[pcost]
    except:
        pass
    try:
        index_type[ptype].remove(index)
        if not index_type[ptype]:
            del index_type[ptype]
    except:
        pass
    try:
        index_date[pdate].remove(index)
        if not index_date[pdate]:
            del index_date[pdate]
    except:
        pass
    return True
    

def get_list(count: int=None, start: int=0):
    """ Получение списка продуктов """
    if count is None:
        count = len(data)
    if start < len(data):
        for x in data[start:min(start + count + 1, len(data))]:
            if x is not None:
                yield display_row(x)
        

def empty_list_date(dt: datetime):
    return time_datetime_to_utc(dt) not in index_date


def get_list_date(dt: datetime):
    for i in index_date[time_datetime_to_utc(dt)]:
        if data[index_eq[i]] is not None:
            yield display_row(data[index_eq[i]])
        
        
def empty_list_type(t: str):
    return t not in index_type


def get_list_type(t: str):
    for i in index_type[t]:
        if data[index_eq[i]] is not None:
            yield display_row(data[index_eq[i]])
        
        
def sort_cost(inc: bool):
    data.sort(key=lambda x: 0 if x is None else x[2], reverse=not(inc))
    i = 0
    for p in data:
        if p is not None:
            index_eq[p[0]] = i
        i += 1
