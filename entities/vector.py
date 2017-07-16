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
        magnitude = self.find_magnitude() 
        inverted = (1/magnitude)
        normalized = [inverted*val for val in self.coordinates]
        return normalized


    def calc_dot_product(self, v):
        zipped = zip(self.coordinates, v.coordinates)
        return sum([i*j for i,j in zipped])


    def calc_dot_product_angle(self, v, unit='radian'):
        dot_product = self.calc_dot_product(v)

        radians = math.acos(
            dot_product / 
            (self.find_magnitude() * v.find_magnitude())
        )

        if unit == 'radian':
            return radians 

        return math.degrees(radians)