def matrix():
    matrix = [[0 for _ in range(8)] for _ in range(8)]
    matrix[0][3] = 1
    matrix[1][5] = 1
    matrix[2][7] = 1
    matrix[3][1] = 1
    matrix[4][4] = 1
    matrix[5][1] = 1
    matrix[6][2] = 1
    matrix[7][6] = 1
    for row in matrix:
        print(" ".join(str(cell) for cell in row))
matrix()


def matrix():
    matrix = [[0 for _ in range(4)] for _ in range(4)]
    matrix[0][1] = 1
    matrix[1][3] = 1
    matrix[2][0] = 1
    matrix[3][2] = 1
    for row in matrix:
        print(" ".join(str(cell) for cell in row))
matrix()


def matrix():
    matrix = [[0 for _ in range(8)] for _ in range(8)]
    matrix