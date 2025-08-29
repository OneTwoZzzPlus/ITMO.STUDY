def input_natural(title: str = ""):
    s = input(title)
    f = None
    while f is None:
        try:
            if s.strip().isdigit():
                f = int(s.strip())
                if f == 0:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            s = input("Только натуральные числа: ")
            f = None
    return f


def input_int(title: str = ""):
    s = input(title)
    f = None
    while f is None:
        try:
            f = int(s.strip())
        except ValueError:
            s = input("Только целые числа: ")
            f = None
    return f


def input_float(title: str = ""):
    s = input(title)
    f = None
    while f is None:
        try:
            f = float(s.strip())
        except ValueError:
            s = input("Только рациональные числа: ")
            f = None
    return f
