class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        return [y[0] for y in sorted(zip(names, heights), key=lambda x: -x[1])]