import math 
from decimal import Decimal, getcontext


getcontext().prec = 30


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(c) for c in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __len__(self):
        return len(self.coordinates)

    def __getitem__(self, i):
        return self.coordinates[i]

    def __str__(self):
        return 'Vector: {}'.format([round(coord, 3)
                                    for coord in self.coordinates])

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    
    def plus(self, v):
        summed = []

        for i, val in enumerate(v.coordinates):
            summed.append(val+self.coordinates[i])

        return Vector(summed) 

    
    def minus(self, v):
        summed = []
    
        for i, val in enumerate(v.coordinates):
            summed.append( self.coordinates[i] - val )

        return Vector(summed) 


    def times_scalar(self, v):
        multiplied = []

        for val in self.coordinates:
            multiplied.append(val*v)

        return Vector(multiplied) 


    def find_magnitude(self):
        sum_of_squares = sum([val*val for val in self.coordinates])
        return Decimal(math.sqrt(sum_of_squares))


    def normalize(self):
        try:
            return self.times_scalar(Decimal('1.0') / self.find_magnitude())
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')


    def calc_dot_product(self, other):
        return sum(x * y for x, y in zip(self.coordinates, other.coordinates))


    def calc_dot_product_angle(self, other, unit='radian'):
        dot_prod = round(self.normalize().calc_dot_product(other.normalize()), 3)
        radians = math.acos(dot_prod)

        if unit == 'radian':
            return radians

        return math.degrees(radians)


    def is_parallel_to(self, v):
        if self.is_zero() or v.is_zero():
            return True 
        
        return (
            self.calc_dot_product_angle(v) == 0 or 
            self.calc_dot_product_angle(v) == math.pi
        )

    
    def is_zero(self, tolerate=1e-10):
        return self.find_magnitude() < tolerate


    def is_orthogonal_to(self, v, tolerate=1e-10):
        return abs(self.calc_dot_product(v)) < tolerate


    def get_projected_vector(self, basis_vector):
        unit_vector = basis_vector.normalize()
        weight = self.calc_dot_product(unit_vector)
        return unit_vector.times_scalar(weight)
