from .MeasException import *
    
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