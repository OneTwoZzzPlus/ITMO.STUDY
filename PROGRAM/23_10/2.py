def input_cost(s: str):
    while True:
        try:
            inp = input(f'Цена для {s} >>> ')
            if len(inp) > 12:
                raise Exception('слишком длинная строка')
            inp = float(inp)
            if inp <= 0:
                raise Exception('отрицательная цена')
            if inp * 100 % 1 != 0:
                raise Exception('нельзя меньше копейки')
            return inp
        except (TypeError, EOFError, ValueError):
            print('Некорректный ввод: неправильные символы')
        except Exception as e:
            print('Некорректный ввод:', e)


def input_name(s: int):
    while True:
        try:
            inp = input(f'Продукт {s} >>> ')
            if len(inp) > 50:
                raise Exception('слишком длинная строка')
            if any(x in inp for x in ['\n', '\r', '\t']):
                raise TypeError
            inp = inp.replace(' ', '')
            return inp
        except (TypeError, EOFError, ValueError):
            print('Некорректный ввод: неправильные символы')
        except Exception as e:
            print('Некорректный ввод:', e)


product = []
while (inp := input_name(len(product) + 1)) != '':
    product.append(inp)

cost = []
for i in range(len(product)):
    cost.append(input_cost(f'{i + 1}. {product[i]}'))

price = [round(x*1.15, 2) for x in cost]
data = zip(product, cost, price)

print('\n===== РЕЗУЛЬТАТ ===== out2.txt =====\n')
with open('out2.txt', 'w', encoding='utf-8') as file:
    file.write('product\tcost\tprice\n')
    for x, y, z in data:
        s = f'{x}\t{y:.2f}\t{z:.2f}'
        print(s)
        file.write(f'{s}\n')
