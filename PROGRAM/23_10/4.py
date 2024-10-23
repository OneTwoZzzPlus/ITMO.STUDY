def input_float():
    while True:
        try:
            inp = input('>>> ')
            if inp == 'exit' or inp == '':
                return None
            return float(inp)
        except (TypeError, EOFError, ValueError):
            print('Некорректный ввод: неправильные символы')


lst = []
while (value := input_float()) != None:
    lst.append(value)
lst = [1.12 * x if x < 10 else (0.25 * x if x > 10 else 10) for x in lst]
lst.sort()
lst = [f'{round(x, 2):.2f}' for x in lst]

print('\n===== РЕЗУЛЬТАТ ===== out4.txt =====\n')
with open('out4.txt', 'w', encoding='utf-8') as file:
    for x in lst:
        print(x)
        file.write(x)
        file.write('\n')
