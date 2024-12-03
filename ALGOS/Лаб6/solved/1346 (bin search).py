class Solution(object):
    def bin_s(self, x, down):
        low = 0
        high = len(self.arr) - 1
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            if self.arr[mid] < x:
                low = mid + 1
            elif self.arr[mid] > x:
                high = mid - 1
            else:
                if down:
                    for i in range(mid, 0, -1):
                        if self.arr[i - 1] != x:
                            break
                        mid -= 1
                    return mid
                else:
                    for i in range(mid, len(self.arr) - 1):
                        if self.arr[i + 1] != x:
                            break
                        mid += 1
                    return mid
        return low if down else high
        

    def bin_search(self, x, low, high):
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            if self.arr[mid] < x:
                low = mid + 1
            elif self.arr[mid] > x:
                high = mid - 1
            else:
                return True
        return False

    def checkIfExist(self, arr):
        self.arr = arr
        arr.sort()
        mi, ma = self.bin_s(arr[0] // 2, True), self.bin_s(arr[-1] // 2, False)
        for i in range(mi, ma + 1):
            if arr[i] == 0:
                if i + 1 < len(arr):
                    if arr[i + 1] == 0:
                        return True
            elif arr[i] < 0:
                if self.bin_search(arr[i] * 2, 0, i):
                    return True
            else:
                if self.bin_search(arr[i] * 2, i + 1, len(arr) - 1):
                    return True
        return False
