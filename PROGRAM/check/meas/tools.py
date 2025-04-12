from .MeasException import *
from math import *
from datetime import datetime

class Tools:
    @property
    def latex(self):
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
            
        latex_pm = '\\pm'
        return f"${x_str}{latex_pm}{delta_str}$"
    
    def phys_round(self, value):
        first_digit = self._get_first_significant_digit(value)
        k_delta_x = 2 if first_digit in {1, 2, 3} else 1
        return self._round_to_significant(value, k_delta_x)
    
    
def timer(method_to_decorate):

    def wrapper(self, *args, **kwargs):
        start = datetime.now()
        res = method_to_decorate(self, *args, **kwargs)
        finish = datetime.now() - start
        print("Время выполнения =", finish)
        return res

    return wrapper


def check_len(method_to_decorate):
    
    def wrapper(self, m1, m2, *args):
        if not isinstance(m1, list) or not isinstance(m2, list):
            raise MeasException('Передай список!')
        if len(m1) == 0 or len(m2) == 0:
            raise MeasException('Пустые данные!')
        if len(m1) != len(m2):
            raise MeasException('Разные размеры массивов данных!')
        first_type = type(m1[0])
        if any(type(x) != first_type for x in m1) or any(type(x) != first_type for x in m2):
            raise MeasException('Разные типы данных в массивах!')
        
        return method_to_decorate(self, m1, m2, *args)

    return wrapper