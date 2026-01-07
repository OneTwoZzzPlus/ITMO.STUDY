import math
from .BaseMeasurement import *
from copy import deepcopy
CALC_ERROR = 16
# TODO MIN_ORDER, MAX_ORDER = -5, 5 in rounding

  
class Measurement(BaseMeasurement):
    def __init__(self, value: float, delta: float | None = None, 
                 epsilon: float | None = None, direct: bool = False, **kwargs):
        self._value = value
        self._delta = delta
        self._epsilon = epsilon
        self._is_direct = direct
        self._calc()

    @staticmethod
    def _soft(x):
        x = round(x, CALC_ERROR)
        return 0 if math.isclose(x, 0) else x

    def _calc(self):
        """ Ensures the availability of _delta_ and _epsilon_ """
        if self._epsilon is None and self._delta is None:
            self._epsilon = 0.0
            self._delta = 10**(1-CALC_ERROR)
        elif self._epsilon is None:
            self._delta = self._soft(abs(self._delta))
            if math.isclose(self._value, 0.0):
                self._epsilon = 0.0
            else:
                self._epsilon = (self._delta / abs(self._value) * 100.0)
        elif self._delta is None:
            self._epsilon = self._soft(abs(self._epsilon))
            self._delta = (self._epsilon * self._value / 100.0)
        
        self._value = self._soft(self._value)
        self._delta = self._soft(self._delta)
        self._epsilon = self._soft(self._epsilon)
        
        self._str_value, self._str_delta, self._str_epsilon = self._round_components()

    @staticmethod
    def round_error(x: float):
        """ Rounds error rate (_delta_ or _epsilon_) """
        # separating mantissa and exponenta 
        mem = format(x, '.3e').split('e')
        m, e = mem[0].replace('.', ''), int(mem[1])
        # counting of significant digits
        sign = 2 if m[0] in '123' else 1
        
        if m[sign] == '5':
            # rounding up if there are sign digits after '5'
            xm = x * 10**(-e+3)
            if xm - int(m) != 0:
                m = str(int(m) + 1)
        
        # rounding mantissa
        mant = (round(int(m), sign-4) // 100) / 10
        # assembling
        rounded_x = mant * 10**e
        # calculating round order
        order = sign - e - 1
        
        # print(x, m, e, sign, mant, rounded_x, order)
        
        return rounded_x, order

    def _round_components(self, N=0):
        """
            Rounds up according to the methodology
            Input (self._value, self._delta, self._epsilon)
            Return (str_value, str_delta, str_relative)
        """
        delta, value = self._delta / 10**N, self._value / 10**N
        
        # value + delta
        rounded_delta, order = self.round_error(delta)
        str_delta = format(rounded_delta, f'.{max(0, order)}f')
        rounded_value = round(value, order)
        str_value = format(rounded_value, f'.{max(0, order)}f')
        
        # relative
        rounded_epsilon, eps_order = self.round_error(self._epsilon)
        str_epsilon = format(rounded_epsilon, f'.{max(0, eps_order)}f')
        
        return str_value, str_delta, str_epsilon

    def format_result(self, N=0, cl=True, latex=False, include_rel=False):
        """ Форматирует вывод """
        sV, sD, sR = self._round_components(N)
        if latex:
            base = ('(' if cl else '') + f"{sV} \\pm {sD}" + (')' if cl else '')
            rel = f", \\varepsilon={sR}\\%" if include_rel and sR != "undefined" else (", \\varepsilon=undefined" if include_rel else "")
        else:
            base = f"{sV} ± {sD}"
            rel = f", ε={sR}%" if include_rel and sR != "undefined" else (", ε=undefined" if include_rel else "")
        return base + rel

    def format_std(self, N=0, cl=True): return self.format_result(N, cl, latex=False, include_rel=False)
    def format_rel(self, N=0, cl=True): return self.format_result(N, cl, latex=False, include_rel=True)
    def latex_std(self, N=0, cl=True): return self.format_result(N, cl, latex=True, include_rel=False)
    def latex_rel(self, N=0, cl=True): return self.format_result(N, cl, latex=True, include_rel=True)

    def format_value(self, N=0): return self._round_components(N)[0]
    def format_delta(self, N=0): return self._round_components(N)[1]
    def format_epsilon(self, N=0): return self._round_components(N)[2]

    @property
    def raw(self):
        return f"{self._soft(self._value)}, Δ = {self._soft(self._delta)}, ε = {self._soft(self._epsilon)}"
    
    @property
    def rounded(self):
        return f'{self.str_value}, Δ = {self.str_delta}, ε = {self.str_epsilon}'

    def __str__(self):
        return f'{self.rounded} ({self.raw})'
    
    def __repr__(self):
        return f'{self.rounded}'
    
    def __eq__(self, other): return self._value == other.value
    def __ne__(self, other): return not (self == other)
     
    def __gt__(self, other): return self._value > other.value
    def __le__(self, other): return not (self > other)
     
    def __lt__(self, other): return self._value < other.value
    def __ge__(self, other): return not (self < other)
    
    def __neg__(self):
        new_self = deepcopy(self)
        new_self._value = -self._value
        return new_self
    
    def __abs__(self):
        new_self = deepcopy(self)
        new_self._value = abs(self._value)
        return new_self
    
    def __add__(self, other):
        if isinstance(other, Measurement):
            return Measurement(
                self._value + other._value, 
                math.sqrt((self._idm * self._delta)**2 + (self._idm * other._delta)**2)
                )
        return NotImplemented("You can only add measurements")
        
    def __sub__(self, other):
        if isinstance(other, Measurement):
            return Measurement(
                self._value - other._value, 
                math.sqrt((self._idm * self._delta)**2 + (self._idm * other._delta)**2)
                )
        return NotImplemented("You can only subtract measurements")
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Measurement(
                self._value * other, 
                self._delta * other, 
                direct=self._is_direct
            )
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if math.isclose(other, 0):
                raise ZeroDivisionError()
            return Measurement(
                self._value / other, 
                self._delta / other, 
                direct=self._is_direct
            )
    