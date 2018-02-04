from decimal import Decimal, getcontext
getcontext().prec = 30


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps


from .vector import Vector
from .line import Line
from .plane import Plane
from .linear_system import LinearSystem