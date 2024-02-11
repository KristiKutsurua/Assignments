matrix = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]

result_matrix = []

for i in range(len(matrix)):
    row = []
    for j in range(len(matrix[0])):
        row.append(matrix[j][i])
    result_matrix.append(row)

for row in result_matrix:
    print(row)    

