from sgenerator import *

def hash_2digit(s: str) -> int:
    return int(s) if s[0] != s[1] else int(s[0])

    
def RabinKarp(text: str, whash=hash_2digit) -> list[int]:
    mx, m = 0, ''
    for pattern in [str(x) for x in range(10, 100)]:
        
        result = 0
        pattern_hash = whash(pattern)
        for i in range(len(text)-1):
            if pattern_hash == whash(text[i:i+2]):
                if pattern == text[i:i+2]:
                    result += 1
                    
        if result > mx:
            mx = result
            m = pattern
    print(f'Шаблон {m} встречается {mx} раз')
        
        
RabinKarp(gen_primes(500))
RabinKarp(gen_fibonachi(500))