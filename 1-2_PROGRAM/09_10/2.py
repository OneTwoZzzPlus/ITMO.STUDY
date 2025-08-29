from inputter import input_float

d = int(str(abs(input_float("Введите число: "))).replace('.', '')[::-1])
print(d)
