# Ввод точек
A = (1, 8, -4)
B = (2, 4, -4)
C = (3, 5, -5)


# Строим 2 вектора
a = (A[0]-B[0], A[1]-B[1], A[2]-B[2])
b = (A[0]-C[0], A[1]-C[1], A[2]-C[2])

# Скалярное произведение
p = sum(a[i]*b[i] for i in range(len(a)))
# Модули векторов
moduleA = sum(a[i]*a[i] for i in range(len(a)))**0.5
moduleB = sum(b[i]*b[i] for i in range(len(b)))**0.5

# Ищем угол
cosF = p / (moduleA * moduleB)
sinF = (1 - cosF**2)**0.5

# Считаем площадь
S = moduleA * moduleB * sinF / 2

print('ОТВЕТ')
print(S)
