class MeasException(BaseException):
    pass
    
class StudentException(BaseException):
    def __init__(self, N: int):
        self.N = N
        super().__init__(f"Отсутствует коэффициент Стьюдента N = {N}!")
        
class ExpressionError(BaseException):
    pass