from Input import Input
from abc import ABC, abstractmethod, abstractproperty


class Country(ABC):
    _capital: str
    _population: int

    def __init__(self, population):
        self.population = population

    @property
    def capital(self):
        return self._capital

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value: int):
        if not isinstance(value, int):
            raise ValueError('population: ожидалось число')
        if value <= 0:
            raise ValueError('population: ожидалось положительное число')
        self._population = value

    @abstractmethod
    def border(self):
        pass


class Russia(Country):
    def __init__(self, population, capital="Москва"):
        super().__init__(population)
        self._capital = capital

    def border(self):
        print("Границы открыты")


class Canada(Country):
    _capital = "Оттава"

    def border(self):
        print("Границы открыты")


class Germany(Country):
    _capital = "Берлин"

    def border(self):
        print("Границы закрыты")


def main():
    russia = Russia(144_317_440)
    russia.border()
    print(russia.capital)
    germany = Germany(84_552_242)
    germany.border()
    canada = Canada(41_465_298)
    canada.border()
    try:
        new_pop = Input("Популяция России").int()
        russia.population = new_pop
        print(f'Популяция России = {russia.population}')
    except ValueError as e:
        print(e)

main()