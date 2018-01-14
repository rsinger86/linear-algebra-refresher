from entities import Vector 


#v = Vector([3.039, 1.879])
#bv = Vector([0.825, 2.036])

#print( v.get_projected_vector(bv) )

#v = Vector([-9.88, -3.264, -8.159])
#bv = Vector([-2.155, -9.353, -9.473])

#projected_vector = v.get_projected_vector(bv)

#print(v.minus(projected_vector))

# v - projected vector = orthogonal vector

#v = Vector([3.009, -6.172, 3.692, -2.51])
#bv = Vector([6.404, -9.144, 2.759, 8.718])

#projected_vector = v.get_projected_vector(bv)

#print(projected_vector)

#print(v.minus(projected_vector))

v = Vector([
    1.5,
    9.547,
    3.691
])

w = Vector([
    -6.007,
    0.124,
    5.772
])


cp = v.get_cross_product(w)
print(cp.find_magnitude() / 2)