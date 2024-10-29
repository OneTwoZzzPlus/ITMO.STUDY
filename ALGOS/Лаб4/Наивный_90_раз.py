def fib():
    fb = [1, 1]
    for i in range(498):
        fb.append(fb[-2]+fb[-1])
    return ''.join(list(map(str, fb)))

def prost():
    pr = ['2', '3']
    i = 5
    while len(pr)!=500:
        check = True
        for j in range(3, int((i)**0.5)+3, 2):
            if i%j == 0:
                check = False
        if check:
            pr.append(str(i))
        i += 2
    return ''.join(pr)


v1 = prost()
v2 = fib()
mx, m = 0, ''
for j in range(10, 100):
    now = 0
    for i in range(len(v1)):
        if v1[i:i+2] == str(j): 
            now += 1
    if now > mx:
        mx = now
        m = str(j)
print('Вариант 1: Чаще всего встречается', m, ' - ', mx, 'раз')

mx, m = 0, ''
for j in range(10, 100):
    now = 0
    for i in range(len(v2)):
        if v2[i:i+2] == str(j): 
            now += 1
    if now > mx:
        mx = now
        m = str(j)
print('Вариант 2: Чаще всего встречается', m, ' - ', mx, 'раз')




