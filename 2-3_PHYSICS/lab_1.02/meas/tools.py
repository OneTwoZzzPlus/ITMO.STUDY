from math import *

def soft(x):
    CALC_ERROR = 12
    x = round(x, CALC_ERROR)
    return 0 if isclose(x, 0) else x


def get_first_significant_digit(n):
    if n == 0:
        return 0
    n_abs = abs(n)
    s = "{:.15e}".format(n_abs)
    mantissa_part, exp_part = s.split('e')
    mantissa = mantissa_part.replace('.', '').lstrip('0')
    return int(mantissa[0]) if mantissa else 0

def round_to_significant(value, significant):
    if value == 0:
        return 0.0
    formatted = "{:.{prec}e}".format(value, prec=significant-1)
    return float(formatted)

def phys_round(value):
    first_digit = get_first_significant_digit(value)
    k_delta_x = 2 if first_digit in {1, 2, 3} else 1
    return round_to_significant(value, k_delta_x)

def format_with_decimals(number, decimals):
    # Форматируем число с фиксированным количеством знаков после запятой
    return ("{0:." + str(decimals) + "f}").format(number)
        
        
def round_measurement(x, delta_x, delta_rel=None):
    # Обработка абсолютной погрешности
    first_digit = get_first_significant_digit(delta_x)
    k_delta_x = 2 if first_digit in {1, 2, 3} else 1
    rounded_delta_x = round_to_significant(delta_x, k_delta_x)
    
    # Определение порядка округления для x
    formatted_delta = "{:.{prec}e}".format(rounded_delta_x, prec=k_delta_x-1)
    mantissa, exp_part = formatted_delta.split('e')
    exp = int(exp_part)
    order = 10 ** (exp - (k_delta_x - 1))
    
    rounded_x = round(x / order) * order if order != 0 else x
    
    # Обработка относительной погрешности
    rounded_delta_rel = None
    if delta_rel is not None:
        first_digit_rel = get_first_significant_digit(delta_rel)
        k_delta_rel = 2 if first_digit_rel in {1, 2, 3} else 1
        rounded_delta_rel = round_to_significant(delta_rel, k_delta_rel)
    
    # return (rounded_x, rounded_delta_x, rounded_delta_rel) if delta_rel is not None else (rounded_x, rounded_delta_x)
    # ИЗМЕНЕНО! Добавлен soft на окгругление!
    if delta_rel is not None:
        return soft(rounded_x), soft(rounded_delta_x), soft(rounded_delta_rel)
    else:
        return soft(rounded_x), soft(rounded_delta_x)

def format_measurement(x, delta_x, latex=True):
    # Обработка абсолютной погрешности
    first_digit = get_first_significant_digit(delta_x)
    k_delta = 2 if first_digit in {1, 2, 3} else 1
    rounded_delta = round_to_significant(delta_x, k_delta)
    
    # Определяем порядок округления для x
    delta_str = "{:.{}e}".format(rounded_delta, k_delta-1)
    mantissa_part, exp_part = delta_str.split('e')
    exponent = int(exp_part)
    step = 10 ** (exponent - (k_delta - 1))
    
    # Округляем x до нужного шага
    rounded_x = round(x / step) * step
    
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
    
    return f"{x_str}{'\\pm' if latex else '±'}{delta_str}"