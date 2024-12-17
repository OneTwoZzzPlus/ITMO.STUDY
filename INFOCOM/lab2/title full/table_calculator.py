s = [
r"\textbf{Наименование должности, ссылка, зарплата} & \textbf{Требования работодателя} & \textbf{Дисциплины из учебного плана} & \textbf{Преимущества вакансии} & \textbf{Недостатки вакансии} \\",
r"""
«Руководитель IT-проектов / project manager», оплата не указана, \url{https://hh.ru/vacancy/106836530}. &
Технические знания, опыт взаимодействия   с командой разработчиков; желание глубоко погрузиться в проект и сделать его еще   лучше; лидерские качества, инициативность и самостоятельность. &
Технологии командной разработки   программного обеспечения; Создание программного обеспечения;   Объектно-ориентированное программирование. &
50\% компенсация питания. &
Ответственность за команду.
""",
]

balance = [0, 0, 0, 0, 0]

ass = []
for i in range(len(s)):
    ass.append([len(x.strip().rstrip().replace('{', '').replace('}', '')
                     .replace('\\', '').replace('url', '').replace('ruble', 'руб.')
                     .replace('textbf', '')) for x in s[i].split('&')])

for i in range(len(ass)):
    ass[i] = [x/sum(ass[i]) for x in ass[i]]

a = []
for i in range(len(ass[0])):
    a.append(max([x[i] for x in ass]))
print(a)
m = 227  # mm
n = sum(a)
b = [int(m / n * x) for x in a]
b[-1] = m - sum(b[:-1])

print(b)
mis = [36, 30, 32, 37, 30]
mis = [mis[i] + balance[i] for i in range(len(mis))]
dis = [b[i]-mis[i] for i in range(len(mis))]
print(dis)
for i in range(len(dis)):
    if dis[i] < 0:
        while dis[i] < 0:
            if dis[i] >= 0:
                break
            for j in range(len(dis)):
                if dis[j] > 0:
                    b[j] -= 1
                    dis[j] -= 1
                    b[i] += 1
                    dis[i] += 1
                    if dis[i] >= 0:
                        break
print(b)
c = [str(x) for x in b]
r = '|p{' + 'mm}|p{'.join(c) + 'mm}|'
print(r)
