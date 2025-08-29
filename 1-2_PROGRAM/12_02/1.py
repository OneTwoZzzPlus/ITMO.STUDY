from Input import Input


class Progression:
    def __init__(self, a0, d):
        self.a0 = a0
        self.d = d

    def geometric(self, n):
        return [self.a0 * self.d ** (i - 1) for i in range(1, n + 1)]

    def arithmetic(self, n):
        return [self.a0 + self.d * (i - 1) for i in range(1, n + 1)]


def main():
    a0 = Input('Элемент A0').float()
    d = Input('Коэффициент d').float()
    n = Input('n').natural()
    p = Progression(a0, d)
    print(p.geometric(n))
    print(p.arithmetic(n))


if __name__ == "__main__":
    main()
