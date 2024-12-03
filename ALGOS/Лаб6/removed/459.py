class Solution:
    def divisors(self, n: int):
        d = {1}
        for i in range(2, int(n ** 0.5) + 1):
            if not n % i:
                d.add(i)
                d.add(n // i)
        return sorted(d)

    def repeatedSubstringPattern(self, s: str) -> bool:
        for d in self.divisors(len(s)):
            for i in range(d, len(s) - d + 1, d):
                if s[i - d:i] != s[i: i + d]:
                    break
            else:
                return True
        return False
    
    
print(Solution().repeatedSubstringPattern("abac"))
