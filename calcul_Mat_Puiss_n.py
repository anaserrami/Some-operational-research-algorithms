n = 5
M = [[0, 1, 0, 0, 0],
     [0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 1, 1, 0]]

# function to compute matrix product
def matrix_product(A, B):
    n = len(A)
    C = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = C[i][j] or (A[i][k] and B[k][j])
    return C

# compute matrix powers
M_powers = [M]
for i in range(2, n+1):
    M_powers.append(matrix_product(M_powers[i-2], M))

# print matrix powers
for i in range(n-1):
    print("M^{} = {}".format(i+1, M_powers[i]))