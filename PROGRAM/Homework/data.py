import csv
import datetime

current_path = ''
data: list[tuple[int, str, float, str, int]] = None
index_cost: dict[float, list[int]] = {}
index_type: dict[str, list[int]] = {}
index_date: dict[int, list[int]] = {}
available = lambda: data is not None


time_utc_to_datetime = lambda x: datetime.datetime.fromtimestamp(x)
time_display_utc = lambda x: time_utc_to_datetime(x).strftime('%m/%d/%y')
time_datetime_to_utc = lambda x: int(x.timestamp())

display_row = lambda x: (str(x[0]), x[1], str(x[2]), x[3], time_display_utc(x[4]))

def _encode_row(row: list[str]):
    try:
        product_name = str(row[0])
        if len(product_name) >= 40:
            raise ValueError
        product_cost = int(row[1])
        if product_cost <= 0 or product_cost >= 4_294_967_296:
            raise ValueError
        product_cost = product_cost / 100
        product_type = str(row[2])
        if len(product_type) >= 40:
            raise ValueError
        product_date = int(row[3])
        if product_cost <= 0 or product_cost >= 32503669200:
            raise ValueError
        return (-1, product_name, product_cost, product_type, product_date)
    except (IndexError, TypeError, ValueError) as e:
        print(e)
        return None


def _decode_row(row: tuple[int, str, int, str, datetime.datetime]):
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
    global data
    xv = _encode_row(x)
    if xv is not None:
        index_id = len(data)
        data.append(xv)
        index_cost.setdefault(xv[2], []).append(index_id)
        index_type.setdefault(xv[3], []).append(index_id)
        index_date.setdefault(xv[4], []).append(index_id)
    else:
        print("Некорректная запись проигнорирована:", x)
    

def load_file(path: str='base.txt') -> bool:
    global data, current_path, index_cost, index_type, index_date
    try:
        file = open(path, 'r', encoding='utf-8')
        file_reader  = csv.reader(file, delimiter = ",", lineterminator="\r")
        current_path = path
        data = []
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
    global data, current_path
    if path is None:
        path = current_path
    try:
        if available():
            file = open(path, 'w', encoding='utf-8')
            current_path = path
            file_writer = csv.writer(file, delimiter = ",", lineterminator="\r")
            for x in data:
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
    _add_product([
        product_name, str(int(product_cost * 100)), product_type,
        time_datetime_to_utc(product_date)
    ])


def get_list(count: int=None, start: int=0):
    if count is None:
        count = len(data)
    if start < len(data):
        for x in data[start:min(start + count + 1, len(data))]:
            yield display_row(x)
        
        
def get_date(dt: datetime):
    for i in index_date[time_datetime_to_utc(dt)]:
        yield display_row(data[i])
        

def get_type(t: str):
    for i in index_type[t]:
        yield display_row(data[i])
        
        
def get_type(t: str):
    for i in index_type[t]:
        yield display_row(data[i])