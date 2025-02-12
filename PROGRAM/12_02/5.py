# 77777
from datetime import datetime
from enum import Enum
from random import randint
from Input import Input


class VehicleType(Enum):
    CAR = 1
    HELICOPTER = 2
    DRONE = 3
    SPACESHIP = 4
    BUS = 5


class Vehicle:
    name: str
    coordinates: tuple[float, float, float]
    engine_power: float
    number_of_wheels: int
    distance_travelled: int

    def __init__(self, name: str, coordinates: tuple[float, float, float],
                 engine_power: float, number_of_wheels: int,
                 distance_travelled: int, vehicle_type: VehicleType):
        self.name = name
        self.coordinates = coordinates
        self.creationDate = datetime.now()
        self.engine_power = engine_power
        self.number_of_wheels = number_of_wheels
        self.distance_travelled = distance_travelled
        self.vehicle_type = vehicle_type

    def drive(self, t: int, v: tuple[float, float, float]):
        """ Ехать t секунд по вектору v """
        distance = self.engine_power * t + (3.1415 * self.number_of_wheels)
        self.distance_travelled += distance
        (x, y, z) = self.coordinates
        self.coordinates = (x + v[0] * distance, y + v[1] * distance, z + v[2] * distance)
        print(f'Машина проехала расстояние {distance}')

    def park(self):
        """ Припарковаться """
        distance = randint(1, 30)
        self.distance_travelled += distance
        (x, y, z) = self.coordinates
        self.coordinates = (x + distance / 2, y + distance / 2, z)
        print(f'Машина проехала расстояние {distance}')

    def get_coordinates(self):
        return self.coordinates


def main():
    drone = Vehicle(
        Input('Имя').str(),
        (0, 0, 0),
        Input('Мощность').float(),
        0,
        Input('Пробег').float(),
        VehicleType.DRONE
    )
    while True:
        try:
            n = Input('Действие').natural()
            match n:
                case 1: print(drone.get_coordinates())
                case 2:
                    t = Input('Время').float()
                    x = Input('x').float()
                    y = Input('y').float()
                    z = Input('z').float()
                    drone.drive(t, (x, y, z))
                case 3: drone.park()
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()

