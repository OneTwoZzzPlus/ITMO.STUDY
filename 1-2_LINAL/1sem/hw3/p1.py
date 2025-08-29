# ВВОД ВЕКТОРОВ a, b
# a = (-4, -4, -2)
# b = (4, 1, -1)
a = (-2, -1, 2)
b = (3, 4, -3)

pr = sum(a[i]*b[i] for i in range(len(a))) / sum(a[i]*a[i] for i in range(len(a)))**0.5
print(pr)
