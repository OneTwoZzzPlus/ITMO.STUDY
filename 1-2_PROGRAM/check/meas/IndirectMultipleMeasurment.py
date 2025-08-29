from math import *
from .MultipleMeasurement import *
  
class IndirectMultipleMeasurement(MultipleMeasurement):
    def __init__(self, measured_values):
        super().__init__(measured_values)
        
    def _calc(self):
        # Считаем значение и погрешность
        self._value_ = sum(self._values) / self._N
        self._sigma_ = sqrt(sum((x - self._value_)**2 for x in self._values)
                            /(self._N*(self._N - 1)))
        self._delta_ = self._sigma_ * self._student
        self._epsilon_ = self._delta_ / self._value_ * 100  
            
    def info(self):
        return super().info() + f"\nsigma_ = {self._sigma_}"