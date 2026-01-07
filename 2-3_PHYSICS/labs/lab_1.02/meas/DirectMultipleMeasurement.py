import math
from .MultipleMeasurement import *
 
class DirectMultipleMeasurement(MultipleMeasurement):
    _delta_instrumental: float
    _delta_random_: float
    _student: float
    
    @property
    def values(self):
        return self._values
    
    @property
    def N(self):
        return self._N
    
    def __init__(self, 
            measured_values:list[int|float|Measurement], delta_instrumental:int|float=0, 
            dim:int|None=None, **kwargs):
        self._delta_instrumental = delta_instrumental
        if isinstance(measured_values[0], Measurement):
            self._measurments = measured_values
            self._values = [x.value for x in measured_values]
        else: 
            self._values = measured_values
            self._measurments = [Measurement(x, delta_instrumental, direct=True) for x in measured_values]
        if dim is not None:
            self._delta_instrumental *= dim
        super().__init__(measured_values, **kwargs)
    
    def _calc(self):
        # Считаем значение и погрешность
        self._value = sum(self._values) / self._N
        self._sigma = math.sqrt(sum((x - self._value)**2 for x in self._values)/(self._N*(self._N - 1)))
        self._delta_random = self._sigma * self._student
        self._delta = math.sqrt(self._delta_random**2 + (4/9)*self._delta_instrumental**2)
        self._epsilon = self._delta / self._value * 100 if not math.isclose(self._value, 0) else 0 
        
        self._str_value, self._str_delta, self._str_epsilon = self._round_components()
        
    def __str__(self):
        return (
            super().__str__() + 
            f"\nsigma_ = {self._sigma}\ndelta_instrumental = {self._delta_instrumental}" +
            f"\ndelta_random_ = {self._delta_random}\nstudent = {self._student}"
        )