m = [__import__("random").randint(1, 100) for _ in range(20)]


def hash_division(K, M):
    return K % M


def hash_multiply(K, M):
    С = 0.1
    return int(M * ((K * С) % 1))



print("Ключ", m[0])
print("Хэш деления", hash_division(m[0], len(m)))
print("Хэш умножения", hash_multiply(m[0], len(m)))


def hash_add(s, M=256):
    # тк как не указано количество закодированных символов, возьмем код символа функцией ord
    s = list(map(ord, s))
    h = sum(s) % M
    return h


print("Хеш сложения для", 'acd', hash_add('acd'))



