class Solution(object):
    def twoSum(self, numbers, target):
        low = 0
        high = len(numbers) - 1
        while low < high:
            su = numbers[low] + numbers[high]
            if su == target:
                return [low + 1, high + 1]
            elif su > target:
                high -= 1
            else:
                low += 1