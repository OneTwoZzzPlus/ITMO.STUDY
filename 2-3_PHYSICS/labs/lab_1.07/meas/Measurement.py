from math import *
from .tools import * 
from .BaseMeasurement import *
from .DataBase import *

  
class Measurement(BaseMeasurement, Tools):
    def __init__(self, value:float, delta:float|None=None, epsilon:float|None=None, 
                 name:str|None=None, char:str='', unit:str='',
                 dim:float|None=None, direct:bool=False):
        if isinstance(value, str):
            name = value
            
        if name is not None:
            try:
                res = MeasurmentDB.get(MeasurmentDB.name == name)
            except (MeasurmentDB.DoesNotExist, OperationalError):
                res = MeasurmentDB.create(
                    name=name,
                    value=value,
                    delta=delta,
                    epsilon=None
                )
            value = res.value
            delta = res.delta
            epsilon = res.epsilon
        
        self._name = name
        self._char = char
        self._unit = unit
        self._value_ = value
        self._delta_ = delta
        self._epsilon_ = epsilon
        self._is_direct = direct
        self._dimer(dim)
        self._calc()
        self._round()
    
    def naming(self, char:str, unit:str=''):
        self._char = char
        self._unit = unit
    
    def _soft(self, x):
        # Округлить компьютерную погрешность
        CALC_ERROR = 12
        x = round(x, CALC_ERROR)
        return 0 if isclose(x, 0) else x
    
    def _calc(self):
        if self._epsilon_ is None and self._delta_ is None:
            self._epsilon_, self.delta = 0, 10^(-13)
        if self._epsilon_ is None:
            if isclose(self.value_, 0):
                self._epsilon_ = 0
            else:
                self._epsilon_ = (self._delta_ / abs(self._value_) * 100)
        elif self._delta_ is None:
            self._delta_ = self._epsilon_ * self._value_ / 100
    
    def _dimer(self, dim):
        if dim is not None:
            self._value_ *= dim
            if self._delta_ is not None:
                self._delta_ *= dim
        
    def _get_first_significant_digit(self, n):
        # Получаем первую значащую цифру
        n_abs = abs(float(n))
        if n_abs == 0:
            return 0
        s = "{:.15e}".format(n_abs)
        mantissa, exp = s.split('e')
        mantissa = mantissa.replace('.', '').lstrip('0')
        return int(mantissa[0]) if mantissa else 0

    def _round_to_significant(self, value, significant):
        # Округлить до значащей цифры
        if value == 0:
            return 0.0
        return float(("{:." + str(significant-1) + "e}").format(value))

    def _format_with_decimals(self, number, decimals):
        # Форматируем число с фиксированным количеством знаков после запятой
        return ("{0:." + str(decimals) + "f}").format(number)
    
    def _round(self):
        # Обработка абсолютной погрешности
        first_digit = self._get_first_significant_digit(self._delta_)
        k_delta_x = 2 if first_digit in {1, 2, 3} else 1
        rounded_delta_x = self._round_to_significant(self._delta_, k_delta_x)
        
        # Определение порядка округления для x
        formatted_delta = "{:.{prec}e}".format(rounded_delta_x, prec=k_delta_x-1)
        mantissa, exp_part = formatted_delta.split('e')
        exp = int(exp_part)
        order = 10 ** (exp - (k_delta_x - 1))
        
        rounded_x = round(self._value_ / order) * order if order != 0 else self._value_
        
        # Обработка относительной погрешности
        rounded_delta_rel = None

        first_digit_rel = self._get_first_significant_digit(self._epsilon_)
        k_delta_rel = 2 if first_digit_rel in {1, 2, 3} else 1
        rounded_delta_rel = self._round_to_significant(self._epsilon_, k_delta_rel)
        
        # ИЗМЕНЕНО! Добавлен soft на окгругление!
        self._value = self._soft(rounded_x)
        self._delta = self._soft(rounded_delta_x)
        self._epsilon = self._soft(rounded_delta_rel)
    
    def format(self):
        # Обработка абсолютной погрешности
        first_digit = self._get_first_significant_digit(self._delta_)
        k_delta = 2 if first_digit in {1, 2, 3} else 1
        rounded_delta = self._round_to_significant(self._delta_, k_delta)
        
        # Определяем порядок округления для x
        delta_str = "{:.{}e}".format(rounded_delta, k_delta-1)
        mantissa_part, exp_part = delta_str.split('e')
        exponent = int(exp_part)
        step = 10 ** (exponent - (k_delta - 1))
        
        # Округляем x до нужного шага
        rounded_x = round(self._value_ / step) * step
        
        # Определяем количество знаков после запятой
        if step < 1:
            decimals = -int(log10(step))
        else:
            decimals = 0
        
        # Форматируем с сохранением всех нулей
        x_str = self._format_with_decimals(rounded_x, decimals)
        delta_str = self._format_with_decimals(rounded_delta, decimals)
        
        # Убираем лишние точки для целых чисел
        if decimals == 0:
            x_str = x_str.split('.')[0]
            delta_str = delta_str.split('.')[0]
            
        char_pm = '±'
        return f"{x_str}{char_pm}{delta_str}"
    
    @property
    def rounded(self):
        # Для дебага округлённых значений
        return f"{self.format()}, ε = {self._epsilon}%"
    
    @property
    def raw(self):
        # Для дебага сырых значений
        return f"{self._soft(self._value_)}, Δ = {self._soft(self._delta_):.9f}, ε = {self._soft(self._epsilon_):.9f}"
    
    def __str__(self):
        return f'{self.rounded} ({self.raw})'
    
    def __repr__(self):
        return f'{self.rounded}'
    
    def info(self):
        return f'{self.rounded} ({self.raw})'
    
    def __eq__(self, other): return self._value == other.value
    def __ne__(self, other): return not (self == other)
     
    def __gt__(self, other): return self._value > other.value
    def __le__(self, other): return not (self > other)
     
    def __lt__(self, other): return self._value < other.value
    def __ge__(self, other): return not (self < other)
    
    
    def __add__(self, other):
        if isinstance(other, Measurement):
            return Measurement(
                self._value_ + other._value_, 
                sqrt((self._idm() * self._delta_)**2 + (self._idm() * other._delta_)**2)
                )
        raise ValueError("Можно складывать только измерения")
        
    
    def __sub__(self, other):
        if isinstance(other, Measurement):
            return Measurement(
                self._value_ - other._value_, 
                sqrt((self._idm * self._delta_)**2 + (self._idm * other._delta_)**2)
                )
        raise ValueError("Можно вычитать только измерения")
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if isclose(other, 0):
                raise ZeroDivisionError()
            return Measurement(
                self.value_ / other, 
                self.delta_ / other, 
                direct=self._is_direct
            )
    