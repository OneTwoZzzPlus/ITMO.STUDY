# 77777
from datetime import datetime
from random import randint
from Input import Input


class Vector3:
    x: float
    y: float
    z: float

    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = x, y, z

    def __abs__(self):
        return (self.x**2 + self.y**2, self.z**2)**0.5

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other) -> float:
        if isinstance(other, float):
            return Vector3(self.x + other, self.y + other, self.z + other)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


class Vehicle:
    _vehicle_type = "ТС"
    _name: str
    _coordinates: Vector3
    _engine_power: float
    _distance_travelled: float
    _creation_date: datetime

    def __init__(self, name: str, coordinates: Vector3, engine_power: float):
        self.name = name
        self.coordinates = coordinates
        self.engine_power = engine_power
        self._distance_travelled = 0
        self._creation_date = datetime.now()

    @property
    def vehicle_type(self) -> str:
        return self._vehicle_type

    @property
    def name(self) -> str:
        return self._name

    @property
    def coordinates(self) -> Vector3:
        return self._coordinates

    @property
    def engine_power(self) -> float:
        return self._engine_power

    @property
    def distance_travelled(self) -> float:
        return self._distance_travelled

    @property
    def age(self) -> float:
        return datetime.now() - self._creation_date

    @name.setter
    def name(self, value: str):
        self._name = value

    @coordinates.setter
    def coordinates(self, value: Vector3):
        self._coordinates = value

    @engine_power.setter
    def engine_power(self, value: float):
        if value < 0:
            raise ValueError('Отрицательная мощность!')
        self._engine_power = value

    def drive(self, t: int, v: Vector3):
        """ Перемещаться t секунд по вектору v """
        distance = self.engine_power * t
        self._distance_travelled += distance
        self.coordinates += v * distance
        print(f'{self._vehicle_type} {self.name} преодолел расстояние {distance}')

    def park(self, p: Vector3):
        """ Переместиться в точку p """
        self.coordinates = p
        print(f'{self._vehicle_type} {self.name} на месте')

    def __str__(self):
        return f"Тип: {self.vehicle_type}, имя: {self.name}, координаты {self.coordinates},"\
               f"мощность: {self.engine_power}, пробег: {self.distance_travelled},"\
               f"возраст: {self.age}"


class Drone(Vehicle):
    _vehicle_type = "Дрон"
    _payload: float
    _cargo: str

    def __init__(self, name: str, coordinates: Vector3, engine_power: float, payload: float):
        super().__init__(name, coordinates, engine_power)
        self.payload = payload
        self._cargo = None

    @property
    def payload(self):
        return self._payload

    @property
    def cargo(self):
        return "Ничего!" if self._cargo is None else self._cargo

    @payload.setter
    def payload(self, value):
        self._payload = value

    def load(self, weight: float, cargo: str):
        if self._cargo is not None:
            self.upload()
        if weight < self._payload:
            self._cargo = cargo
            print("Загружен!")
        else:
            print("Слишком тяжёлый груз!")

    def upload(self):
        if self._cargo is None:
            print("Нечего выгружать!")
        else:
            self._cargo = None
            print("Груз выгружен!")

    def __str__(self):
        return f"Тип: {self.vehicle_type}, имя: {self.name}, координаты {self.coordinates},"\
               f"мощность: {self.engine_power}, пробег: {self.distance_travelled},"\
               f"возраст: {self.age}, грузоподъёмность: {self.payload}, груз: {self.cargo}"


class Car(Vehicle):
    _vehicle_type = "Машина"
    _fuel: float

    def __init__(self, name: str, coordinates: Vector3, engine_power: float):
        super().__init__(name, coordinates, engine_power)
        self._fuel = 100

    def refill(self):
        print(f"Заправили {self.name}")
        self._fuel += 100

    def __str__(self):
        return f"Тип: {self.vehicle_type}, имя: {self.name}, координаты {self.coordinates},"\
               f"мощность: {self.engine_power}, пробег: {self.distance_travelled},"\
               f"возраст: {self.age}, топливо: {self._fuel}"


def main():
    drone = Drone(
        Input('Имя дрона').str(),
        Vector3(0, 0, 0),
        Input('Мощность').float(),
        Input('Грузоподъёмность').float()
    )
    car = Car(
        Input('Имя машины').str(),
        Vector3(0, 0, 0),
        Input('Мощность').float()
    )
    while True:
        try:
            n = Input('Что сделать с дроном (1-6), машиной(7-8)?').natural()
            match n:
                case 1: print(drone)
                case 2:
                    t = Input('Время').float()
                    x = Input('x').float()
                    y = Input('y').float()
                    z = Input('z').float()
                    drone.drive(t, Vector3(x, y, z))
                case 3:
                    x = Input('x').float()
                    y = Input('y').float()
                    z = Input('z').float()
                    drone.park(Vector3(x, y, z))
                case 4:
                    drone.payload = Input("Грузоподъёмность новая").natural()
                case 5:
                    drone.load(Input("Вес").natural(), Input("Название").str())
                case 6:
                    drone.upload()
                case 7:
                    print(car)
                case 8:
                    car.refill()
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
