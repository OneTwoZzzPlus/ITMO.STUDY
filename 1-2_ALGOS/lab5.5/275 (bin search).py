class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        mh = 0
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            h = n - mid
            if citations[mid] == h:
                return h
            if citations[mid] > h:
                mh = max(mh, h)
                high = mid - 1
            elif citations[mid] < h:
                low = mid + 1
        return mh
    
    
print(Solution().hIndex([1,2,3,3,5,6,7]))