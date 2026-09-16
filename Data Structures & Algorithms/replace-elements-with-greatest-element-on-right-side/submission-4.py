class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = 0
        i = 0
        j = 1
        s = len(arr)-1
        #print(s)
        while i <= s:
            #print(f'i: {i}')
            #print(f'j: {j}')
            #print(f'm: {m}')
            if i == s:
                arr[i] = -1
                i = i + 1
            elif j > s:
                arr[i] = m
                i = i + 1
                j = i + 1
                m = 0
            elif arr[j] > m:
                m = arr[j]
                j = j + 1
            else: 
                j = j + 1
        return arr
