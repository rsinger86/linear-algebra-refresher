### TODO: Write a function called transpose() that 
###       takes in a matrix and outputs the transpose of the matrix

def transpose(matrix):
    matrix_transpose = []
    
    for c in range(0, len(matrix[0])):
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[c])
        
        matrix_transpose.append(transposed_row)

    return matrix_transpose


def get_dot_product(v1, v2):
    zipped = zip(v1, v2)
    return sum([i*j for i,j in zipped])


def matrix_multiplication(matrixA, matrixB):
    product = []
    transposed_b = transpose(matrixB)

    for a_row in matrixA:
        prod_row = []
        for b_row in transposed_b:
            prod_row.append(
                get_dot_product(b_row, a_row)
            )
        product.append(prod_row)

    return product


assert transpose([[5, 4, 1, 7], [2, 1, 3, 5]]) == [[5, 2], [4, 1], [1, 3], [7, 5]]
assert transpose([[5]]) == [[5]]
assert transpose([[5, 3, 2], [7, 1, 4], [1, 1, 2], [8, 9, 1]]) == [[5, 7, 1, 8], [3, 1, 1, 9], [2, 4, 2, 1]]




assert matrix_multiplication([[5, 3, 1], 
                              [6, 2, 7]], 
                             [[4, 2], 
                              [8, 1], 
                              [7, 4]]) == [[51, 17], 
                                           [89, 42]]

assert matrix_multiplication([[5]], [[4]]) == [[20]]

assert matrix_multiplication([[2, 8, 1, 2, 9],
                             [7, 9, 1, 10, 5],
                             [8, 4, 11, 98, 2],
                             [5, 5, 4, 4, 1]], 
                             [[4], 
                              [2], 
                              [17], 
                              [80], 
                              [2]]) == [[219], [873], [8071], [420]]


assert matrix_multiplication([[2, 8, 1, 2, 9],
                             [7, 9, 1, 10, 5],
                             [8, 4, 11, 98, 2],
                             [5, 5, 4, 4, 1]], 
                             [[4, 1, 2], 
                              [2, 3, 1], 
                              [17, 8, 1], 
                              [1, 3, 0], 
                              [2, 1, 4]]) == [[61, 49, 49], [83, 77, 44], [329, 404, 39], [104, 65, 23]]
