class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        d={'A':1,'C':2,'G':3,'T':4}

        ans = set()
        curr = sum([d[x] * (4**(10-i)) for i, x in enumerate(s[:10])])
        z = {curr}
        for i in range (10, len(s)):
            curr = (curr - (d[s[i - 10]] * 4**10) + d[s[i]]) * 4
            if curr in z:
                ans.add(s[i - 9:i + 1])
            z.add(curr)
        return list(ans)
