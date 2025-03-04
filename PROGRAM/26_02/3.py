from Input import Input


class Cat:
    _nickname: str
    _age: int
    _wool_length: str

    def __init__(self, nickname, age):
        self.nickname, self.age = nickname, age

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, value):
        self._nickname = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: int):
        if not 0 <= value <= 19:
            raise ValueError("Неправильный возраст")
        self._age = value

    @property
    def wool_length(self):
        return self._wool_length

    def __str__(self):
        return f'Кот: {self.nickname}, возраст: {self.age}, длина шерсти: {self.wool_length}'


class Sphinx(Cat):
    _wool_length = "лысый"

    def hunting(self):
        print(f'{self.nickname} охотится!')


class Meikun(Cat):
    _wool_length = "длинная"

    def catching_rats(self):
        print(f'{self.nickname} ловит крыс!')


class Korat(Cat):
    _wool_length = "средняя"

    def play(self):
        print(f'{self.nickname} играет!')


def main():
    nn = Input("Кличка Сфинкса").str()
    while True:
        try:
            cat = Sphinx(nn, Input("Возраст").int())
            cat.hunting()
            print(cat)
            break
        except ValueError as e:
            print(e)

    nn = Input("Кличка Мейкуна").str()
    while True:
        try:
            cat = Meikun(nn, Input("Возраст").int())
            cat.catching_rats()
            print(cat)
            break
        except ValueError as e:
            print(e)

    nn = Input("Кличка Кората").str()
    while True:
        try:
            cat = Korat(nn, Input("Возраст").int())
            cat.play()
            print(cat)
            break
        except ValueError as e:
            print(e)


main()