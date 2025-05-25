class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s = sentence.split()
        lsw = len(searchWord)
        for i in range(len(s)):
            if len(s[i]) >= lsw:
                if s[i][:lsw] == searchWord:
                    return i + 1
        return -1