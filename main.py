from geometric_objects import Line, Vector, Plane


# Vector([-0.412, 3.806, 0.728]) -3.46
# Vector([1.03, -9.515, -1.82]) 8.65
# Vector([2.611, 5.528, 0.283]) 4.6
# Vector([7.715, 8.306, 5.342]) 3.76
# Vector([-7.926, 8.625, -7.217]) -7.952
# Vector([-2.642, 2.875, -2.404]) -2.443

plane1 = Plane(
    normal_vector=Vector([-7.926, 8.625, -7.212]), 
    constant_term=-7.952
)

plane2 = Plane(
    normal_vector=Vector([-2.642, 2.875, -2.404]), 
    constant_term=-2.443
)


print('is_equal_to', plane1.is_equal_to(plane2))
print('is_parallel_to', plane1.is_parallel_to(plane2))