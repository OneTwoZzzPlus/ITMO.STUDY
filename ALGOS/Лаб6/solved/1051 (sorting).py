class Solution:
    def QuickSort(self, a):
        if len(a) < 2:
            return a
        mid = len(a) // 2
        less, equals, more = [], [], []
        for x in a:
            if x == a[mid]:
                equals.append(x)
            elif x > a[mid]:
                more.append(x)
            else:
                less.append(x)
        return self.QuickSort(less) + equals + self.QuickSort(more)

    def heightChecker(self, heights: List[int]) -> int:
        expected = self.QuickSort(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count