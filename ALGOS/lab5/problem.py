NO_OF_CHARS = 256


def badCharHeuristic(string, size):
    badChar = [-1] * NO_OF_CHARS
    for i in range(size):
        badChar[ord(string[i])] = i
    return badChar


def search_first(txt: str, pat:str):
    m = len(pat)
    n = len(txt)
    badChar = badCharHeuristic(pat, m)
    s = 0
    res = []
    while(s <= n-m):
        j = m-1
        while j >= 0 and pat[j] == txt[s+j]:
            j -= 1
        if j < 0:
            return True
            res.append(s)
            s += (m-badChar[ord(txt[s+m])] if s+m < n else 1)
        else:
            s += max(1, j-badChar[ord(txt[s+j])])
    return False


s1, s2 = input(), " " + " ".join(input().split()) + " "

spaces = 0
sas = 0
buff = 0
inc_words = 0
all_words = len(s1.split())
for i in range(len(s2)):
    if s2[i] == " ":
        spaces += 1
        if spaces == 4:
            pat = s2[sas + 1:i]
            if search_first(s1, pat):
                inc_words += 3 - min(buff, 3)
                buff = 2
            else:
                buff -= 1
            sas += 1
            while s2[sas] != " ":
                sas += 1
            spaces -= 1
             
             
print("{}%".format(inc_words / all_words * 100))
