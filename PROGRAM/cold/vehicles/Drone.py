from .Vehicle import Vehicle
from .Vector3 import Vector3


class Drone(Vehicle):
    _vehicle_type = "Дрон"
    _payload: float
    _cargo: str

    def __init__(self, name: str, engine_power: float, payload: float, coordinates=Vector3(0, 0, 0)):
        super().__init__(name, engine_power, coordinates)
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
        return f"{super().__str__()}, грузоподъёмность: {self.payload:.2f}, груз: {self.cargo}"