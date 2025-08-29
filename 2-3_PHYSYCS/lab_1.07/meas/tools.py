from .MeasException import *
from math import *
from datetime import datetime

class Tools:
    def phys_round(self, value):
        first_digit = self._get_first_significant_digit(value)
        k_delta_x = 2 if first_digit in {1, 2, 3} else 1
        return self._round_to_significant(value, k_delta_x)
    
    def latex(self, dim=1):
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
        x_str = self._format_with_decimals(rounded_x * 10**dim, decimals - dim)
        delta_str = self._format_with_decimals(rounded_delta * 10**dim, decimals - dim)
        
        # Убираем лишние точки для целых чисел
        if decimals == 0:
            x_str = x_str.split('.')[0]
            delta_str = delta_str.split('.')[0]
            
        latex_pm = '\\pm'
        
        if x_str[-1] == '0' and delta_str[-1] == '0':
            x_str, delta_str = x_str[:-1], delta_str[:-1]
        
        return f"{x_str}{latex_pm}{delta_str}"
    
    def latex_m(self, dim=0):
        return f'${self.latex(dim=dim)}$'
    
    def meas_latex(self, dim=0):
        name, unit = self._char, self._unit
        return f"\\centerline{{${name} = ({self.latex(dim)}){f'\\cdot 10^{{{-dim}}}' if dim != 0 else ''} {unit}, \\quad \\varepsilon = {self.epsilon} \\%, \\quad \\alpha = 0.95$}}"
    
    def value_latex(self, dim=0, hide_char=False):
        name, unit = "" if hide_char else f"{self._char} = ", self._unit
        return f"{name}({self.latex(dim)}){f'\\cdot 10^{{{-dim}}}' if dim != 0 else ''} {unit}"
    
    def value_latex_m(self, dim=0):
        return f"${self.value_latex(dim=dim)}$"

    def DDM(self):
        ch = self._char
        return (
            f"$\\bar{{{ch}}} = {self.value} {self._unit}$.\n\n" +
            f"\\centerline{{$\\sigma_{{\\bar{{{ch}}}}} = {self._sigma_}, \quad " +
            f"\\Delta_{{\\bar{{{ch}}}}} = {self._student} \\cdot {self._sigma_} = {self._delta_random_} {self._unit}$}}\n\n" +
            f"\\centerline{{$\\Delta_{{{ch}}} = \sqrt{{({self._delta_random_})^2 + (\\frac{2}{3} \\cdot {self._delta_instrumental_})^2}} = {self.delta} {self._unit}, \quad " +
            f"\\varepsilon_{{{ch}}} = \\frac{{{self.delta}}}{{{self.value}}} \\cdot 100\\% = {self.epsilon}\%$}}"
        )
    
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