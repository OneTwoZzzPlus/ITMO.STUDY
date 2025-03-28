from math import *
from .tools import *
from .LinearMultipleMeasurement import *
from .Drawer import *



class DrawableMultipleMeasurement(LinearMultipleMeasurement, Drawer):
    def calculate_coefficients(self, X, Y):
        """Вычисляет коэффициенты A и B по МНК для модели Y = A·X + B"""
        N = len(X)
        A = (N * sum(x*y for x, y in zip(X, Y)) - sum(X) * sum(Y)) / (N * sum(x*x for x in X) - (sum(X))**2)
        B = (N * sum(x*x for x, y in zip(X, Y)) * sum(Y) - sum(X) * sum(x*y for x, y in zip(X, Y))) / (N * sum(x*x for x in X) - (sum(X))**2)
        A = (N * sum(x*y for x, y in zip(X, Y)) - sum(X) * sum(Y)) / (N * sum(x*x for x in X) - (sum(X))**2)
        B = (sum(Y) * sum(x*x for x in X) - sum(X) * sum(x*y for x, y in zip(X, Y))) / (N * sum(x*x for x in X) - (sum(X))**2)
        # print(A, B)
        return A, B
    
    @timer
    def plot_MKN(self):
        X, Y = [x.value_ for x in self.measurments_X], [y.value_ for y in self.measurments_Y]
        self.plot_dependency(*self.calculate_coefficients(X, Y), self._measurments_X, self._measurments_Y)