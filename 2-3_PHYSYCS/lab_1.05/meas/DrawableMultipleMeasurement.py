from math import *
from .tools import *
from .LinearMultipleMeasurement import *
from .Drawer import *



class DrawableMultipleMeasurement(LinearMultipleMeasurement, Drawer):
    def calculate_coefficients(self, X, Y):
        # ФУНКЦИОНАЛ ПЕРЕНЕСЁН в LinearMultipleMeasurement
        """Вычисляет коэффициенты A и B по МНК для модели Y = A·X + B"""
        N = len(X)
        A = (N * sum(x*y for x, y in zip(X, Y)) - sum(X) * sum(Y)) / (N * sum(x*x for x in X) - (sum(X))**2)
        B = (N * sum(x*x for x, y in zip(X, Y)) * sum(Y) - sum(X) * sum(x*y for x, y in zip(X, Y))) / (N * sum(x*x for x in X) - (sum(X))**2)
        A = (N * sum(x*y for x, y in zip(X, Y)) - sum(X) * sum(Y)) / (N * sum(x*x for x in X) - (sum(X))**2)
        B = (sum(Y) * sum(x*x for x in X) - sum(X) * sum(x*y for x, y in zip(X, Y))) / (N * sum(x*x for x in X) - (sum(X))**2)
        return B, A
    
    @timer
    def plot_MKN(self, **kwargs):
        self.plot_dependency(self.a, self.b, self._measurments_X, self._measurments_Y, **kwargs)