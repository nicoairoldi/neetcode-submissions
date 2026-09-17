class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        while j < (len(t)-1) and i < (len(s)-1):
            if s[i] == t[j]:
                i = i+1
                j = j + 1
            else: 
                j = j + 1
        print(s)
        if i >= (len(s) - 1):
            return True
        return False