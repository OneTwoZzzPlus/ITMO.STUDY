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

def pr(st):
    sp = []
    for j in range(1, len(st)+1):
        sp.append(0)
        for i in range(len(st[:j])):
            if st[:j][:i] == st[:j][-1*i:]:
                sp[-1] = max(sp[-1], i)
    return sp

        
v1 = prost()
v2 = fib()
mx, m = 0, ''
for ii in range(10, 100):
    pref = pr(str(ii))
    now = 0
    i = 0
    j = 0
    while i < len(v1):
        if v1[i] == str(ii)[j]:
            i += 1
            j += 1
            if j == 2:
                now += 1
                j = pref[j-1]
        else:
            if j > 0:
                j = pref[j-1]
            else:
                i += 1
    if now > mx:
        mx = now
        m = str(ii)
print('Вариант 1: Чаще всего встречается', m, ' - ', mx, 'раз')

mx, m = 0, ''
mx, m = 0, ''
for ii in range(10, 100):
    pref = pr(str(ii))
    now = 0
    i = 0
    j = 0
    while i < len(v2):
        if v2[i] == str(ii)[j]:
            i += 1
            j += 1
            if j == 2:
                now += 1
                j = 0
        else:
            if j > 0:
                j = pref[j-1]
            else:
                i += 1
    if now > mx:
        mx = now
        m = str(ii)
print('Вариант 2: Чаще всего встречается', m, ' - ', mx, 'раз')




