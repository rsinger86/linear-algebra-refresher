"""
This module defines a class that represents vector as a mathematical object.
"""

import math


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


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
            summed.append(self.coordinates[i]-val)

        return Vector(summed) 


    def times_scalar(self, v):
        multiplied = []

        for val in self.coordinates:
            multiplied.append(val*v)

        return Vector(multiplied) 


    def find_magnitude(self):
        sum_of_squares = sum([val*val for val in self.coordinates])
        return math.sqrt(sum_of_squares)


    def normalize(self):
        """
            Returns vector's direction.
        """
        magnitude = self.find_magnitude()
        inverted = (1/magnitude)
        normalized = [inverted*val for val in self.coordinates]
        return Vector(normalized)


    def calc_dot_product(self, other_vector):
        """
            Returns inner product with another vector.
        """
        zipped = zip(self.coordinates, other_vector.coordinates)
        return sum([i*j for i, j in zipped])


    def calc_dot_product_angle(self, other_vector, unit='radian'):
        """
            Utilizes dot product to calculate angle with anotther vector.
        """
        dot_product = self.calc_dot_product(other_vector)

        radians = math.acos(
            dot_product /
            (self.find_magnitude() * other_vector.find_magnitude())
        )

        if unit == 'radian':
            return radians

        return math.degrees(radians)


    def is_parallel(self, other_vector):
        """
            Checks with this vector is parallel with anotther vector.
        """
        if self.is_zero() or other_vector.is_zero():
            return True

        divide_results = []

        for i, val in enumerate(other_vector.coordinates):
            divide_results.append(other_vector.coordinates[i] / self.coordinates[i])

        return len(set(divide_results)) == 1

    
    def is_zero(self, tolerate=1e-10):
        return self.find_magnitude() < tolerate


    def is_orthogonal(self, v, tolerate=1e-10):
        return abs(self.calc_dot_product(v)) < tolerate


    def get_orthogonal_to_vector(self, basis_vector):
        """
            Since this vector = parallel vector + orthogonal vector....
        """
        return self.minus(
            self.get_parallel_to_vector(basis_vector)
        )


    def get_parallel_to_vector(self, basis_vector):
        """
            Parallel vector, aka the projecion of this vector onto the basis vector,
            is equal to the dot product of this vector and the normalized basis vector,
            times scalar the normalized basis vector.
        """
        unit_vector = basis_vector.normalize()
        weight = self.calc_dot_product(unit_vector)
        return unit_vector.times_scalar(weight)


    def get_cross_product(self, other_vector):
        """
            Returns the cross product of vector with this vector.
        """
        v = self.coordinates
        w = other_vector.coordinates 

        return Vector([
            (v[1] * w[2]) - (w[1] * v[2]),
            -((v[0] * w[2]) - (w[0] * v[2])),
            (v[0] * w[1]) - (w[0] * v[1])
        ])


