from Input import Input


class Pupil:
    _name: str
    _age: int
    _classNumber: str

    def __init__(self, name="Radomir", age=8, class_number=1):
        self.name, self.age, self.class_number = name, age, class_number

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError()
        if not 0 <= value <= 150:
            raise ValueError()
        self._age = value

    @property
    def class_number(self):
        return self._class_number

    @class_number.setter
    def class_number(self, value: int):
        classes = ['1-A', '2-B', '3-C', '4-D', '5-D', '6-E',
                   '7-F', '8-G', '9-H', '10-I', '11-J', '12-K']
        if not 1 <= int(value) <= 12:
            raise ValueError("Неверный номер класса")
        self._class_number = classes[int(value) - 1]

    def __str__(self):
        return f'Имя: {self._name}, возраст: {self._age}, класс: {self._class_number}'

    def info(self):
        print(self)


def main():
    try:
        r = Pupil()
        r.info()
        name = Input('Введите имя').str()
        age = Input('Введите возраст').natural()
        class_number = Input('Введите номер класса').natural()
        p = Pupil(name, age, class_number)
        p.info()
        p.name = Input('Введите новое имя').str()
        p.info()
        p.age = Input('Введите новый возраст').natural()
        p.info()
        p.class_number = Input('Введите новый номер класса').natural()
        p.info()
    except ValueError as e:
        print(e)


main()