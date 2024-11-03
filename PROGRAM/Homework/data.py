import csv
import dtf
import logging


# Размеры и формат данных
PRODUCT_NAME_LEN = 40
PRODUCT_TYPE_LEN = 40
PRODUCT_COST_MAX = 4_294_967_296 # COST.00 x100
DELIMITER = ','
LINETERMINATOR = '\r'

# Хранилище данных
current_path = ''
# ID | NAME | COST*100 | TYPE | UTC_TIME
data: list[tuple[int, str, int, str, int]] = None

# Индексы
index_eq: list[int] = []  # Сопоставление индексов индексаторов и данных
index_cost: dict[int, list[int]] = {}  # Индексатор по цене
index_type: dict[str, list[int]] = {}    # Индексатор по категории
index_date: dict[int, list[int]] = {}    # Индексатор по дате

# Доступность
available = lambda: data is not None

# Для отображения
display_cost = lambda x: f"{x:.2f}"
display_row = lambda x: (str(x[0]), x[1], display_cost(x[2]), x[3], dtf.display_utc(x[4]))


def _validate_product(index: int, pname, pcost, ptype, pdate):
    """ Преобразование корректных данных в продукт O(1) """
    try:
        # Название
        product_name = str(pname)
        if len(product_name) >= PRODUCT_NAME_LEN:
            raise TypeError(f"длина названия превышает {PRODUCT_NAME_LEN}")
        # Цена
        product_cost = int(pcost)
        if product_cost <= 0:
            raise TypeError(f"цена не положительная!")
        if product_cost >= PRODUCT_COST_MAX:
            raise TypeError(f"цена превышает {PRODUCT_COST_MAX}!")
        # Категория
        product_type = str(ptype)
        if len(product_type) >= PRODUCT_TYPE_LEN:
            raise ValueError(f"длина названия превышает {PRODUCT_NAME_LEN}")
        # Дата
        product_date = dtf.correct(int(pdate))
        if product_date <= 0 or product_date >= dtf.MAX_DATE:
            raise TypeError
        return (index, product_name, product_cost, product_type, product_date)
    except (TypeError, ValueError) as e:
        logging.info(f"Проигнорировано, т.к. {e}: {(pname, pcost, ptype, pdate)}")
        return None


def _add_product(pname, pcost, ptype, pdate):
    """ Добавление продукта из данных O(1) """
    global data
    index_id = len(data)
    xv = _validate_product(index_id, pname, pcost, ptype, pdate)
    if xv is not None:
        data.append(xv)
        # Индексируем
        index_eq.append(index_id)
        for value, indexer in zip(xv[2:5], [index_cost, index_type, index_date]):
            indexer.setdefault(value, []).append(index_id)
        

def _add_row_as_product(x: list):
    """ Добавление продукта из строки файла O(1) """
    if len(x) == 4:
        _add_product(*x)
    else:
        logging.info(f"Строка проигнорировано, т.к. разделителей '{DELIMITER}' слишком"\
                     f" {"МНОГО" if len(x) > 4 else "МАЛО"}: {x}")
    

def load_file(path: str='base.csv') -> bool:
    """ Загрузить коллекцию из файла O(n) """
    global data, current_path, index_cost, index_type, index_date, index_eq
    try:
        # Читаем файл
        file = open(path, 'r', encoding='utf-8')
        file_reader  = csv.reader(file, delimiter=DELIMITER, lineterminator=LINETERMINATOR)
        current_path = path
        # Очищаем место хранение данных и индексаторы
        data = []
        index_eq = []
        index_cost, index_type, index_date = {}, {}, {}
        # Построчно читааем записи
        for x in file_reader:
            _add_row_as_product(x)
        # Закрываем файл 
        file.close()
        return True
    except FileNotFoundError:
        # Создаём файл, если его не существует
        logging.info(f"Создаём файл {path}")
        open(path, 'w', encoding='utf-8')
        return load_file(path)
    except PermissionError:
        return False
        

def save_file(path: str=None) -> bool:
    """ Сохранить коллекцию в файл O(n) """
    global data, current_path
    if path is None:
        path = current_path
    # Не сохранять, если база не загружена
    if not available():
        return False
    try:
        # Открываем файл для записи
        file = open(path, 'w', encoding='utf-8')
        file_writer = csv.writer(file, delimiter=DELIMITER, lineterminator=LINETERMINATOR)
        current_path = path
        # Построчно записываем
        for x in data:
            # Если запись не удалена
            if x is not None:
                try:
                    file_writer.writerow(list(x[1:]))
                except Exception as e:
                    logging.warning(f"Неожиданная ошибка '{e}' при записи продукта {x}")
        # Закрываем файл
        file.close()
        return True
    except PermissionError:
        return False
    

def add_product(product_name: str, product_cost: float, product_type: str, product_date: dtf.date):
    """ Добавление продукта O(1) """
    _add_product(
        product_name, int(product_cost * 100), 
        product_type, dtf.datetime_to_utc(product_date)
    )


def remove_product(index: int) -> bool:
    global data, index_cost, index_type, index_date, index_eq
    # Проверяем существование записи
    if not 0 <= index < len(data):
        return False
    if data[index_eq[index]] is None:
        return False
    # Получаем запись
    i, _, pc, pt, pd = data[index_eq[index]]
    # Удаляем (заменяем на None) запись
    data[index_eq[index]] = None
    # Удаляем индекс из индексаторов
    for value, indexer in zip([pc, pt, pd], [index_cost, index_type, index_date]): 
        try:
            indexer[value].remove(index)
            if not indexer[value]:
                del indexer[value]
        except:
            pass
    return True
    

def get_list(count: int=None, start: int=0):
    """ Получение списка продуктов (iterator по O(1)) """
    if count is None:
        count = len(data)
    if start < len(data):
        for x in data[start:min(start + count + 1, len(data))]:
            if x is not None:
                yield display_row(x)
        

def empty_list_date(dt: dtf.date):
    """ Проверка на пустоту результата поиска по дате O(1) """
    return dtf.datetime_to_utc(dt) not in index_date


def get_list_date(dt: dtf.date):
    """ Поиск по дате (iterator по O(1)) """
    for i in index_date[dtf.datetime_to_utc(dt)]:
        if data[index_eq[i]] is not None:
            yield display_row(data[index_eq[i]])
        
        
def empty_list_type(t: str):
    """ Проверка на пустоту результата поиска по категории O(1) """
    return t not in index_type


def get_list_type(t: str):
    """ Поиск по категории (iterator по O(1)) """
    for i in index_type[t]:
        if data[index_eq[i]] is not None:
            yield display_row(data[index_eq[i]])
        
        
def sort_cost(inc: bool):
    """ Сортировка по возрастанию(inc=True) / убыванию(inc=False) стоимости O(n*logn + n) """
    data.sort(key=lambda x: 0 if x is None else x[2], reverse=not(inc))
    # Восстанавливаем индексацию через index_eq
    i = 0
    for p in data:
        if p is not None:
            index_eq[p[0]] = i
        i += 1
