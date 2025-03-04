class Vector3:
    x: float
    y: float
    z: float

    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = x, y, z

    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other) -> float:
        if isinstance(other, float):
            return Vector3(self.x + other, self.y + other, self.z + other)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
