from math import *
from .MultipleMeasurement import *
 
class DirectMultipleMeasurement(MultipleMeasurement):
    _delta_instrumental_: float
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
            dim:int|None=None,
            name:str|None=None, char:str='', unit:str=''):
        self._delta_instrumental_ = delta_instrumental
        if isinstance(measured_values[0], Measurement):
            self._measurments = measured_values
            self._values = [x.value_ for x in measured_values]
        else: 
            self._values = measured_values
            self._measurments = [Measurement(x, delta_instrumental, direct=True) for x in measured_values]
        if dim is not None:
            self._delta_instrumental_ *= dim
        super().__init__(measured_values, dim=dim, name=name, char=char, unit=unit)
    
    def _calc(self):
        # Считаем значение и погрешность
        self._value_ = sum(self._values) / self._N
        self._sigma_ = sqrt(sum((x - self._value_)**2 for x in self._values)/(self._N*(self._N - 1)))
        self._delta_random_ = self._sigma_ * self._student
        self._delta_ = sqrt(self._delta_random_**2 + (4/9)*self._delta_instrumental_**2)
        self._epsilon_ = self._delta_ / self._value_ * 100 if not isclose(self._value_, 0) else 0  
        
    def info(self):
        return (
            super().info() + 
            f"\nsigma_ = {self._sigma_}\ndelta_instrumental = {self._delta_instrumental_}" +
            f"\ndelta_random_ = {self._delta_random_}\nstudent = {self._student}"
        )