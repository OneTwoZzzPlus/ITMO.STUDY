from turtle import *
screensize(10000, 10000)
# tracer(0)


n, m = 10, 100
d = 180 - ((n - 2) * 180 / n)

print(d)

for _ in range(n):
    fd(m)
    rt(d)

done()