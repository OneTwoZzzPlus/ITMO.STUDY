s = input("Введите текст > ")
print("ИСХОДНЫЙ:", s)
print("SWAPCASE:", s.swapcase())
print("ДЛИНА:", len(s))

n = ''
for x in s:
    if x == x.lower():
        n += x.upper()
    else:
        n += x.lower()
print("LOWER+UPPER:", n)
