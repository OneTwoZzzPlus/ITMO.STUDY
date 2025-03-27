import sqlite3
PATH = 'music.db'


try:
    connection = sqlite3.connect(PATH)
    cursor = connection.cursor()
    print(f'Подключено к {PATH}')

    cursor.execute('SELECT * FROM tMusician')
    for i, name, age, gender in cursor.fetchall():
        print(f'{i}. {name}: {"группа" if age is None else f'{age}, {"муж" if gender else "жен"}'}')
    
    song = 'Лесник'
    cursor.execute(f'''
        SELECT *
        FROM tComment
        JOIN tSong ON tComment.id_Song = tSong.id
        WHERE tSong.title = '{song}';
    ''')
    res = cursor.fetchall()
    print(res)
    cursor.close()
    
except sqlite3.Error as e:
    print("Ошибка при подключении к SQLite", e)
finally:
    if (connection):
        connection.commit()
        connection.close()
        print(f'Отключено от {PATH}')