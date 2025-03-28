from math import *
from .tools import *
from .Measurement import *
from .MultipleMeasurement import *
from .IndirectMultipleMeasurment import *
  
class LinearMultipleMeasurement():
    _measurments_X: MultipleMeasurement
    _measurments_Y: MultipleMeasurement
    _delta_a: int
    
    @property
    def measurments_X(self):
        return self._measurments_X
    
    @property
    def measurments_Y(self):
        return self._measurments_Y
    
    @check_len
    def __init__(self, measurments_X, measurments_Y):
        self._N = len(measurments_X)
        if issubclass(type(measurments_X), MultipleMeasurement):
            self._measurments_X = measurments_X
            self._measurments_Y = measurments_Y
        else:
            self._measurments_X = IndirectMultipleMeasurement(measurments_X)
            self._measurments_Y = IndirectMultipleMeasurement(measurments_Y)
        self._calc()
        
    def _calc(self):
        N, x, y = self._N, self.measurments_X.values,  self.measurments_Y.values
        av_x = sum(x) / N
        av_y = sum(y) / N
        b = sum((x[i] - av_x) * (y[i] - av_y) for i in range(N))
        a = av_y - b * av_x
        d = [y[i] - (a + b*x[i]) for i in range(N)]
        D = sum((x[i] - av_x)**2 for i in range(N))
        sigma_bQ = (sum(d[i]**2 for i in range(N))) / (N - 2) / D
        sigma_aQ = (1/N + av_x**2/D) * (sum(d[i]**2 for i in range(N)) / (N - 2))
        delta_a = 2*sqrt(sigma_aQ)
        delta_b = 2*sqrt(sigma_bQ)
        
    def info(self):
        return f"{self._measurments_X}\n{self._measurments_Y}"