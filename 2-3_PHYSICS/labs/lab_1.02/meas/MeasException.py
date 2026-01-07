class MeasException(BaseException):
    pass
    
class ExpressionError(MeasException):
    pass
    
class StudentException(MeasException):
    def __init__(self, N: int):
        self.N = N
        super().__init__(f"Отсутствует коэффициент Стьюдента N = {N}!")