from geometric_objects import Line, Vector 


# Ax + By = k
# 4.046x + 2.836y = 1.21
# 10.115x + 7.09y = 3.025
line1 = Line(
    normal_vector=Vector([4.046, 2.836]), 
    constant_term=1.21
)

line2 = Line(
    normal_vector=Vector([10.115, 7.09]), 
    constant_term=3.025
)

print('Intersection', line1.find_intersection_with(line2))
print('Is equal', line1.is_equal_to(line2))