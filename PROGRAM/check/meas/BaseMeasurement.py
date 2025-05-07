from abc import ABC, abstractmethod

class BaseMeasurement(ABC):
    _value: float      # окр. значение
    _value_: float     # значение
    _delta: float      # окр. абсолютная
    _delta_: float     # абсолютная
    _epsilon: float    # окр. относительная
    _epsilon_: float   # относительная
    
    _is_direct: bool   # измерение прямое
    
    def _idm(self):
        return 2/3 if self._is_direct else 1
    
    @property
    def value(self):
        return self._value
    
    @property
    def v(self):
        return self._value_
    
    @property
    def value_(self):
        return self._value_
    
    @property
    def delta(self):
        return self._delta
    
    @property
    def delta_(self):
        return self._delta_

    @property
    def epsilon(self):
        return self._epsilon
    
    @property
    def epsilon_(self):
        return self._epsilon_
    
    @property
    def is_direct(self):
        return self._is_direct
    
    @abstractmethod
    def _calc(self):
        raise NotImplementedError('Реализуйте пересчёт значений!')
    
    @abstractmethod
    def info(self):
        raise NotImplementedError('Реализуйте вывод информации!')
    