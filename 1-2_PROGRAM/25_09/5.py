def input_float(s: str, not_null=False) -> float:
    while True:
        r = input(s + ' > ')
        try:
            r = float(r)
            if not (not_null and r == 0):
                return r
            else:
                print('Делить на 0 нельзя!')
        except TypeError:
            pass


def input_operator(s: str) -> (str, bool):
    while True:
        r = input(s + ' > ')
        if r in ['+', '-', '*', '/', '^']:
            return r, r == '/'


def operation(a, operator, b):
    match operator:
        case '+':
            ret = a + b
        case '-':
            ret = a - b
        case '*':
            ret = a * b
        case '^':
            ret = a ** b
        case '/':
            ret = a / b
        case _:
            ret = 0
    return int(ret) if ret % 1 == 0 else ret


a_ = input_float('Первое число')
operator_, not_null_ = input_operator('Оператор')
b_ = input_float('Второе число', not_null_)

print(operation(a_, operator_, b_))
