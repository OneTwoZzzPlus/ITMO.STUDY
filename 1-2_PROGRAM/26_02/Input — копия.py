class Input:
    def __init__(self, s, breaker='q'):
        self.s = s
        self.breaker = breaker

    def inp(self, func):
        while True:
            try:
                r = input(f'{self.s} > ')
                if r == self.breaker:
                    raise KeyboardInterrupt()
                return func(r)
            except ValueError:
                print('Некорректный ввод, попробуйте ещё раз')
            except KeyboardInterrupt:
                exit(0)

    @staticmethod
    def _natural(x):
        x = int(x)
        if x > 0:
            return x
        else:
            raise ValueError()

    def float(self):
        return self.inp(float)

    def int(self):
        return self.inp(int)

    def natural(self):
        return self.inp(self._natural)

    def str(self):
        return self.inp(str)


if __name__ == "__main__":
    while True:
        Input('LOL').natural()