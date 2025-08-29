def input_name() -> str:
    while True:
        try:
            s = input("Введите имя > ")
            if len(s) < 40 and 1040 <= ord(s[0]) <= 1071 and all(1072 <= ord(y) <= 1103 for y in s[1:]):
                return s
        except (ValueError, OverflowError):
            pass


def input_long() -> int:
    while True:
        try:
            n = int(input("Введите рост > "))
            if 100 <= n <= 300:
                return n
        except (ValueError, OverflowError):
            pass


def input_command() -> bool:
    while True:
        try:
            print('Команды: "все построены" и пустая строка')
            s = input("Введите команду > ")
            if s == '':
                return True
            if s.lower() == "все построены":
                return False
        except (ValueError, OverflowError):
            pass


line = [('Вася', 170), ('Петя', 176), ('Ваня', 187), ('Саша', 185)]


def insert_soldier(nm: str, lg: int):
    global line
    line.append((None, lg))
    line.sort(key=lambda x: x[1])
    num = None
    for i in range(len(line)):
        if line[i][0] is None:
            line[i] = (nm, lg)
            num = i + 1
    for nam, lon in line:
        print(f"{nam} - {lon}")
    print("Порядковый номер новичка:", num)


while input_command():
    insert_soldier(input_name(), input_long())
for name, long in line:
    print(f"{name} - {long}")
