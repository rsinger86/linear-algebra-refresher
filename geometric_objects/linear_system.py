from decimal import Decimal, getcontext
from copy import deepcopy
from vector import Vector
from plane import Plane
from geometric_objects import MyDecimal

getcontext().prec = 30


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def swap_rows(self, row1, row2):
        plane1, plane2 = self.planes[row1], self.planes[row2]
        self.planes[row2] = plane1
        self.planes[row1] = plane2


    def multiply_coefficient_and_row(self, coefficient, row):
        plane = self.planes[row]
        new_coordinates = [v*coefficient for v in plane.normal_vector.coordinates]

        self.planes[row] = Plane(
            normal_vector=Vector(new_coordinates), 
            constant_term=plane.constant_term * coefficient
        )


    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        plane_to_add = self.planes[row_to_add]
        add_coordinates = [v*coefficient for v in plane_to_add.normal_vector.coordinates]
        add_constant_term = plane_to_add.constant_term * coefficient
        modified_plane = self.planes[row_to_be_added_to]

        self.planes[row_to_be_added_to] = Plane(
            normal_vector=Vector([
                i+j for i, j in 
                zip(add_coordinates, modified_plane.normal_vector.coordinates)
            ]), 
            constant_term=modified_plane.constant_term + add_constant_term
        )



    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector.coordinates)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices


    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]


    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


    def swap_with_row_below_for_nonzero_coefficient_if_able(self, row, col):
        num_equations = len(self)

        for k in range(row+1, num_equations):
            coefficient = MyDecimal(self[k].normal_vector[col])
            if not coefficient.is_near_zero():
                self.swap_rows(row, k)
                return True 
        
        return False
            

    def clear_coefficients_below(self, row, col):
        num_equations = len(self)
        beta = MyDecimal(self[row].normal_vector[col])

        for k in range(row+1, num_equations):
            n = self[k].normal_vector
            gamma = n[col]
            alpha = -gamma/beta
            self.add_multiple_times_row_to_row(alpha, row, k)


    def compute_triangular_form(self):
        ## Do not use multiply_coeffecient_and_row
        ## Swap with top-most row below current row
        ## Only add multiples of rows to rows underneath
        ## p0 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
        ## p1 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
        ## p2 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
        ## p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
        ## indices_of_first_nonzero_terms_in_each_row
        system = deepcopy(self)

        num_equations = len(system)
        num_variables = system.dimension

        j = 0
        for i in range(num_equations):
            while j < num_variables:
                c = MyDecimal(system[i].normal_vector[j])

                if c.is_near_zero():
                    swap_succeeded = system.swap_with_row_below_for_nonzero_coefficient_if_able(i, j)
                    if not swap_succeeded:
                        j += 1
                        continue 

                system.clear_coefficients_below(i, j)
                j += 1
                break 
        
        return system


    def clear_coefficients_above(self, row, col):
        if row == 0:
            return

        num_equations = len(self)
        beta = MyDecimal(self[row].normal_vector[col])

        for k in range(row)[::-1]:
            n = self[k].normal_vector
            gamma = n[col]
            alpha = -gamma/beta
            self.add_multiple_times_row_to_row(alpha, row, k)


    def compute_rref(self):
        tf = self.compute_triangular_form()

        num_equations = len(tf)
        pivot_indices = tf.indices_of_first_nonzero_terms_in_each_row()

        for row in range(num_equations)[::-1]:
            pivot_var = pivot_indices[row]
            if pivot_var < 0:
                continue
            tf.scale_row_to_make_coefficient_equal_one(row, pivot_var)
            tf.clear_coefficients_above(row, pivot_var)

        return tf

    def scale_row_to_make_coefficient_equal_one(self, row, col):
        n = self[row].normal_vector
        beta = Decimal('1.0') / n[col]
        self.multiply_coefficient_and_row(beta, row)


    def raise_exception_if_contradictory_equation(self):
        # if 0 == K, where K is non-zero
        for p in self.planes:
            try:
                p.first_nonzero_index(p
                )
            except Exception as e:
                if str(e) == 'No nonzero elements found':
                    constant_term = MyDecimal(p.constant_term)

                    if not constant_term.is_near_zero():
                        raise Exception('No solutions found')
                else:
                    raise e 


    def raise_exception_if_too_few_pivots(self):
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        num_pivots = sum([1 if index >= 0 else 0 for index in pivot_indices])
        num_variables = self.dimension

        if num_pivots < num_variables:
            raise Exception('Infinite solutions')


    def do_gaussian_elimination_and_extract_solution(self):
        rref = self.compute_rref()
        
        rref.raise_exception_if_contradictory_equation()
        rref.raise_exception_if_too_few_pivots()

        num_variables = rref.dimension

        solution_coordinates = [
            rref.planes[i].constant_term for i in 
            range(num_variables)
        ]

        return Vector(solution_coordinates)


    def compute_solution(self):
        try:
            return self.do_gaussian_elimination_and_extract_solution()
        except Exception as e:
            return str(e)


    def get_parametrization(self):
        basepoint_vector = self.get_parametrization_basepoint()
        direction_vectors = self.get_parametrization_direction_vectors()
        return basepoint_vector 

    def get_parametrization_direction_vectors(self):
        rref = self.compute_rref()
        direction_vectors = []
        non_zeroindices = rref.indices_of_first_nonzero_terms_in_each_row()
        free_vars = set([0,1,2]) - set(non_zeroindices)
        num_free_vars = len(free_vars)

        for free_var in free_vars:
            print('hi')



    def get_parametrization_basepoint(self):
        rref = self.compute_rref()
        coordinates = [0] * 3
        nonzero_indices = rref.indices_of_first_nonzero_terms_in_each_row()

        for i, non_zeroindex in enumerate(nonzero_indices):
            coordinates[non_zeroindex] = rref.planes[i].constant_term
        
        return Vector(coordinates)



class Parametrization(object):

    BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM = (
        'The basepoint and direction vectors should all live in the same '
        'dimension')

    def __init__(self, basepoint, direction_vectors):

        self.basepoint = basepoint
        self.direction_vectors = direction_vectors
        self.dimension = self.basepoint.dimension

        try:
            for v in direction_vectors:
                assert v.dimension == self.dimension

        except AssertionError:
            raise Exception(self.BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM)

    def __str__(self):

        output = ''
        for coord in range(self.dimension):
            output += 'x_{} = {} '.format(coord + 1,
                                          round(self.basepoint[coord], 3))
            for free_var, vector in enumerate(self.direction_vectors):
                output += '+ {} t_{}'.format(round(vector[coord], 3),
                                             free_var + 1)
            output += '\n'
        return output