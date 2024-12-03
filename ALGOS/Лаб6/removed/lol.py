class Solution:
    def hash_ACGT(self, s: str) -> int:
        h = 0
        d = {"A": 0, "C": 1, "G": 2, "T": 3}
        for i in range(len(s)):
            h += d[s[i]] * (1 << (2 * i))
        return h

    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        result = {}
        answer = set()
        for i in range(len(s)-9):
            h = self.hash_ACGT(s[i:i+10])
            result[h] = (result.setdefault(h, (0,))[0] + 1, s[i:i+10])
        for v in result.values():
            if v[0] > 1:
                answer.add(v[1])
        return answer
    
    
print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))