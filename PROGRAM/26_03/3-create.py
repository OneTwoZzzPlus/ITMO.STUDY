import sqlite3
PATH = 'music.db'

# Таблица tMusician
# True = мужской гендер
# В группах возраст и пол не указаны
musicians = [
    ("Король и Шут", None, None), 
    ("Кис-Кис", None, None),
    ("ZOLOTO", None, None),
    ("Дайте танк (!)", None, None),
    ("Женя Трофимов", 32, True),   
    ("Александр Пушной", 45, True),
    ("SLAVA SKRIPKA", 38, True)
]

# Таблица tSong
songs = [
    (1, "Лесник", "Один из самых известных хитов группы Король и Шут"),
    (1, "Ели мясо мужики", "Классическая песня в стиле хоррор-панк"),
    (2, "Молодость", "Энергичный трек от Кис-Кис"),
    (3, "Кобра", "Популярная песня ZOLOTO"),
    (4, "Грустная песня", "Хит от Дайте танк (!)"),
    (5, "Весна", "Лирическая композиция Жени Трофимова"),
    (6, "Профессор", "Юмористическая песня Александра Пушного"),
    (7, "Мальчик на девятке", "Хит от SLAVA SKRIPKA")
]

# Таблица tComment
comments = [
    ("Отличная песня, слушаю уже 10 лет!", 1, 1),
    ("Обожаю этот трек, такой энергичный!", 3, 3),
    ("Классика русского рока!", 1, 1),
    ("Очень душевно, спасибо за такую музыку!", 5, 5),
    ("Слушаю каждый день, не надоедает!", 1, 1),
    ("Лучшая песня этого исполнителя!", 4, 7),
    ("Как же это актуально звучит сейчас!", 2, 4)
]

def create():
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tMusician (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                canonicalName   TEXT,
                age             INTEGER,
                gender          BOOLEAN
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tSong (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                id_musician     INTEGER,
                title           TEXT,
                description     TEXT,
                FOREIGN KEY (id_musician) REFERENCES tMusician(id) ON DELETE RESTRICT
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tComment (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                textComm        TEXT,
                id_Musician     INTEGER,
                id_Song         INTEGER,
                FOREIGN KEY (id_Musician) REFERENCES tMusician(id) ON DELETE RESTRICT,
                FOREIGN KEY (id_Song) REFERENCES tSong(id) ON DELETE RESTRICT
            );
        """)
        connection.commit()
        print('База создана')
    except sqlite3.Error as e:
        print(f"Ошибка: {e}")

def fill():
    cursor.executemany('INSERT INTO tMusician (canonicalName, age, gender) VALUES (?, ?, ?)', musicians)
    cursor.executemany('INSERT INTO tSong (id_musician, title, description) VALUES (?, ?, ?)', songs)
    cursor.executemany('INSERT INTO tComment (textComm, id_Musician, id_Song) VALUES (?, ?, ?)', comments)
    connection.commit()
    print('База заполнена')


try:
    connection = sqlite3.connect(PATH)
    cursor = connection.cursor()
    print(f'Подключено к {PATH}')
    cursor.execute('SELECT sqlite_version();')
    print('Версия базы данных:', cursor.fetchone()[0])
    
    create()
    fill()
    
    cursor.execute('SELECT * FROM tMusician')
    print(cursor.fetchall())
    
    cursor.close()
except sqlite3.Error as e:
    print("Ошибка при подключении к SQLite", e)
finally:
    if (connection):
        connection.commit()
        connection.close()
        print(f'Отключено от {PATH}')