from .Vehicle import Vehicle
from .Vector3 import Vector3


class Car(Vehicle):
    _vehicle_type = "Машина"
    _fuel: float

    def __init__(self, name: str, engine_power: float, coordinates=Vector3(0, 0, 0)):
        super().__init__(name, engine_power, coordinates)
        self._fuel = 100

    def refill(self):
        print(f"Заправили {self.name}")
        self._fuel += 100

    def __str__(self):
        return f"{super().__str__()}, топливо: {self._fuel:.2f}"
