s = input("Введите текст > ")
su = sum(int(x) for x in s if x.isdigit())
print(su)
