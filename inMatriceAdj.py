n = 5
M = [[1, 0, 1, 0, 0],
     [0, 1, 0, 1, 0],
     [1, 0, 0, 0, 1],
     [0, 1, 0, 0, 0],
     [0, 0, 1, 0, 1]]

for i in range(n):
    for j in range(n):
        if M[i][j] == 1:
            print(f"({i+1},{j+1}) ∈ A")
        else:
            print(f"({i+1},{j+1}) ∉ A")