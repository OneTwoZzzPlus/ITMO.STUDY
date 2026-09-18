from sympy import *
# ВВОД ВЕКТОРОВ a, b, c и произведения
# a = [3, 0, -3]
# b = [1, 3, 3]
# c = [-5, 4, 4]
# prod_xc = -4
# a = [-3, 1, 3]
# b = [-2, -4, -1]
# c = [-5, 2, -5]
# prod_xc = -5
# a = [-1, -4, -1]
# b = [-1, -3, -5]
# c = [0, 2, 1]
# prod_xc = -2
# a = [-5, -4, -5]
# b = [1, 3, 0]
# c = [1, 1, -4]
# prod_xc = 1
# a = (1,-5,2)
# b = (-1,2,-1)
# c = (-1,2,-3)
# prod_xc = -2
a = (-1, 2, 1)
b = (3, -2, -4)
c = (-3, -4, 0)
prod_xc = -2

A = Matrix([a, b, c])
# Вектор значений
B = Matrix([0, 0, prod_xc])

x1, x2, x3 = symbols('x1 x2 x3')

det_A = A.det()
# Проверка на случай, если определитель главной матрицы равен нулю
if det_A == 0:
    raise ValueError("Определитель матрицы коэффициентов равен нулю, метод Крамера не применим.")

solutions = []
# Проходим по каждому столбцу матрицы и вычисляем определитель со заменой столбца на вектор значений
for i in range(A.shape[0]):
    Ai = A.copy()
    Ai[:, i] = B
    solutions.append(Ai.det() / det_A)

# Вывод результатов
sn = []
sd = []
for i, sol in enumerate(solutions, start=1):
    sn.append(f"{expand(sol)}")
    sd.append(str(float(sol.evalf(chop=True))))
print('ОТВЕТ')
print("[", ', '.join(sn), "]", sep="")
print('ОТВЕТ (десятичная дробь)')
print("[", ', '.join(sd), "]", sep="")
