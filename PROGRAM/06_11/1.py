while True:
    try:
        s = input("Введите ФИО > ")
        words = s.split()
        if len(words) != 3:
            raise ValueError("Введите 3 слова!")
        if not all(1040 <= ord(x[0]) <= 1071 and all(1072 <= ord(y) <= 1103 for y in x[1:]) for x in words):
            raise ValueError("Введите слова кириллицей, начиная с прописной буквы!")
        print(f"{words[0]} {words[1][0]}.{words[2][0]}.")
        break
    except ValueError as e:
        print(e)
