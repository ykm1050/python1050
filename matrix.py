def matrix():
    matrix = [[0 for _ in range(4)] for _ in range(4)]
    matrix[0][1] = 1
    matrix[1][3] = 1
    matrix[2][0] = 1
    matrix[3][2] = 1
    for row in matrix:
        print(" ".join(str(cell) for cell in row))
matrix()
