import math

def input_int_list() -> list[int]:
    a = []
    print("Вводите целочисленные элементы массива")
    while True:
        try:
            s = input(" > ")
            if s == '' and len(a) > 0:
                return a
            a.append(int(s))
        except (ValueError, OverflowError):
            pass


def input_step(maximum: int) -> int:
    while True:
        try:
            n = int(input("Введите шаг > "))
            if abs(n) > maximum or n == 0:
                raise ValueError
            return n
        except (ValueError, OverflowError):
            pass


def iterate_list(a: list[int], step: int):
    return a[step:] + a[:step]


a1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
s1 = input_step(len(a1))
print(iterate_list(a1, s1))

a2 = input_int_list()
s2 = input_step(len(a2))
print(terate_list(a2, s2))

