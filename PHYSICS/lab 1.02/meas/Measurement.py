from math import *
from .tools import * 

  
class Measurement:
    value: float    # окр. значение
    value_: float   # значение
    delta: float    # окр. абсолютная
    delta_: float   # абсолютная
    epsilon: float  # окр. относительная
    epsilon_: float # относительная

    def __init__(self, value, delta, epsilon=None):
        self.value_ = value
        self.delta_ = delta
        self.epsilon_ = (delta / value * 100)  if epsilon is None else epsilon
        self.round()

    def round(self):
        # Обработка абсолютной погрешности
        first_digit = get_first_significant_digit(self.delta_)
        k_delta_x = 2 if first_digit in {1, 2, 3} else 1
        rounded_delta_x = round_to_significant(self.delta_, k_delta_x)
        
        # Определение порядка округления для x
        formatted_delta = "{:.{prec}e}".format(rounded_delta_x, prec=k_delta_x-1)
        mantissa, exp_part = formatted_delta.split('e')
        exp = int(exp_part)
        order = 10 ** (exp - (k_delta_x - 1))
        
        rounded_x = round(self.value_ / order) * order if order != 0 else self.value_
        
        # Обработка относительной погрешности
        rounded_delta_rel = None

        first_digit_rel = get_first_significant_digit(self.epsilon_)
        k_delta_rel = 2 if first_digit_rel in {1, 2, 3} else 1
        rounded_delta_rel = round_to_significant(self.epsilon_, k_delta_rel)
        
        # ИЗМЕНЕНО! Добавлен soft на окгругление!
        self.value = soft(rounded_x)
        self.delta = soft(rounded_delta_x)
        self.epsilon = soft(rounded_delta_rel)

    def format(self, latex=True):
        # Обработка абсолютной погрешности
        first_digit = get_first_significant_digit(self.delta_)
        k_delta = 2 if first_digit in {1, 2, 3} else 1
        rounded_delta = round_to_significant(self.delta_, k_delta)
        
        # Определяем порядок округления для x
        delta_str = "{:.{}e}".format(rounded_delta, k_delta-1)
        mantissa_part, exp_part = delta_str.split('e')
        exponent = int(exp_part)
        step = 10 ** (exponent - (k_delta - 1))
        
        # Округляем x до нужного шага
        rounded_x = round(self.value_ / step) * step
        
        # Определяем количество знаков после запятой
        if step < 1:
            decimals = -int(log10(step))
        else:
            decimals = 0
        
        # Форматируем с сохранением всех нулей
        x_str = format_with_decimals(rounded_x, decimals)
        delta_str = format_with_decimals(rounded_delta, decimals)
        
        # Убираем лишние точки для целых чисел
        if decimals == 0:
            x_str = x_str.split('.')[0]
            delta_str = delta_str.split('.')[0]
            
        char_pm, latex_pm = '±', '\\pm'
        return f"{x_str}{latex_pm if latex else char_pm}{delta_str}"
    
    @property
    def rounded(self):
        # Для дебага округлённых значений
        return f"{self.format(False)} ε = {self.epsilon}"
    
    @property
    def raw(self):
        # Для дебага сырых значений
        return f"{soft(self.value_)} Δ = {soft(self.delta_):.9f} ε = {soft(self.epsilon_):.9f}"
    
    def __str__(self):
        return f'{self.rounded} ({self.raw})'
    
    def __repr__(self):
        return f'{self.rounded}'
    
    def __eq__(self, other): return self.value == other.value
    def __ne__(self, other): return not (self == other)
     
    def __gt__(self, other): return self.value > other.value
    def __le__(self, other): return not (self > other)
     
    def __lt__(self, other): return self.value < other.value
    def __ge__(self, other): return not (self < other)