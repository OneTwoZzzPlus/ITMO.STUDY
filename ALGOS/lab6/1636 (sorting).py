class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        freq = {}
        for x in nums:
            freq[x] = freq.setdefault(x, 0) + 1

        return sorted(nums, key=lambda k: (freq[k], -k))

