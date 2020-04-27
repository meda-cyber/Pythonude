matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]


def add(matrix1, matrix2):
    combined = []

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
            combined.append(row)

    return combined
