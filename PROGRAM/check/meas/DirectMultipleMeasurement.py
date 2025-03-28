from math import *
from .tools import *
from .MultipleMeasurement import *
 
class DirectMultipleMeasurement(MultipleMeasurement):
    _delta_instrumental_: float
    _delta_random_: float
    _student: float
    
    @property
    def values(self):
        return self.values
    
    @property
    def N(self):
        return self._N
    
    def __init__(self, measured_values, delta_instrumental=0):
        self._delta_instrumental_ = delta_instrumental
        super().__init__(measured_values)
        
    def _calc(self):
        # Считаем значение и погрешность
        self._value_ = sum(self._values) / self._N
        self._sigma_ = sqrt(sum((x - self._value_)**2 for x in self._values)/(self._N*(self._N - 1)))
        self._delta_random_ = self._sigma_ * self._student
        self._delta_ = sqrt(self._delta_random_**2 + (4/9)*self._delta_instrumental_**2)
        self._epsilon_ = self._delta_ / self._value_ * 100     
        
    def info(self):
        return (
            super().info() + 
            f"\nsigma_ = {self._sigma_}\ndelta_instrumental = {self._delta_instrumental_}" +
            f"\ndelta_random_ = {self._delta_random_}\nstudent = {self._student}"
        )