from math import *
from .tools import *
from abc import ABC, abstractmethod

class BaseMeasurement(ABC):
    _value: float    # окр. значение
    _value_: float   # значение
    _delta: float    # окр. абсолютная
    _delta_: float   # абсолютная
    _epsilon: float  # окр. относительная
    _epsilon_: float # относительная
    
    @property
    def value(self):
        return self._value
    
    @property
    def delta(self):
        return self._delta

    @property
    def epsilon(self):
        return self._epsilon
    
    @abstractmethod
    def _calc(self):
        raise NotImplementedError('Реализуйте пересчёт значений!')
    
    @abstractmethod
    def info(self):
        raise NotImplementedError('Реализуйте вывод информации!')
    