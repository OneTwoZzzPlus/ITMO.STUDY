class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        flag = False
        for ch in s:
            if ch == '0':
                flag = True
            if flag and ch == '1':
                return False
        return True