from Input import Input


class Triangle:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Неправильные стороны треугольника =(")

    def square(self) -> float:
        p = (self.a + self.b + self.c) / 2
        s = (p * (p - self.a) * (p - self.b) * (p - self.c))**0.5
        return s


def main():
    a = Input('a').float()
    b = Input('b').float()
    c = Input('c').float()
    triangle = Triangle(a, b, c)
    print('Площадь треугольника =', triangle.square())


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(e)
