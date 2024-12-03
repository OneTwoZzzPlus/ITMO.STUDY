class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # ord(x) - 97 = hash(word)
        d = [0] * 27
        w = set()
        s = s.split()
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            n = ord(pattern[i]) - 97
            h = hash(s[i])
            if d[n] == 0 and h not in w:
                d[n] = h
                w.add(h)
            elif d[n] != h:
                return False
        return True