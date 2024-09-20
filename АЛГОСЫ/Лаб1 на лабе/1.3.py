'''
3)Без циклов
4)Без рекурсии
5)Не используя ничего, кроме print
'''

def power(n):
    return 1 if n==0 else 2*power(n-1) 

n = 7 # int(input())
r = power(n)
print(r)