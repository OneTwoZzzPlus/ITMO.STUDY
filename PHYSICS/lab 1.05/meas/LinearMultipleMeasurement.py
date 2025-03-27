from math import *
from .tools import *
from .Measurement import Measurement
 
student_koef = {2:12.7, 3:4.30, 4:3.18, 5:2.78, 6:2.57, 7:2.45, 8:2.36, 9:2.31, 10:2.26, 20:2.09, 30:2.04}
 
class LinearMultipleMeasurement(Measurement):
    _values: list[float]
    _measurments_X: list[Measurement]
    _measurments_Y: list[Measurement]
    
    @property
    def measurments_X(self):
        return self._measurments_X
    
    @property
    def measurments_Y(self):
        return self._measurments_Y
    
    @check_len
    def __init__(self, measurments_X, measurments_Y):
        self._measurments_X = measurments_X
        self._measurments_Y = measurments_Y
        self._values = [v._value_ / u._value_ for (v, u) in zip(measurments_X, measurments_Y)]
        self._calc()
        self._round() 
        
    def _calc(self):
        # Считаем значение и погрешность
        # ПЕРЕСМОТРЕТЬ student
        self._student = 1
        self._value_ = sum(self._values) / len(self._values)
        self._delta_ = sqrt(sum((x - self._value_)**2 for x in self._values)/(len(self._values)*(len(self._values) - 1))) * self._student
        self._epsilon_ = self._delta_ / self._value_ * 100
        
        
    def info(self):
        return f"{self._measurments_X}\n{self._measurments_Y}"\
               f"\nN = {len(self._values)}\naverage = {self._value}\naverage_ = {self._value_}" \
               f"\ndelta = {self._delta}\ndelta_ = {self._delta_}" \
               f"\nstudent = {self._student}\nepsilon = {self._epsilon}\nepsilon_ = {self._epsilon_}"