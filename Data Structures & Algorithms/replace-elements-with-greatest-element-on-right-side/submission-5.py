class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = 0
        last = len(arr) -1
        j = last
        while j >= 0:
            saved = arr[j]
            if j == last:
                arr[j] = -1
            if j != last:
                arr[j] = m
            if saved > m:
                m = saved
            j = j - 1
        return arr