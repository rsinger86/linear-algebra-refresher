# num col 



def identity_matrix(size):
    identity = []
    one_col = 0

    for i in range(0, size):
        row = []

        for j in range(0, size):
            v = 1 if j == one_col else 0
            row.append(v)
            
        identity.append(row)
        one_col += 1
    
    return identity



assert identity_matrix(1) == [[1]]

assert identity_matrix(2) == [[1, 0], 
                             [0, 1]]

assert identity_matrix(3) == [[1, 0, 0],
                             [0, 1, 0],
                             [0, 0, 1]]

assert identity_matrix(4) == [[1, 0, 0, 0],
                             [0, 1, 0, 0],
                             [0, 0, 1, 0],
                             [0, 0, 0, 1]]