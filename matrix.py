

def transpose(matrix: list):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j >= i:
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
    return matrix


def flip(matrix: list):
    for j in range(int(len(matrix) / 2)):
        for i in range(len(matrix)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][len(matrix) - 1 - j]
            matrix[i][len(matrix) - 1 - j] = temp
    return matrix


def rotate(matrix: list):
    matrix_size = len(matrix) - 1
    for i in range(len(matrix) // 2):
        for j in range(i, matrix_size - i):
            matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][
                ~i] = matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]
    return matrix
