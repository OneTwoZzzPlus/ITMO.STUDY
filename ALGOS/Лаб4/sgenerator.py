def gen_primes(n: int) -> str:
    D, q, primes = {}, 2, ''
    while n > 0:
        if q not in D:
            n -= 1
            primes += str(q)     
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1
    return primes

def gen_fibonachi(n: int):
    fib1, fib2, fibonachi = 1, 1, '11'
    for _ in range(n-2):
        fib1, fib2 = fib2, fib1 + fib2
        fibonachi += str(fib2)
    return fibonachi
