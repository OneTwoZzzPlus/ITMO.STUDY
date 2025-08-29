from turtle import *
screensize(10000, 10000)
left(90)
# tracer(0)
m = 100
d = m * 0.5 * 2**0.5

for _ in range(4):
    fd(m)
    lt(90)

lt(45)
fd(2*d)
rt(90)
fd(d)
rt(90)
fd(d)
rt(90)
fd(2*d)
lt(135)
fd(m)

done()