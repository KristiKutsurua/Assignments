matrix1 = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]

matrix2 = [
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
]

result_matrix = []

for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix1[0])):
        row.append(matrix1[i][j] + matrix2[i][j])
    result_matrix.append(row)

for row in result_matrix:
    print(row)    

