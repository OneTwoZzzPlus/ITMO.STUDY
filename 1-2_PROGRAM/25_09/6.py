def input_time(s: str) -> int:
    while True:
        r = input(s + ' > ')
        try:
            data = r.split(':')
            if len(data) == 2:
                h, m = int(data[0]), int(data[1])
                if 0 <= h <= 23 and 0 <= m <= 59:
                    return h * 60 + m
        except TypeError:
            pass


def min_to_hhmm(x: int) -> str:
    h, m = x // 60, x % 60
    return f"{h:02}:{m:02}"


m1 = input_time('Время отправления')
m2 = input_time('Время прибытия')

delta = (m2 - m1) if (m1 <= m2) else (m2 - m1 + 1440)

print(min_to_hhmm(delta))

