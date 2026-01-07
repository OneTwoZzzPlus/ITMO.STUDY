import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from .Measurement import *
from .MeasException import ExpressionError

def expression(measurements: list[Measurement], s: str, name='', char='', unit=''):
    # Создаем словарь для уникальных char (первый в приоритете)
    measurement_dict = {}
    for m in measurements:
        if m.char not in measurement_dict:
            measurement_dict[m.char] = m

    # Парсим выражение и проверяем корректность
    try:
        expr = parse_expr(s)
    except Exception as e:
        raise ExpressionError(f"Некорректный ввод выражения: {str(e)}")

    # Извлекаем переменные из выражения
    variables = expr.free_symbols
    var_names = [str(v) for v in variables]

    # Проверяем наличие всех переменных в измерениях
    for var in var_names:
        if var not in measurement_dict:
            raise ExpressionError(f"Неизвестная переменная: '{var}'")

    # Подготавливаем данные: значения, символы, погрешности
    symbols = {}
    values = {}
    deltas = {}
    for var in variables:
        var_str = str(var)
        m = measurement_dict[var_str]
        symbols[var_str] = var  # Символы уже созданы при парсинге
        values[var] = m.value_
        # Корректируем погрешность для прямых измерений
        deltas[var] = (2/3 * m.delta_) if m.is_direct else m.delta_

    # Вычисляем среднее значение выражения
    z_value = expr.subs(values).evalf()
    if isinstance(z_value, sp.core.numbers.NaN):
        raise ExpressionError("Невозможно вычислить значение выражения")

    # Вычисляем абсолютную погрешность по Способу 1
    delta_z_squared = 0
    for var in variables:
        derivative = sp.diff(expr, var)
        derivative_value = derivative.subs(values).evalf()
        delta = deltas[var]
        delta_z_squared += (derivative_value * delta) ** 2

    delta_z = sp.sqrt(delta_z_squared)
    epsilon_z = (delta_z / z_value) * 100 if z_value != 0 else float('inf')

    # Возвращаем результат
    return Measurement(
        value=float(z_value),
        delta=float(delta_z),
        epsilon=float(epsilon_z),
        name=name,
        char=char,
        unit=unit
    )