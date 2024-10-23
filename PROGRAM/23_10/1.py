def input_str():
    while True:
        try:
            inp = input('Строка >>> ')
            if inp == '':
                return None
            if len(inp) > 200:
                raise Exception('слишком длинная строка')
            if any(x in inp for x in '\n\r\t1234567890@#№%*'):
                raise TypeError
            inp_lower = inp.lower()
            if any(x not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-;:,.!? ' for x in inp_lower):
                raise TypeError
            for i in range(len(inp) - 1, -1, -1):
                if inp_lower[i] in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
                    if inp_lower[i + 1:] in ['', '.', '!', '"', ',', '...', ':', ')', '?']:
                        return inp_lower[i]
            print('Неподходящая строка')
        except (TypeError, EOFError, ValueError):
            print('Некорректный ввод: неправильные символы')


product = ""
while (inp := input_str()) != None:
    product += inp
if len(product) >= 2:
    product = product[0].upper() + product[1:]
print(product)