"""
O(n^3)
Умножение матриц
"""
def multiply_matrices(matrix1: list[list[int]], matrix2: list[list[int]]):
    result = []
    m, n, p = len(matrix1), len(matrix2[0]), len(matrix2)

    for i in range(m):
        result.append([])
        for j in range(n):
            result[i].append(0)
            for k in range(p):
                result[i][j] += matrix1[i][k] * matrix2[k][j];
    return result


# Случайные матрицы
from random import randint
from pprint import pprint
n = 5

matrixA = [[randint(0, 1000) for _ in range(n)] for _ in range(n)]
matrixB = [[randint(0, 1000) for _ in range(n)] for _ in range(n)]
# a = map(int, input().split())
print('Исходные:')
pprint(matrixA)
pprint(matrixB)
print('Результат')
pprint(multiply_matrices(matrixA, matrixB))

