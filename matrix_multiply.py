







def get_row(matrix, n_row):
    return matrix[n_row]


def get_column(matrix, n_col):
    column = []

    for row in matrix:
        column.append(row[n_col])

    return column


def get_dot_product(v1, v2):
    zipped = zip(v1, v2)
    return sum([i*j for i,j in zipped])


def matrix_multiplication(matrixA, matrixB):
    m_rows = len(matrixA)
    p_columns = len(matrixB[0])
    
    result = []

    for r in range(0, m_rows):
        prod_row = []
        
        for c in range(0, p_columns):
            row_vector = get_row(matrixA, r)
            col_vector = get_column(matrixB, c)
            dot_product = get_dot_product(row_vector, col_vector)
            prod_row.append(dot_product)
        
        result.append(prod_row)
    
    return result



### TODO: Run this code cell to test your results
assert matrix_multiplication([[5], [2]], [[5, 1]]) == [[25, 5], [10, 2]]
assert matrix_multiplication([[5, 1]], [[5], [2]]) == [[27]]
assert matrix_multiplication([[4]], [[3]]) == [[12]]
assert matrix_multiplication([[2, 1, 8, 2, 1], [5, 6, 4, 2, 1]], [[1, 7, 2], [2, 6, 3], [3, 1, 1], [1, 20, 1], [7, 4, 16]]) == [[37, 72, 33], [38, 119, 50]]