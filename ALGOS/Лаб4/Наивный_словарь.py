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

sl = {}
for i in range(len(v1)-1):
    if v1[i] != '0': #Дополнительное условие - подстрока не может начинаться с 0
        if v1[i:i+2] in sl:
            sl[v1[i:i+2]] += 1
        else:
            sl[v1[i:i+2]] = 1
mx = max(list(sl.values()))
for i in sl:
    if sl[i] == mx:
        print('Вариант 1: Чаще всего встречается', i, ' - ', mx, 'раз')
sl = {}
for i in range(len(v2)-1):
    if v2[i] != '0': #Дополнительное условие - подстрока не может начинаться с 0
        if v2[i:i+2] in sl:
            sl[v2[i:i+2]] += 1
        else:
            sl[v2[i:i+2]] = 1
mx = max(list(sl.values()))
for i in sl:
    if sl[i] == mx:
        print('Вариант 2: Чаще всего встречается', i, ' - ', mx, 'раз')


















