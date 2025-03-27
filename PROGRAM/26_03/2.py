import sqlite3

create_query = """
CREATE TABLE city (
    [номер п/п]         INTEGER PRIMARY KEY AUTOINCREMENT,
    [название города]   TEXT
);
"""

PATH = 'city.db'

cities = [
    ("Москва",),
    ("Санкт-Петербург",),
    ("Новосибирск",),
    ("Екатеринбург",),
    ("Казань",),
    ("Нижний Новгород",),
    ("Челябинск",),
    ("Самара",),
    ("Омск",),
    ("Ростов-на-Дону",),
    ("Уфа",),
    ("Красноярск",),
    ("Пермь",),
    ("Воронеж",),
    ("Волгоград",),
    ("Краснодар",),
    ("Саратов",),
    ("Тюмень",),
    ("Тольятти",),
    ("Ижевск",),
    ("Вологда",)
]

try:
    connection = sqlite3.connect(PATH)
    cursor = connection.cursor()
    print(f'Подключено к {PATH}')
    cursor.execute('SELECT sqlite_version();')
    print('Версия базы данных:', cursor.fetchone()[0])
    
    try:
        cursor.execute(create_query)
        print('Таблица создана')
    except sqlite3.Error as e:
        print(f"Таблица уже существует: {e}")
    
    cursor.executemany('INSERT INTO city ([название города]) VALUES (?)', cities)
    print(f"Добавлено {len(cities)} городов")
    
    cursor.execute('SELECT ([название города]) FROM city')
    
    print('Города:')
    print(', '.join(x[0] for x in cursor.fetchall()))
    
    cursor.close()
except sqlite3.Error as e:
    print("Ошибка при подключении к SQLite", e)
finally:
    if (connection):
        connection.commit()
        connection.close()
        print(f'Отключено от {PATH}')