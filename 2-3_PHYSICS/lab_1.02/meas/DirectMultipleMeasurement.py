from math import *
from .tools import *
from .Measurement import Measurement

student_koef = {2:12.7, 3:4.30, 4:3.18, 5:2.78, 6:2.57, 7:2.45, 8:2.36, 9:2.31, 10:2.26, 20:2.09, 30:2.04}
 
class DirectMultipleMeasurement(Measurement):
    N: int
    values: list[float]
    delta_instrumental: float
    delta_random_: float
    student: float
    
    
    def __init__(self, measured_values, delta_instrumental=0):
        self.values = measured_values
        self.N = len(measured_values)
        if self.N not in student_koef:
            raise ValueError(f'Нет значения Стьюдента {self.N} измерений в "student_koef"')
        self.student = student_koef[self.N]
        self.delta_instrumental = delta_instrumental
        self.calc()
        self.round()
        
    def calc(self):
        self.value_ = sum(self.values) / self.N
        self.sigma_ = sqrt(sum((x - self.value_)**2 for x in self.values)/(self.N*(self.N - 1)))
        self.delta_random_ = self.sigma_ * self.student
        self.delta_ = sqrt(self.delta_random_**2 + (4/9)*self.delta_instrumental**2)
        self.epsilon_ = self.delta_ / self.value_ * 100     
        
    def debug(self):
        return f"\nN = {self.N}\nvalues = {self.values}\naverage = {self.value}\naverage_ = {self.value_}" \
               f"\nsigma_ = {self.sigma_}\ndelta = {self.delta}\ndelta_ = {self.delta_}" \
               f"\ndelta_instrumental = {self.delta_instrumental}" \
               f"\ndelta_random_ = {self.delta_random_}\nstudent = {self.student}"\
               f"\nepsilon = {self.epsilon}\nepsilon_ = {self.epsilon_}"