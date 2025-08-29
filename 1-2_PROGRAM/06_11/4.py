def input_login():
    while True:
        try:
            s = input("Введите логин до 20 символов > ")
            if len(s) >= 20:
                raise ValueError
            return s
        except ValueError as e:
            print(e)


def input_bool():
    while True:
        try:
            s = input("[+/-] > ")
            if s == '+':
                return True
            elif s == '-':
                return False
            print("Введите + или -")
        except ValueError as e:
            print(e)


logins = {"root", "ivan"}

print("Добро пожаловать!")
if input_login() in logins:
    print("Доступ разрешён")
else:
    print("Хотите добавить новый логин?")
    if input_bool():
        while (lg := input_login()) in logins:
            print("Такой логин уже существует")
        logins.add(lg)
        print("Логин добавлен, доступ разрешён")
    else:
        print("Доступ запрещён!")
