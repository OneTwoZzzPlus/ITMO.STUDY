from .Measurement import Measurement
from .MeasException import *
from abc import ABC, abstractmethod
 
student_koef = {2:12.7, 3:4.30, 4:3.18, 5:2.78, 6:2.57, 7:2.45, 8:2.36, 9:2.31, 10:2.26, 20:2.09, 30:2.04}
 
class MultipleMeasurement(Measurement, ABC):
    _N: int
    _values: list[float]
    _measurments: list[Measurement]
    
    @property
    def values(self):
        return self._values
    
    @property
    def measurments(self):
        return self._measurments
    
    @property
    def N(self):
        return self._N
    
    def __init__(self, measured_values):
        self._N = len(measured_values)
        if self._N not in student_koef:
            raise StudentException(self._N)
        self._student = student_koef[self._N]
        self._calc()
        self._round()
        
    def info(self):
        return f"\nN = {self._N}\nvalues = {self._values}\naverage = {self._value} ({self._value_})" \
               f"\ndelta = {self._delta} ({self._delta_})" \
               f"\nepsilon = {self._epsilon} ({self._epsilon_})"
               
    def __getitem__(self, index):
        return self._measurments[index]
    
    @property
    def asMeasurment(self):
        return Measurement(self._value, self._delta, self._epsilon)