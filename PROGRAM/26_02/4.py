from Input import Input


class Doctor:
    _age: int

    def __init__(self, age=25):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 25:
            raise ValueError('Слишком молодой доктор!')
        self._age = value

    def __str__(self):
        return f"Доктор"


class Pediatrician(Doctor):
    _efficiency = 100

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
        print("Изменен стаж доктора!")

    def treat_child(self):
        print(f"Лечение ребёнка с эффективностью {abs(100 / 100 - self._efficiency):.2f}%")

    def inspect_child(self, child: str):
        print(f"Осмотр ребёнка {child}")
        self._efficiency += len(child)


class Oculist(Doctor):
    _limit = 2

    @property
    def limit(self):
        return self._limit

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
        self.chill()

    def work(self):
        if self._limit <= 0:
            self.chill()
        else:
            print(f"Проверка зрения!")
            self._limit -= 1

    def chill(self):
        print(f"Окулист отдыхает...")
        self._limit = 2


class Dentist(Doctor):
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        self._age = value
        self.cause_pain()

    def cause_pain(self):
        print(f'Больно дёрнул зуб! Сейчас ему {self._age}')


def main():
    pediatr = Pediatrician()
    while True:
        try:
            pediatr.age = Input('Возраст педиатра').natural()
            break
        except ValueError as e:
            print(e)
    pediatr.inspect_child(Input('Имя ребёнка').str())
    pediatr.treat_child()

    oculist = Oculist(60)
    oculist.work()
    oculist.work()
    oculist.work()

    dentist = Dentist(30)
    while True:
        try:
            pediatr.age = Input('Возраст дантиста').natural()
            break
        except ValueError as e:
            print(e)
    dentist.cause_pain()


main()
