from random import randint

N = int(input())
s = [randint(-100, 100) for i in range(N)]


def seq(l):
    maxim = 0
    p = [0, 0]
    n = 1
    k, m = 0, 0
    for i in range(1, len(l)):
        if l[i] >= l[i - 1]:
            n += 1
            m += 1
        else:
            if maxim < n:
                maxim = n
                p = [k, m]
            n = 1
            k = i
            m = i
    return l[p[0]:p[1] + 1]


print(s)
print(seq(s))
