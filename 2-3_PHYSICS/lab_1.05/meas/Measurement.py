from math import *
from .tools import * 
from .BaseMeasurement import *

  
class Measurement(BaseMeasurement, Tools):
    def __init__(self, value, delta=0, epsilon=None):
        self._value_ = value
        self._delta_ = delta
        self._epsilon_ = epsilon
        self._calc()
        self._round()
    
    def _soft(self, x):
        # Округлить компьютерную погрешность
        CALC_ERROR = 12
        x = round(x, CALC_ERROR)
        return 0 if isclose(x, 0) else x
    
    def _calc(self):
        if isclose(self.value_, 0):
            self._epsilon_ = 0
        else:
            self._epsilon_ = (self._delta_ / abs(self._value_) * 100)  if self._epsilon_ is None else self._epsilon_

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
        return f"{self.format()} ε = {self._epsilon}"
    
    @property
    def raw(self):
        # Для дебага сырых значений
        return f"{self._soft(self._value_)} Δ = {self._soft(self._delta_):.9f} ε = {self._soft(self._epsilon_):.9f}"
    
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
        if not isinstance(other, Measurement):
            raise ValueError("Можно складывать только измерения")
        return Measurement(self._value_ + other._value_, self._delta_ + other._delta_)
    
    def __sub__(self, other):
        if not isinstance(other, Measurement):
            raise ValueError("Можно вычитать только измерения")
        return Measurement(self._value_ - other._value_, self._delta_ - other._delta_)
    