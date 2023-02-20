
# Этап 1
# Вычислитель кронекеровских произведений

first_str = input()


def kronecker_vec(vec1, vec2):

    vec_new = []

    for i in vec1:
        for j in vec2:
            vec_new += [i * j]
    return vec_new


def kronecker_matrix(matrix1, matrix2):

    global n, m
    matrix_new = [[0] * (n * m) for i in range(n * m)]

    for i1 in range(n):
        for j1 in range(n):
            for j2 in range(m):
                for i2 in range(m):
                    matrix_new[i2 + i1 * m][j2 + j1 * m] = matrix1[i1][j1] * matrix2[i2][j2]
    return matrix_new


if first_str == 'vector':
    n, m = (int(i) for i in input().split())

    vec1 = [int(i) for i in input().split()]
    vec2 = [int(i) for i in input().split()]

    # print(vec1, vec2)

    vec_new = kronecker_vec(vec1, vec2)
    for i in range(len(vec_new)):
        if i != n * m - 1:
            print(vec_new[i], end=' ')
        else:
            print(vec_new[i])

else:
    n, m = (int(i) for i in input().split())
    matrix1 = [[0]*n for i in range(n)]
    matrix2 = [[0]*m for i in range(m)]

    for i in range(n):
        matrix1[i] = [int(j) for j in input().split()]
    for i in range(m):
        matrix2[i] = [int(j) for j in input().split()]

    # print(matrix1)
    # print(matrix2)
    matrix_new = kronecker_matrix(matrix1, matrix2)
    for i in range(len(matrix_new)):
        for j in range(len(matrix_new)):
            if j != n * m - 1:
                print(matrix_new[i][j], end=' ')
            else:
                print(matrix_new[i][j])

