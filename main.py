from entities import Vector 



v1 = Vector([8.218,-9.341])
v2 = Vector([-1.129,2.111])

v3 = Vector([7.119, 8.215])
v4 = Vector([-8.223,0.878])

v5 = Vector([1.671, -1.012, -0.318])

v6 = Vector([-0.221, 7.437])
v7 = Vector([8.813, -1.331, -6.247])

v8 = Vector([7.35, 0.221, 5.188])
v9 = Vector([2.751, 8.259, 3.985])

print(v8.calc_dot_product_angle(v9, unit='degree'))

