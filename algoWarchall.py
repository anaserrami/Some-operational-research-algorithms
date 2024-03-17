n = 5
M = [[0, 1, 0, 0, 0],
     [0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 1, 1, 0]]

for i in range(n):
    for j in range(n):
        if M[i][j] == 1:
            for k in range(n):
                if M[j][k] == 1:
                    M[i][k] = 1

new_M = []
for row in M:
    new_M.append(str(row))
M_str = "[" + ",\n ".join(new_M) + "]"
print(M_str)