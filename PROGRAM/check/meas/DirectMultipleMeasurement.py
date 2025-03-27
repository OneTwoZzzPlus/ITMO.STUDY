from math import *
from .tools import *
from .Measurement import Measurement

student_koef = {2:12.7, 3:4.30, 4:3.18, 5:2.78, 6:2.57, 7:2.45, 8:2.36, 9:2.31, 10:2.26, 20:2.09, 30:2.04}
 
class DirectMultipleMeasurement(Measurement):
    _N: int
    _values: list[float]
    _delta_instrumental: float
    _delta_random_: float
    _student: float
    
    @property
    def values(self):
        return self.values
    
    @property
    def N(self):
        return self._N
    
    def delta_instrumental(self, x: int):
        self._delta_instrumental = x
        self._calc()
        self._round()
    
    def __init__(self, measured_values, delta_instrumental=0):
        self._values = measured_values
        self._N = len(measured_values)
        if self._N not in student_koef:
            raise ValueError(f'Нет значения Стьюдента {self._N} измерений в "student_koef"')
        self._student = student_koef[self._N]
        self._delta_instrumental = delta_instrumental
        self._calc()
        self._round()
        
    def _calc(self):
        # Считаем значение и погрешность
        self._value_ = sum(self._values) / self._N
        self._sigma_ = sqrt(sum((x - self._value_)**2 for x in self._values)/(self._N*(self._N - 1)))
        self._delta_random_ = self._sigma_ * self._student
        self._delta_ = sqrt(self._delta_random_**2 + (4/9)*self._delta_instrumental**2)
        self._epsilon_ = self._delta_ / self._value_ * 100     
        
    def info(self):
        return f"\nN = {self._N}\nvalues = {self._values}\naverage = {self._value}\naverage_ = {self._value_}" \
               f"\nsigma_ = {self._sigma_}\ndelta = {self._delta}\ndelta_ = {self._delta_}" \
               f"\ndelta_instrumental = {self._delta_instrumental}" \
               f"\ndelta_random_ = {self._delta_random_}\nstudent = {self._student}"\
               f"\nepsilon = {self._epsilon}\nepsilon_ = {self._epsilon_}"