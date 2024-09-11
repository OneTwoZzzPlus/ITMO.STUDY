def input_int(title: str):
    s = input(title)
    f = None
    while f is None:
        try:
            f = int(s.strip())
        except ValueError:
            s = input("Неверный формат, попробуйте ещё раз: ")
    return f


def input_float(title: str, min = None, max = None, not_min = False, not_max = False):
    s = input(title)
    f = None
    while f is None:
        try:
            f = float(s.strip())
            if min is not None:
                if f < min:
                    raise ValueError
            if max is not None:
                if f > max:
                    raise ValueError
            if not_min:
                if f == min:
                    raise ValueError
            if not_max:
                if f == max:
                    raise ValueError
        except ValueError:
            s = input("Неверный формат, попробуйте ещё раз: ")
    return f