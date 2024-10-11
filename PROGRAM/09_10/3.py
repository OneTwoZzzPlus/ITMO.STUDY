"""
FORMULA:
start * (1.1**(n-1)) >= finish * 1.1
1.1**(n) >= finish * 1.1 / start
log1.1(1.1**n) >= log1.1(finish * 1.1 / start)
n >= log1.1(finish * 1.1 / start)
TEST:
for i in range(1, n + 1):
    print(i, 1.1**(i-1) * start)
EFFICIENCY
O(1)
"""

from math import log, ceil

start, finish = float(input("Первый день = ")), float(input("Цель = "))
n = ceil(log(finish * 1.1 / start, 1.1))
print(f'На {n} день спортсмен добьётся успеха')

