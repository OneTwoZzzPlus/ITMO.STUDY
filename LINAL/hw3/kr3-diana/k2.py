# ВВОД ВЕКТОРОВ a, b
# a = (-4, -4, -2)
# b = (4, 1, -1)
# a = (-2, -1, 2)
# b = (3, 4, -3)
# a = (-4, 1, -2)
# b = (1, 4, 4)
# a = (-2,-4,2)
# b = (2,-3,-3)
# a = (-1,1,-3)
# b = (-1,2,3)
# a = (-5,1,4)
# b = (-2,-1,1)
a = (4,-1,1)
b = (2,-1,-1)

pr = sum(a[i]*b[i] for i in range(len(a))) / sum(a[i]*a[i] for i in range(len(a)))**0.5
print(pr)
