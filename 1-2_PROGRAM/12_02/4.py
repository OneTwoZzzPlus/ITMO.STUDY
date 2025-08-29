from Input import Input
from datetime import datetime


class Car:
    works = False

    def __init__(self, color: str, ttype: str, year: int):
        self.set_color(color)
        self.set_type(ttype)
        self.set_year(year)

    def start(self):
        if not self.works:
            print('Автомобиль заведён')
            self.works = True
        else:
            print('Автомобиль сейчас не может быть заведён')

    def stop(self):
        if self.works:
            print('Автомобиль заглушен')
            self.works = False
        else:
            print('Автомобиль сейчас не может быть заглушен')

    @staticmethod
    def input_year(year):
        if 1886 <= int(year) <= datetime.now().year:
            return int(year)
        raise ValueError('Неправильный год!')

    def set_year(self, year: int):
        self.year = self.input_year(year)

    def set_type(self, ttype: str):
        if isinstance(ttype, str):
            self.ttype = ttype
        else:
            raise ValueError('Ожидалась строка - тип автомобиля!')

    def set_color(self, color: str):
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError('Ожидалась строка - цвет автомобиля!')

    def info(self):
        print(f'Автомобиль {'запущен' if self.works else 'заглушен'}'
              f'\n\tЦвет {self.color}\n\tТип {self.ttype}\n\tГод {self.year}')


def main():
    car = Car(
        Input('Введите цвет').str(),
        Input('Введите тип').str(),
        Input('Введите год').inp(Car.input_year)
    )
    while True:
        try:
            n = Input('Действие').natural()
            match n:
                case 1: car.start()
                case 2: car.stop()
                case 3: car.set_year(Input('Введите новый год').inp(Car.input_year))
                case 4: car.set_type(Input('Введите новый тип').str())
                case 5: car.set_color(Input('Введите новый цвет').str())
                case 6: car.info()
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()

