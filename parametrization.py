import sys
from decimal import Decimal
from geometric_objects import (
    Line, 
    Vector, 
    Plane, 
    LinearSystem, 
    MyDecimal
)


p1 = Plane(normal_vector=Vector(['0.786', '0.786', '0.588']), constant_term='-0.714')
p2 = Plane(normal_vector=Vector(['-0.138', '-0.138', '0.244']), constant_term='0.319')
s = LinearSystem([p1,p2])
r = s.get_parametrization()
print(r)