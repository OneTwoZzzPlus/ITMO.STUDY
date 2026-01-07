import math 
from .Tools import *
from .Measurement import *
from .MultipleMeasurement import *
  
class LinearMultipleMeasurement():
    _measurments_X: list[Measurement]
    _measurments_Y: list[Measurement]
    _a: Measurement
    _b: Measurement
    
    @property
    def a(self):
        return self._a
    
    @property
    def b(self):
        return self._b
    
    @property
    def measurments_X(self):
        return self._measurments_X
    
    @property
    def measurments_Y(self):
        return self._measurments_Y
    
    @check_len
    def __init__(self, measurments_X, measurments_Y):
        self._N = len(measurments_X)
        if isinstance(measurments_X[0], Measurement):
            self._measurments_X = measurments_X
            self._measurments_Y = measurments_Y
        else:
            self._measurments_X = [Measurement(x, 0) for x in measurments_X]
            self._measurments_Y = [Measurement(y, 0) for y in measurments_Y]
        self._calc()
    
    def _calc(self):
        N, x, y = self._N, [x.value for x in self.measurments_X], [y.value for y in self.measurments_Y]
        av_x = sum(x) / N
        av_y = sum(y) / N
        b = sum((x[i] - av_x) * (y[i] - av_y) for i in range(N)) / sum((x[i] - av_x)**2 for i in range(N))
        a = av_y - b * av_x
        d = [y[i] - (a + b*x[i]) for i in range(N)]
        D = sum((x[i] - av_x)**2 for i in range(N))
        sum_sQ = (sum(d[i]**2 for i in range(N))) / (N - 2)
        sigma_bQ = sum_sQ  / D
        sigma_aQ = (1/N + av_x**2/D) * (sum_sQ)
        delta_a = 2*math.sqrt(sigma_aQ)
        delta_b = 2*math.sqrt(sigma_bQ)
        self._a = Measurement(a, delta_a)
        self._b = Measurement(b, delta_b)
        
    @property
    def info(self):
        return f"y = a + bx: y = {self.a.value}{'+' if self.b.value >= 0 else ''}{self.b.value}x"\
               f"\na = {self.a}\nb = {self.b}"
    
    @property
    def min_X(self):
        return min(self._measurments_X)
    
    @property
    def max_X(self):
        return max(self._measurments_X)
    
    @property
    def min_Y(self):
        return min(self._measurments_Y)
    
    @property
    def max_Y(self):
        return max(self._measurments_Y)
    