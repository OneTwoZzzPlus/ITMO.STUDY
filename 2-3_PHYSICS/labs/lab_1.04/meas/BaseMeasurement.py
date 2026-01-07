from abc import ABC

class BaseMeasurement(ABC):
    _value: float     # значение
    _delta: float     # абсолютная
    _epsilon: float   # относительная
    
    @property
    def value(self):
        return self._value
    
    @property
    def delta(self):
        return self._delta

    @property
    def epsilon(self):
        return self._epsilon
    
    _is_direct: bool   # измерение прямое
    
    @property
    def _idm(self):
        return 2/3 if self._is_direct else 1
    
    @property
    def is_direct(self):
        return self._is_direct
    
    _str_value: str
    _str_delta: str
    _str_epsilon: str
    
    @property
    def str_value(self):
        return self._str_value
    
    @property
    def str_delta(self):
        return self._str_delta

    @property
    def str_epsilon(self):
        return self._str_epsilon
    