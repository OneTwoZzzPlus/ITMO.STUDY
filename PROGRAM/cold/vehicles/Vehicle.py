from datetime import datetime
from .Vector3 import Vector3


class Vehicle:
    _vehicle_type = "Транспортное средство"
    _name: str
    _coordinates: Vector3
    _engine_power: float
    _distance_travelled: float
    _creation_date: datetime

    def __init__(self, name: str, engine_power: float, coordinates=Vector3(0, 0, 0)):
        self.name = name
        self.engine_power = engine_power
        self.coordinates = coordinates
        # Пробег изменяется автоматически
        self._distance_travelled = 0
        # Дата создания для подсчёта возраста
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
        """ Вычисляем возраст ТС """
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
        self._coordinates += v * distance
        print(f'{self._vehicle_type} {self.name} преодолел расстояние {distance}')

    def park(self, p: Vector3):
        """ Переместиться в точку p """
        distance = abs(self.coordinates - p)
        self._distance_travelled += distance
        self._coordinates = p

        print(f'{self._vehicle_type} {self.name} на преодолел расстояние {distance} за {t:.2f}с')

    def __str__(self):
        return f"Тип: {self.vehicle_type}, имя: {self.name}, координаты {self.coordinates:.2f},"\
               f"мощность: {self.engine_power:.2f}, пробег: {self.distance_travelled:.2f},"\
               f"возраст: {self.age}"

    def __add__(self, other):
        if not isinstance(other, Vehicle):
            raise ValueError('object must be Vehicle')
        return Vehicle(f'{self.name}-{other.name}', self.engine_power + other.engine_power, self.coordinates)
    
    def __mul__(self, other):
        if not isinstance(other, Vehicle):
            raise ValueError('object must be Vehicle')
        return Vehicle(f'{self.name}', self.engine_power, self.coordinates)