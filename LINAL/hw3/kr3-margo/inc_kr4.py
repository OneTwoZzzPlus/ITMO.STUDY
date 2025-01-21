import numpy as np
from sympy import *

# Исходные векторы
v1 = np.array([-1, 1, 2, 1], dtype=float)
v2 = np.array([2, -3, -5, -3], dtype=float)
v3 = np.array([4, -5, -9, -5], dtype=float)


# Функция для ортогонализации Грама-Шмидта
def gram_schmidt(vectors):
    orthogonal = []
    for v in vectors:
        w = v - sum(np.dot(v, u) / np.dot(u, u) * u for u in orthogonal)
        orthogonal.append(w)
    return orthogonal


# Функция для нормализации
def normalize(vectors):
    return [v / np.linalg.norm(v) for v in vectors]


# Ортогонализация и нормализация
vectors = [v1, v2, v3]
orthogonal = gram_schmidt(vectors)
orthonormal = normalize(orthogonal)

# Преобразование векторов в массивы с округлением
orthonormal = [np.round(vec, 5) for vec in orthonormal]
print(orthonormal)

print(', '.join(str(y) for y in orthonormal[0]))

print(f"[{'; '.join((', '.join(str(y) for y in x)) for x in orthonormal)}]")

