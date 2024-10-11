'''
Шахматное поле n*n. где n>=4
Разместить n ферзей, чтобы никто не нападал на другой
'''

n = int(input())
empty, ferz = '-', '♕'
desk = [[empty for _ in range(n)] for _ in range(n)]


if n % 2 == 0:
    left, right = n // 2 - 1, n - 1
    for s in range(0, n, 2):
        desk[s][left] = ferz
        desk[s + 1][right] = ferz
        left -= 1
        right -= 1
else:
    left, right = n // 2 - 1, n - 1
    for s in range(0, n - 1, 2):
        desk[s][right] = ferz
        desk[s + 1][left] = ferz
        left -= 1
        right -= 1
    desk[n - 1][n // 2] = ferz


# print('  ', '  '.join([str(x) for x in range(1, n + 1)]))
for x in range(n):
    # print(x + 1, end='  ')
    for y in range(n):
        print(desk[x][y], end='  ')
    print()
